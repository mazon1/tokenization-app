import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    df = pd.read_csv("data/final_all_names_code.csv")
    return df