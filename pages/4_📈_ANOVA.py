import streamlit as st
import scipy.stats as stats
import pandas as pd
from utils.data_loader import load_balanced_data

st.set_page_config(layout="wide")

st.title("📈 ANOVA Analysis")

# -------------------------------
# 🔹 LOAD BALANCED DATA
# -------------------------------
df = load_balanced_data()
