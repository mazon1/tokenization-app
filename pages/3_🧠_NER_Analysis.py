import streamlit as st
from utils.ner import load_models, run_ner

st.title("🧠 NER Analysis")

bert, babel = load_models()

name = st.text_input("Enter name")

model_choice = st.selectbox("Choose Model", ["BERT", "Babelscape"])

if name:
    model = bert if model_choice == "BERT" else babel

    pred, error = run_ner(name, model)

    st.metric("Predicted Name", pred)
    st.metric("Error Type", error)