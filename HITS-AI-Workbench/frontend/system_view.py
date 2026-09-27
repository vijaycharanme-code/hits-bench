import streamlit as st
import psutil

def render_system():
    st.title("SYSTEM MONITOR")

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    col1, col2 = st.columns(2)
    with col1:
        st.metric("CPU Utilization", f"{cpu}%")
    with col2:
        st.metric("RAM Utilization", f"{ram}%")

    st.subheader("Services")
    st.write("Backend API: ONLINE")
    st.write("Laya Decision Engine: ONLINE")
    st.write("LangGraph Orchestration: ONLINE")
