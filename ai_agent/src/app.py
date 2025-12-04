"""Streamlit app for the AI Agent."""
import streamlit as st
import logging
from ai_agent import AIAgent
from excel_processor import ExcelProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)

# Page configuration
st.set_page_config(
    page_title="User Data AI Agent",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if 'agent' not in st.session_state:
    try:
        st.session_state.agent = AIAgent()
        st.session_state.messages = []
    except ValueError as e:
        st.error(f"Configuration error: {str(e)}")
        st.stop()

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'processed_users' not in st.session_state:
    st.session_state.processed_users = None

# Title and description
st.title("🤖 User Data AI Agent")
st.markdown("""
This AI agent helps you upload Excel files with user data and update the user service.
Upload an Excel file with user information (must include an 'id' column) and the agent will help you process it.
""")

# Sidebar for file upload
with st.sidebar:
    st.header("📁 Upload Excel File")
    uploaded_file = st.file_uploader(
        "Choose an Excel file",
        type=['xlsx', 'xls'],
        help="Upload an Excel file with user data. Must include an 'id' column."
    )
    
    if uploaded_file is not None:
        file_content = uploaded_file.read()
        st.success(f"File uploaded: {uploaded_file.name}")
        
        # Process file immediately
        try:
            processor = ExcelProcessor()
            users = processor.process_excel_file(file_content)
            st.session_state.processed_users = users
            st.info(f"✅ Processed {len(users)} users from the file")
            
            # Show preview
            with st.expander("Preview Users"):
                st.json(users[:5])  # Show first 5 users
        except Exception as e:
            st.error(f"Error processing file: {str(e)}")
    
    st.divider()
    
    # Action buttons
    if st.session_state.processed_users:
        st.header("⚡ Actions")
        if st.button("🔄 Update Users in Service", type="primary"):
            with st.spinner("Updating users..."):
                results = st.session_state.agent.update_users(st.session_state.processed_users)
                
                if "error" in results:
                    st.error(results["error"])
                else:
                    st.success(f"✅ Updated {results['successful']}/{results['total']} users successfully")
                    if results['failed'] > 0:
                        st.warning(f"⚠️ {results['failed']} users failed to update")
                    
                    # Show detailed results
                    with st.expander("View Detailed Results"):
                        st.json(results['results'])
        
        if st.button("🗑️ Clear Processed Data"):
            st.session_state.processed_users = None
            st.rerun()

# Chat interface
st.header("💬 Chat with AI Agent")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me to help you upload and process user data..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get file content if available
    file_content = None
    if uploaded_file is not None and st.session_state.processed_users is None:
        file_content = uploaded_file.read()
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.agent.chat(prompt, file_content)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

# Initialize conversation if empty
if len(st.session_state.messages) == 0:
    initial_message = st.session_state.agent.chat("Hello! I'm ready to help you upload and process user data from Excel files.")
    st.session_state.messages.append({"role": "assistant", "content": initial_message})
    with st.chat_message("assistant"):
        st.markdown(initial_message)

