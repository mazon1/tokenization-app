import streamlit as st
from utils.ner import load_models, run_ner
from utils.chatbot import explain_ner_result

# Page config
st.set_page_config(layout="wide")

st.title("🧠 NER Analysis")

# -------------------------------
# 🔹 LOAD MODELS
# -------------------------------
bert, babel = load_models()

# -------------------------------
# 🔹 INPUTS
# -------------------------------
name = st.text_input("Enter name", "Chimaobi")

model_choice = st.selectbox("Choose Model", ["BERT", "Babelscape"])

# -------------------------------
# 🔹 RUN NER
# -------------------------------
if name:
    model = bert if model_choice == "BERT" else babel

    pred, error = run_ner(name, model)

    # Handle empty prediction
    predicted_name = pred if pred else "None"

    # -------------------------------
    # 🔹 METRICS
    # -------------------------------
    col1, col2 = st.columns(2)

    col1.metric("Predicted Name", predicted_name)
    col2.metric("Error Type", error)

    # -------------------------------
    # 🔹 AI INTERPRETATION 🔥
    # -------------------------------
    st.subheader("🤖 AI Interpretation")
    st.caption("AI explanation of NER model behavior")

    cache_key = f"{name}_{model_choice}_{error}"

    if "ner_explanation_key" not in st.session_state:
        st.session_state.ner_explanation_key = None

    if (
        st.session_state.ner_explanation_key != cache_key
        or "ner_explanation" not in st.session_state
    ):
        with st.spinner("🤖 Analyzing NER behavior..."):
            explanation = explain_ner_result(
                name=name,
                predicted_name=predicted_name,
                error_type=error,
                model_name=model_choice
            )

            st.session_state.ner_explanation = explanation
            st.session_state.ner_explanation_key = cache_key

    st.markdown(st.session_state.ner_explanation)
