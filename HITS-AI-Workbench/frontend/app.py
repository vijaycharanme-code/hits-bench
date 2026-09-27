import streamlit as st
import sys
from pathlib import Path

# Add project root to sys.path so we can import from backend/core if needed
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from frontend.dashboard import render_dashboard
from frontend.chat import render_chat
from frontend.documents import render_documents
from frontend.agents import render_agents
from frontend.router_view import render_router
from frontend.system_view import render_system

st.set_page_config(
    page_title="HITS AI Workbench",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for dark industrial theme
st.markdown("""
<style>
    /* Dark industrial theme */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }
    .css-1d391kg {
        background-color: #1e1e1e;
    }
    h1, h2, h3 {
        color: #ff9800;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #333333;
        color: #ff9800;
        border: 1px solid #ff9800;
        border-radius: 4px;
    }
    .stButton>button:hover {
        background-color: #ff9800;
        color: #121212;
    }
    .status-online { color: #4caf50; font-weight: bold; }
    .status-offline { color: #f44336; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

def main():
    st.sidebar.title("HITS AI WORKBENCH")
    st.sidebar.markdown("---")

    pages = {
        "HOME": render_dashboard,
        "CHAT": render_chat,
        "DOCUMENT VERIFICATION": render_documents,
        "AGENTS": render_agents,
        "ROUTER": render_router,
        "SYSTEM": render_system
    }

    selection = st.sidebar.radio("Navigation", list(pages.keys()))

    st.sidebar.markdown("---")
    st.sidebar.markdown("<div class='status-online'>SYSTEM ONLINE</div>", unsafe_allow_html=True)

    # Render selected page
    pages[selection]()

if __name__ == "__main__":
    main()
