import streamlit as st

def render_agents():
    st.title("AGENTS STATUS")

    st.subheader("Engineer Agent")
    st.write("Status: ONLINE | Tools: OCR, RAG, Vision, Calculator")

    st.subheader("Supervisor Agent")
    st.write("Status: ONLINE | Tools: Excel, Reports")

    st.subheader("HR Agent")
    st.write("Status: ONLINE | Tools: DOCX, Excel, Verification")

    st.subheader("Document Agent")
    st.write("Status: ONLINE | Tools: PDF, DOCX, OCR")

    st.subheader("Verifier Agent")
    st.write("Status: ONLINE | Tools: Evidence Check, Consistency")
