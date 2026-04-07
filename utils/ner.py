from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_models():
    bert = pipeline("ner", model="dslim/bert-large-NER", aggregation_strategy="simple")
    babel = pipeline("ner", model="babelscape/wikineural-multilingual-ner", aggregation_strategy="simple")
    return bert, babel

def run_ner(name, model):
    sentence = f"Please contact {name} regarding the report."
    result = model(sentence)
    predicted = " ".join([e['word'] for e in result if e['entity_group'] == 'PER'])

    if not predicted:
        error = "No Match"
    elif predicted == name:
        error = "Perfect Match"
    elif name in predicted:
        error = "Partial Match"
    else:
        error = "Misclassification"

    return predicted, error