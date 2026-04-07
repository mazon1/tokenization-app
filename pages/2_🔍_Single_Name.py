import streamlit as st
from utils.tokenizer import tokenize_name, compute_tgdi, estimate_cost

st.title("🔍 Single Name Analysis")

name = st.text_input("Enter a name")

if name:
    tokens, token_strings = tokenize_name(name)

    tgdi = compute_tgdi(name, tokens)
    cost = estimate_cost(tokens)

    col1, col2, col3 = st.columns(3)

    col1.metric("Token Count", len(tokens))
    col2.metric("TGDI", round(tgdi, 3))
    col3.metric("Cost", f"${cost:.6f}")

    st.subheader("Token Breakdown")
    st.markdown(" | ".join(token_strings))