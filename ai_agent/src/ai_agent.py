"""AI Agent using Google AI SDK for chat interface."""
import google.generativeai as genai
import logging
from typing import Optional, List, Dict
from config import GOOGLE_AI_API_KEY, MODEL_NAME
from excel_processor import ExcelProcessor
from user_service_client import UserServiceClient

logger = logging.getLogger(__name__)


class AIAgent:
    """AI Agent that handles chat interactions and user data processing."""
    
    def __init__(self):
        if not GOOGLE_AI_API_KEY:
            raise ValueError("GOOGLE_AI_API_KEY must be set in environment variables or .env file")
        
        genai.configure(api_key=GOOGLE_AI_API_KEY)
        self.model = genai.GenerativeModel(MODEL_NAME)
        self.excel_processor = ExcelProcessor()
        self.user_service_client = UserServiceClient()
        self.conversation_history = []
        
        # System prompt
        self.system_prompt = """You are a helpful AI assistant that helps users upload Excel files with user data 
        and update a user service. Your main tasks are:
        1. Greet users and explain that you can help them upload Excel files with user information
        2. Ask users to upload an Excel file containing user data (must have an 'id' column)
        3. Once a file is uploaded, process it and confirm the data
        4. Ask for confirmation before making API calls to update users
        5. Provide clear feedback on the results
        
        Be friendly, professional, and helpful. Always confirm actions before executing them."""
    
    def chat(self, user_message: str, file_content: Optional[bytes] = None) -> str:
        """
        Process a chat message and optionally handle file upload.
        
        Args:
            user_message: The user's message
            file_content: Optional bytes content of an uploaded Excel file
            
        Returns:
            Agent's response message
        """
        # If file is provided, process it
        if file_content:
            try:
                users = self.excel_processor.process_excel_file(file_content)
                num_users = len(users)
                
                # Add context about the processed file
                file_context = f"\n[System: User uploaded an Excel file with {num_users} users. "
                file_context += f"Ready to update user service. Users: {users[:3]}...]"
                user_message += file_context
                
                # Store processed users for potential update
                self.processed_users = users
                
            except Exception as e:
                error_msg = f"Error processing Excel file: {str(e)}"
                logger.error(error_msg)
                return f"I encountered an error while processing your Excel file: {str(e)}\n\nPlease check that your file:\n- Is a valid Excel file (.xlsx or .xls)\n- Contains an 'id' column\n- Has no duplicate IDs\n\nWould you like to try uploading another file?"
        
        # Build conversation context
        conversation_text = self.system_prompt + "\n\n"
        for msg in self.conversation_history[-5:]:  # Keep last 5 messages for context
            conversation_text += f"User: {msg['user']}\nAssistant: {msg['assistant']}\n\n"
        conversation_text += f"User: {user_message}\nAssistant:"
        
        try:
            # Generate response
            response = self.model.generate_content(conversation_text)
            assistant_message = response.text
            
            # Store in conversation history
            self.conversation_history.append({
                'user': user_message,
                'assistant': assistant_message
            })
            
            return assistant_message
            
        except Exception as e:
            logger.error(f"Error generating AI response: {str(e)}")
            return f"I encountered an error: {str(e)}. Please try again."
    
    def update_users(self, users: Optional[List[Dict]] = None) -> Dict:
        """
        Update users in the user service.
        
        Args:
            users: Optional list of users to update (uses processed_users if not provided)
            
        Returns:
            Dictionary with update results
        """
        if users is None:
            if not hasattr(self, 'processed_users'):
                return {"error": "No users to update. Please upload an Excel file first."}
            users = self.processed_users
        
        results = self.user_service_client.patch_users_batch(users)
        
        # Calculate statistics
        total = len(results)
        successful = sum(1 for success in results.values() if success)
        failed = total - successful
        
        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "results": results
        }
    
    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = []
        if hasattr(self, 'processed_users'):
            delattr(self, 'processed_users')

