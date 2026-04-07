import google.generativeai as genai
import streamlit as st

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use your chosen model
model = genai.GenerativeModel("gemini-2.5-flash")


def explain_name_analysis(name, token_count, tgdi, cost, tokens):
    prompt = f"""
    You are an expert in NLP fairness and tokenization bias.

    Analyze the following name:

    Name: {name}
    Token Count: {token_count}
    TGDI: {tgdi}
    Cost: ${cost}
    Token Breakdown: {tokens}

    Provide a structured explanation with these sections:

    1. Tokenization Insight  
    2. Fragmentation & Bias Risk  
    3. Cost Implication  
    4. Cultural / Representation Impact  

    Keep it concise, clear, and slightly academic.
    """

    response = model.generate_content(prompt)
    return response.text
