import os
import time
import streamlit as st
import google.generativeai as genai

# ---------------------------
# CONFIGURATION
# ---------------------------
st.set_page_config(
    page_title="InterviewPilot — AI Interview Agent",
    page_icon="🎯",
    layout="wide"
)

# Sidebar UI — Gemini API key + model selection
st.sidebar.title("⚙️ Settings")

API_KEY = st.sidebar.text_input(
    "🔑 Enter Gemini API Key",
    type="password",
    placeholder="Paste from Google AI Studio"
)

model_name = st.sidebar.selectbox(
    "Model",
    ["gemini-flash-latest", "gemini-2.5-flash", "gemini-2.5-pro"]
)

feedback_enabled = st.sidebar.checkbox(
    "✅ Give feedback before next question", value=True
)

temperature = st.sidebar.slider(
    "Creativity (temperature)",
    min_value=0.0, max_value=1.0, value=0.4, step=0.1
)

# Stop execution until key exists
if not API_KEY:
    st.warning("Enter your Gemini API key to start.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)


# ---------------------------
# INITIALIZE SESSION STATE
# ---------------------------
if "chat" not in st.session_state:
    st.session_state.chat = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "role" not in st.session_state:
    st.session_state.role = "Data Analyst"


# ---------------------------
# MAIN UI
# ---------------------------
st.title("🎯 InterviewPilot — AI Interview Agent")
st.caption("Practice role-based technical interviews with smart adaptive follow-ups.")

st.session_state.role = st.text_input(
    "Enter the job role you want to be interviewed for:",
    st.session_state.role
)

# Start / Reset button
if st.button("▶️ Start Interview / Reset"):
    model = genai.GenerativeModel(
        model_name,
        generation_config={"temperature": temperature}
    )

    st.session_state.chat = model.start_chat(history=[])
    st.session_state.messages = []  # reset chat history

    intro_prompt = f"""
    You are a professional interviewer for the role: {st.session_state.role}.
    Rules:
    - Ask ONLY one question at a time.
    - Keep questions technical and scenario-based.
    - After user's answer, ask a follow-up question.
    - Be concise.
    """
    first_question = st.session_state.chat.send_message(intro_prompt).text
    st.session_state.messages.append(("assistant", first_question))


# Display chat history on screen
for role, msg in st.session_state.messages:
    with st.chat_message("assistant" if role == "assistant" else "user"):
        st.markdown(msg)


# ---------------------------
# USER INPUT AREA
# ---------------------------
user_input = st.chat_input("Your answer here...")

if user_input:
    # Display user answer
    st.session_state.messages.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    # Build interviewer prompt
    add_feedback = (
        "Before asking next question, give a short 2–3 line evaluation of my answer."
        if feedback_enabled else ""
    )

    # Get response from Gemini
    prompt = f"{user_input}\n\n{add_feedback}"
    response = st.session_state.chat.send_message(prompt).text

    # Typewriter effect
    with st.chat_message("assistant"):
        placeholder = st.empty()
        generated = ""
        for word in response.split():
            generated += word + " "
            placeholder.markdown(generated)
            time.sleep(0.01)

    st.session_state.messages.append(("assistant", response))
