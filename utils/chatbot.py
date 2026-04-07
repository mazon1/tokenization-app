import google.generativeai as genai
import streamlit as st

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Use your chosen model
model = genai.GenerativeModel("gemini-2.5-flash")


# -------------------------------
# 🔹 TOKENIZATION EXPLANATION
# -------------------------------
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


# -------------------------------
# 🔹 NER EXPLANATION (NEW 🔥)
# -------------------------------
def explain_ner_result(name, predicted_name, error_type, model_name):
    prompt = f"""
    You are an expert in NLP fairness and Named Entity Recognition (NER).

    Analyze the following result:

    Name: {name}
    Model: {model_name}
    Predicted Output: {predicted_name}
    Error Type: {error_type}

    Provide a structured explanation with these sections:

    1. What Happened  
    Explain what the model did.

    2. Error Interpretation  
    Why did this error occur (e.g., No Match, Partial Match)?

    3. Link to Tokenization  
    Explain how tokenization fragmentation could have contributed.

    4. Bias Implication  
    Discuss whether this suggests bias against non-Western names.

    Keep it concise, clear, and analytical.
    """

    response = model.generate_content(prompt)
    return response.text
