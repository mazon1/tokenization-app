import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.formula.api import ols

from utils.data_loader import load_balanced_data

st.set_page_config(layout="wide")

st.title("📈 ANOVA Analysis")

# -------------------------------
# 🔹 LOAD BALANCED DATA
# -------------------------------
df = load_balanced_data()

# -------------------------------
# 🔹 SAFETY CHECK
# -------------------------------
required_cols = ["Cultural_Group", "Token_Count"]

missing = [col for col in required_cols if col not in df.columns]

if missing:
    st.error(f"Missing columns: {missing}")
    st.write("Columns found:", df.columns.tolist())
    st.stop()

# -------------------------------
# 🔹 KPI SECTION
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Samples", len(df))
col2.metric("Groups", df["Cultural_Group"].nunique())
col3.metric("Avg Tokens", round(df["Token_Count"].mean(), 2))

# -------------------------------
# 🔹 ANOVA MODEL
# -------------------------------
model = ols('Token_Count ~ C(Cultural_Group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# -------------------------------
# 🔹 EFFECT SIZE (ETA SQUARED)
# -------------------------------
eta_squared = (
    anova_table.loc["C(Cultural_Group)", "sum_sq"] /
    anova_table["sum_sq"].sum()
)

# -------------------------------
# 🔹 DISPLAY RESULTS
# -------------------------------
st.subheader("📊 ANOVA Table")
st.dataframe(anova_table)

# Metrics
col4, col5 = st.columns(2)

p_value = anova_table["PR(>F)"]["C(Cultural_Group)"]
f_stat = anova_table["F"]["C(Cultural_Group)"]

col4.metric("F-statistic", round(f_stat, 3))
col5.metric("p-value", f"{p_value:.5f}")

# Effect size
st.metric("Effect Size (η²)", round(eta_squared, 4))

# -------------------------------
# 🔹 INTERPRETATION
# -------------------------------
st.subheader("🧠 Interpretation")

alpha = 0.05

if p_value < alpha:
    st.success("Statistically significant differences detected between cultural groups.")
else:
    st.info("No statistically significant difference detected.")

st.markdown(f"""
- **p-value = {p_value:.5f}**
- **Effect size (η²) = {eta_squared:.4f}**

Even small effect sizes can have large real-world implications when scaled across large systems.
""")

# -------------------------------
# 🔹 VISUALIZATION
# -------------------------------
st.subheader("📊 Token Distribution by Cultural Group")

fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(data=df, x="Cultural_Group", y="Token_Count", ax=ax)
ax.set_title("Token Count Distribution")
st.pyplot(fig)

# -------------------------------
# 🔹 GROUP MEANS
# -------------------------------
st.subheader("📊 Mean Token Count by Group")

means = df.groupby("Cultural_Group")["Token_Count"].mean().reset_index()

fig, ax = plt.subplots()
sns.barplot(data=means, x="Cultural_Group", y="Token_Count", ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 FOOTER
# -------------------------------
st.markdown("---")
st.markdown("© 2026 | **Uchenna Mgbaja** | LIGS")
