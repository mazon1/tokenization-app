import google.generativeai as genai
import streamlit as st

# Configure API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

def ask_gemini(question):
    system_prompt = """
    You are an expert in tokenization bias in NLP systems.

    You help users understand:
    - Token fragmentation
    - Cultural bias in names
    - TGDI metric
    - NER errors
    - API cost implications

    Always give clear, structured, and practical explanations.
    """

    response = model.generate_content(
        system_prompt + "\nUser: " + question
    )

    return response.text