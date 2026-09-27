import streamlit as st
import requests

def render_dashboard():
    st.title("HOME: System Dashboard")

    try:
        res = requests.get("http://127.0.0.1:8000/system")
        hw_info = res.json()
    except Exception:
        hw_info = {"error": "Backend offline"}

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Hardware Status")
        st.write(f"**OS:** {hw_info.get('os', 'Unknown')}")
        st.write(f"**CPU:** {hw_info.get('cpu', 'Unknown')}")
        st.write(f"**RAM:** {hw_info.get('ram_gb', 0)} GB")
        st.write(f"**GPU:** {hw_info.get('gpu', 'None')}")
        st.write(f"**VRAM:** {hw_info.get('vram_gb', 0)} GB")

    with col2:
        st.subheader("AI Environment")
        st.write("**LAYA ROUTER:** ONLINE")
        st.write("**AGENTS:** READY")
        st.write("**RAG:** READY")
        st.write(f"**PROFILE:** {hw_info.get('profile', 'Unknown')}")

    with col3:
        st.subheader("Quick Actions")
        if st.button("Start New Chat"):
            st.session_state['page'] = "CHAT"
        if st.button("Verify Document"):
            st.session_state['page'] = "DOCUMENT VERIFICATION"
