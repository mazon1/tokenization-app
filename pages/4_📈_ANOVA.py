import streamlit as st
from utils.data_loader import load_data
from utils.stats import run_anova

df = load_data()

st.title("📈 ANOVA Analysis")

anova_table, eta = run_anova(df)

st.dataframe(anova_table)
st.metric("Eta Squared", round(eta, 4))