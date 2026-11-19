
import streamlit as st
import requests

st.title("My AI Chatbot")

user_id = st.text_input("Enter your User ID")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_message = st.chat_input("Type your message here...")

if user_message:

    if not user_id:
        st.warning("Please enter your User ID first.")

    else:
        st.session_state.messages.append({
            "role": "user",
            "content": user_message
        })

        with st.chat_message("user"):
            st.write(user_message)

        try:
            response = requests.post(
                "http://127.0.0.1:8000/my_chatbot",
                json={
                    "user_id": user_id,
                    "message": user_message
                }
            )

            response.raise_for_status()
            bot_reply = response.json()["response"]

            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_reply
            })

            with st.chat_message("assistant"):
                st.write(bot_reply)

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to chatbot: {e}")
