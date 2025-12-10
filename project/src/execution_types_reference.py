import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Execution Type Icons Reference",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2rem;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #64748b;
        margin-bottom: 2rem;
    }
    .execution-code {
        background-color: #f1f5f9;
        padding: 4px 8px;
        border-radius: 4px;
        font-family: monospace;
        color: #334155;
    }
    .lucide-code {
        background-color: #dbeafe;
        padding: 4px 8px;
        border-radius: 4px;
        font-family: monospace;
        color: #1e40af;
    }
    .note-box {
        background-color: #fef3c7;
        border: 1px solid: #fbbf24;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    .implementation-box {
        background-color: #dbeafe;
        border: 1px solid #93c5fd;
        border-radius: 8px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    .icon-preview {
        width: 40px;
        height: 40px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #f8fafc;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">Execution Type Icons Reference</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Ant Design icon equivalents using Lucide React</p>', unsafe_allow_html=True)

# Execution types data
execution_types = [
    {
        'code': 'TEST_MANUAL',
        'icon_name': 'ExperimentOutlined',
        'lucide_icon': 'FlaskConical',
        'description': 'Execution triggered manually for testing.',
        'color': '#9333ea',
        'color_name': 'purple',
        'emoji': '🧪'
    },
    {
        'code': 'EXEC_MANUAL',
        'icon_name': 'PlayCircleOutlined',
        'lucide_icon': 'PlayCircle',
        'description': 'Execution started manually by a user.',
        'color': '#2563eb',
        'color_name': 'blue',
        'emoji': '▶️'
    },
    {
        'code': 'EXEC_SCHED',
        'icon_name': 'ClockCircleOutlined',
        'lucide_icon': 'Clock',
        'description': 'Execution triggered by a schedule.',
        'color': '#16a34a',
        'color_name': 'green',
        'emoji': '🕐'
    },
    {
        'code': 'EXEC_LISTENER',
        'icon_name': 'ApiOutlined',
        'lucide_icon': 'Webhook',
        'description': 'Execution triggered by an event/listener.',
        'color': '#ea580c',
        'color_name': 'orange',
        'emoji': '🔗'
    },
    {
        'code': 'EXEC_LISTENER_BRIDGE',
        'icon_name': 'ApiOutlined + EyeOutlined',
        'lucide_icon': 'ScanEye',
        'description': 'Execution triggered by a bridged listener connection.',
        'color': '#ec4899',
        'color_name': 'pink',
        'emoji': '👁️'
    },
    {
        'code': 'SUB_PROCESS',
        'icon_name': 'BranchesOutlined',
        'lucide_icon': 'GitBranch',
        'description': 'Execution invoked by another parent process.',
        'color': '#0891b2',
        'color_name': 'cyan',
        'emoji': '🌿'
    },
    {
        'code': 'UNKNOWN',
        'icon_name': 'QuestionCircleOutlined',
        'lucide_icon': 'HelpCircle',
        'description': 'Execution type could not be identified.',
        'color': '#6b7280',
        'color_name': 'gray',
        'emoji': '❓'
    },
    {
        'code': 'RETRY_MANUAL',
        'icon_name': 'ReloadOutlined',
        'lucide_icon': 'RotateCw',
        'description': 'Re-execution triggered manually after fail.',
        'color': '#f59e0b',
        'color_name': 'amber',
        'emoji': '🔄'
    },
    {
        'code': 'RETRY_SCHED',
        'icon_name': 'FieldTimeOutlined',
        'lucide_icon': 'Timer',
        'description': 'Re-execution triggered automatically.',
        'color': '#6366f1',
        'color_name': 'indigo',
        'emoji': '⏱️'
    }
]

# Display table
st.markdown("---")

# Create DataFrame for better display
df_display = []
for exec_type in execution_types:
    df_display.append({
        'Icon': exec_type['emoji'],
        'Execution Type Code': exec_type['code'],
        'Ant Design Icon': exec_type['icon_name'],
        'Lucide Equivalent': exec_type['lucide_icon'],
        'Description': exec_type['description'],
        'Color': exec_type['color_name'].capitalize()
    })

df = pd.DataFrame(df_display)

# Display the dataframe with custom styling
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Icon": st.column_config.TextColumn(
            "Icon",
            width="small",
        ),
        "Execution Type Code": st.column_config.TextColumn(
            "Execution Type Code",
            width="medium",
        ),
        "Ant Design Icon": st.column_config.TextColumn(
            "Ant Design Icon",
            width="medium",
        ),
        "Lucide Equivalent": st.column_config.TextColumn(
            "Lucide Equivalent",
            width="medium",
        ),
        "Description": st.column_config.TextColumn(
            "Description",
            width="large",
        ),
        "Color": st.column_config.TextColumn(
            "Color",
            width="small",
        ),
    }
)

