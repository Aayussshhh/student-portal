import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Configure Groq Client
client = Groq(api_key=api_key)

st.title("MCQ Generator")

# Input Section
text_input = st.text_area("Paste your content here:", height=200)
num_questions = st.slider("Number of questions", min_value=1, max_value=30, value=5)

if st.button("Generate MCQs"):
    if not text_input:
        st.error("Please provide some text first!")
    else:
        with st.spinner("Generating questions at lightning speed..."):
            try:
                # Call Groq Chat Completion
                response = client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": f"Generate {num_questions} multiple-choice questions from the text. Format: Question, Options (A-D), and Correct Answer."
                        },
                        {
                            "role": "user",
                            "content": text_input,
                        }
                    ],
                    # Common Groq models: 'llama-3.3-70b-versatile' or 'llama-3.1-8b-instant'
                    model="llama-3.3-70b-versatile", 
                )
                
                st.success("Generated successfully!")
                st.markdown("---")
                # Access the content through choices[0].message.content
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
