import streamlit as st
from utils.chatbot import ask_gemini

st.title("🤖 AI Assistant (Tokenization Bias Expert)")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User input
prompt = st.chat_input("Ask about tokenization bias...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get Gemini response
    response = ask_gemini(prompt)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)