# Implementation Example
st.markdown("---")
st.markdown('<div class="implementation-box">', unsafe_allow_html=True)
st.markdown("### 💻 Implementation Example")
st.markdown("**React + Lucide Icons:**")

code_example = """import { 
  FlaskConical,
  PlayCircle,
  Clock,
  Webhook,
  GitBranch,
  HelpCircle,
  RotateCw,
  Timer,
  ScanEye
} from 'lucide-react';

// Usage in your component:
<FlaskConical size={20} style={{ color: '#9333ea' }} />
<PlayCircle size={20} style={{ color: '#2563eb' }} />
<Clock size={20} style={{ color: '#16a34a' }} />
<Webhook size={20} style={{ color: '#ea580c' }} />
<ScanEye size={20} style={{ color: '#ec4899' }} />
<GitBranch size={20} style={{ color: '#0891b2' }} />
<HelpCircle size={20} style={{ color: '#6b7280' }} />
<RotateCw size={20} style={{ color: '#f59e0b' }} />
<Timer size={20} style={{ color: '#6366f1' }} />"""

st.code(code_example, language="jsx")
st.markdown('</div>', unsafe_allow_html=True)

# Note section
st.markdown('<div class="note-box">', unsafe_allow_html=True)
st.markdown("### ⚠️ Note")
st.markdown("""
**Ant Design icons have compatibility issues in this environment.** 
The table shows **Lucide React equivalents** that match the semantic meaning 
of each Ant Design icon. These icons are visually similar and work seamlessly.
""")
st.markdown("""
**📚 Lucide React Icon Library:** [https://lucide.dev](https://lucide.dev) — Browse 1000+ open-source icons
""")
st.markdown('</div>', unsafe_allow_html=True)

# Detailed breakdown section
st.markdown("---")
st.markdown("### 📊 Detailed Breakdown")

# Create tabs for each execution type
for exec_type in execution_types:
    with st.expander(f"{exec_type['emoji']} {exec_type['code']} - {exec_type['description']}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"**Execution Type Code:**")
            st.code(exec_type['code'])
            st.markdown(f"**Ant Design Icon:**")
            st.write(exec_type['icon_name'])
            st.markdown(f"**Lucide React Equivalent:**")
            st.code(exec_type['lucide_icon'])
        
        with col2:
            st.markdown(f"**Color:**")
            st.markdown(f'<div style="width: 60px; height: 60px; background-color: {exec_type["color"]}; border-radius: 8px; border: 2px solid #e2e8f0;"></div>', unsafe_allow_html=True)
            st.markdown(f"<small>{exec_type['color']} ({exec_type['color_name']})</small>", unsafe_allow_html=True)
            st.markdown(f"**Description:**")
            st.write(exec_type['description'])

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748b; padding: 2rem 0;'>
    <p>Generated from Figma Make: Select Icons for Execution Types</p>
    <p>This reference guide helps maintain consistency across your application's execution type indicators.</p>
</div>
""", unsafe_allow_html=True)


