import streamlit as st

st.set_page_config(layout="wide")

# Sidebar Branding
st.sidebar.image("assets/ligs_logo.png", width=150)
st.sidebar.title("🧠 Tokenization Audit")

st.sidebar.markdown("Navigate using the pages above 👆")

st.title("🧠 Tokenization Bias Audit Platform")

st.markdown("""
This platform analyzes how AI systems process names, revealing bias, fragmentation,
and downstream impact on cost and performance.
""")

st.markdown("---")
st.markdown("© 2026 | Created by **Uchenna Mgbaja**")