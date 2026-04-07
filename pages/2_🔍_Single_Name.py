import streamlit as st
import tiktoken
from utils.chatbot import explain_name_analysis

# Page config
st.set_page_config(layout="wide")

st.title("🔍 Single Name Analysis")

# -------------------------------
# 🔹 INPUT
# -------------------------------
name = st.text_input("Enter a name", "Chimaobi")

# Initialize tokenizer
tokenizer = tiktoken.get_encoding("cl100k_base")

if name:

    # -------------------------------
    # 🔹 TOKENIZATION
    # -------------------------------
    tokens = tokenizer.encode(name)
    token_count = len(tokens)

    tokenized_output = " | ".join(
        [tokenizer.decode([t]) for t in tokens]
    )

    # -------------------------------
    # 🔹 TGDI
    # -------------------------------
    tgdi = round(token_count / len(name), 3) if len(name) > 0 else 0

    # -------------------------------
    # 🔹 COST (example rate)
    # -------------------------------
    cost_per_token = 0.00003
    cost = round(token_count * cost_per_token, 6)

    # -------------------------------
    # 🔹 METRICS
    # -------------------------------
    col1, col2, col3 = st.columns(3)

    col1.metric("Token Count", token_count)
    col2.metric("TGDI", tgdi)
    col3.metric("Cost", f"${cost}")

    # -------------------------------
    # 🔹 TOKEN BREAKDOWN
    # -------------------------------
    st.subheader("Token Breakdown")
    st.write(tokenized_output)

    # -------------------------------
    # 🔹 AUTO AI EXPLANATION 🔥
    # -------------------------------
    st.subheader("🤖 AI Interpretation")
    st.caption("AI-generated interpretation based on tokenization patterns")

    cache_key = f"{name}_{token_count}_{tgdi}_{cost}"

    if "last_explanation_key" not in st.session_state:
        st.session_state.last_explanation_key = None

    if (
        st.session_state.last_explanation_key != cache_key
        or "explanation" not in st.session_state
    ):
        with st.spinner("🤖 Interpreting results..."):
            explanation = explain_name_analysis(
                name=name,
                token_count=token_count,
                tgdi=tgdi,
                cost=cost,
                tokens=tokenized_output
            )

            st.session_state.explanation = explanation
            st.session_state.last_explanation_key = cache_key

    st.markdown(st.session_state.explanation)
