import streamlit as st
import requests

# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000/my_chatbot"

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #172554);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #93c5fd;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 15px;
    margin-bottom: 30px;
}

[data-testid="stChatMessage"] {
    background-color: rgba(255,255,255,0.08);
    border-radius: 15px;
    padding: 15px;
    border: 1px solid rgba(255,255,255,0.10);
}

[data-testid="stChatInput"] {
    border-radius: 15px;
}

div.stButton > button {
    border-radius: 10px;
    border: none;
    background-color: #2563eb;
    color: white;
}

div.stButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- HEADER ----------------

st.markdown(
    '<div class="main-title">🤖 My AI Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your personal AI chatbot • Powered by OpenAI</div>',
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.title("💬 Chat Settings")

    st.write("Welcome to your AI assistant!")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Built with Python, FastAPI, Streamlit and OpenAI.")

# ---------------- WELCOME MESSAGE ----------------

if not st.session_state.messages:
    st.info(
        "👋 Hello! I'm your AI assistant. "
        "Ask me anything to get started."
    )

# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- CHAT INPUT ----------------

user_input = st.chat_input("Type your message here...")

if user_input:

    # Display and save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response from FastAPI
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):

            try:
                response = requests.post(
                    API_URL,
                    json={"message": user_input},
                    timeout=120
                )

                response.raise_for_status()

                bot_response = response.json()["response"]

                st.markdown(bot_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_response
                })

            except requests.exceptions.ConnectionError:
                st.error(
                    "Cannot connect to FastAPI. "
                    "Please start your backend server."
                )

            except requests.exceptions.Timeout:
                st.error("The request timed out. Please try again.")

            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {e}")

            except (ValueError, KeyError):
                st.error("The API returned an unexpected response.")
