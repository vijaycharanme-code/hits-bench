import streamlit as st

def render_router():
    st.title("LAYA ROUTER AUDIT LOG")
    st.write("Shows recent Laya decisions, classification, and security checks.")

    # Placeholder for database integration
    st.table([
        {"id": 1, "task_type": "document_verification", "agent": "document_agent", "safe": True},
        {"id": 2, "task_type": "technical_analysis", "agent": "engineer_agent", "safe": True}
    ])
