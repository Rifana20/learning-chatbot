import streamlit as st
import google.generativeai as genai
import streamlit as st
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Prompt style
BASE_PROMPT = (
    "You are a helpful, patient AI tutor who teaches students up to 10th grade. "
    "Explain concepts simply, clearly, and include a simple ASCII diagram or text illustration "
    "if possible to help the student visualize."
)

st.title("AI Teaching Assistant (with simple diagrams)")

language = st.selectbox("Choose language for the answer:", ["English", "Hindi", "Malayalam"])

user_question = st.text_input("Ask your question (in English, for best results):")

if user_question:
    with st.spinner("Thinking..."):
        full_prompt = (
            f"{BASE_PROMPT}\n"
            f"Provide the answer in {language}.\n"
            f"Question: {user_question}"
        )
        response = model.generate_content(full_prompt)
        st.markdown(f"**Answer ({language}):**\n\n{response.text}")
