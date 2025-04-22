
import streamlit as st

st.set_page_config(page_title="Patient Diary Chatbot", layout="centered")

st.title("💬 GenAI Patient Diary Assistant")

# CSS for left/right chat bubbles
st.markdown("""
<style>
.chat-bubble {
    padding: 10px 15px;
    border-radius: 20px;
    margin: 10px 0;
    max-width: 75%;
    display: inline-block;
}
.left {
    background-color: #f0f2f6;
    text-align: left;
    float: left;
    clear: both;
}
.right {
    background-color: #d1e7dd;
    text-align: right;
    float: right;
    clear: both;
}
.clearfix {
    clear: both;
}
</style>
""", unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your Patient Diary Assistant. How are you feeling today?"}
    ]

# Render all messages
for msg in st.session_state.messages:
    role_class = "left" if msg["role"] == "assistant" else "right"
    st.markdown(
        f'<div class="chat-bubble {role_class}">{msg["content"]}</div><div class="clearfix"></div>',
        unsafe_allow_html=True
    )

# User input
if prompt := st.chat_input("Type your diary entry..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(
        f'<div class="chat-bubble right">{prompt}</div><div class="clearfix"></div>',
        unsafe_allow_html=True
    )

    # Simulated response logic
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
    st.markdown(
        f'<div class="chat-bubble left">{response}</div><div class="clearfix"></div>',
        unsafe_allow_html=True
    )
