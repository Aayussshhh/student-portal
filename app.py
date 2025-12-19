
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="AI MCQ Generator", page_icon="📝")

st.title("📝 AI MCQ Generator")
st.subheader("Generate high-quality questions from any text")

# Input Section
text_input = st.text_area("Paste your content here:", height=200)
num_questions = st.slider("Number of questions", min_value=1, max_value=10, value=3)

if st.button("Generate MCQs"):
    if not text_input:
        st.error("Please provide some text first!")
    else:
        with st.spinner("Generating questions..."):
            prompt = f"""
            Generate {num_questions} multiple-choice questions based on the following text. 
            Format each question as follows:
            Question: [The question]
            A) [Option]
            B) [Option]
            C) [Option]
            D) [Option]
            Correct Answer: [Letter]
            
            Text: {text_input}
            """
            
            try:
                response = model.generate_content(prompt)
                st.success("Generated successfully!")
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.sidebar.info("Built with Streamlit and Gemini API")
