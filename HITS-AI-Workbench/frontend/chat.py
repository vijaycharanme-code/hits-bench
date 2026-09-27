import streamlit as st
import requests

def render_chat():
    st.title("AGENTIC CHAT")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Enter your task or instruction..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Processing with Laya...")

            try:
                res = requests.post("http://127.0.0.1:8000/chat", json={"message": prompt})
                if res.status_code == 200:
                    data = res.json()
                    response_text = data["response"]
                    decision = data["decision"]

                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    message_placeholder.markdown(response_text)

                    with st.expander("Laya Routing Details"):
                        st.json(decision)
                else:
                    message_placeholder.markdown(f"Error: {res.status_code}")
            except Exception as e:
                message_placeholder.markdown(f"Backend connection error: {e}")
