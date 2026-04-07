import streamlit as st
from utils.data_loader import load_data
import seaborn as sns
import matplotlib.pyplot as plt

df = load_data()

st.title("📊 Dataset Dashboard")

# Scorecards
col1, col2, col3 = st.columns(3)

col1.metric("Total Names", len(df))
col2.metric("Avg Tokens", round(df["Token_Count"].mean(), 2))
col3.metric("Max Tokens", df["Token_Count"].max())

# Boxplot
st.subheader("Token Distribution by Cultural Group")

fig, ax = plt.subplots()
sns.boxplot(x="Cultural_Group", y="Token_Count", data=df, ax=ax)
st.pyplot(fig)

# Violin
st.subheader("Distribution Shape")

fig, ax = plt.subplots()
sns.violinplot(data=df, x="Token_Count", y="Cultural_Group", ax=ax)
st.pyplot(fig)