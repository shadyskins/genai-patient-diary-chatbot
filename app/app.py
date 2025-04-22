
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Patient Diary Chatbot", layout="centered")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Patient Diary Assistant. How are you feeling today?"}
    ]

st.title("🧠 Patient Diary Chatbot (Simulated)")

# Chat interface with persistent memory
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your diary entry..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Simulated follow-up logic
    if "weird" in prompt or "off" in prompt or "funny" in prompt:
        response = "Can you describe more? Was it dizziness, nausea, or something else?"
    elif "sleep" in prompt:
        response = "On a scale from 1 to 10, how well did you sleep?"
    elif "pain" in prompt:
        response = "Where did you feel the pain and how severe was it?"
    elif "tired" in prompt:
        response = "Was it fatigue, sleepiness, or physical exhaustion?"
    else:
        response = "Thanks for sharing. Can you tell me more about how that made you feel?"
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
