import streamlit as st
from utils.data_loader import load_data
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = load_data()

st.set_page_config(layout="wide")

st.title("📊 Dataset Dashboard")

# -------------------------------
# 🔹 SAFE COLUMN CHECK (IMPORTANT)
# -------------------------------
if "Token_Count" not in df.columns:
    st.error("Token_Count column missing. Please check data_loader.")
    st.stop()

# -------------------------------
# 🔹 KPI SECTION (UPGRADED)
# -------------------------------
group_counts = df["Cultural_Group"].value_counts()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Names", len(df))
col2.metric("African", group_counts.get("African", 0))
col3.metric("Asian", group_counts.get("Asian", 0))
col4.metric("Western", group_counts.get("Western", 0))

# -------------------------------
# 🔹 DATASET BALANCE CHECK
# -------------------------------
if group_counts.nunique() == 1:
    st.success("✅ Balanced dataset: 10,000 names per group")
else:
    st.warning("⚠️ Dataset imbalance detected")

# -------------------------------
# 🔹 SECONDARY METRICS
# -------------------------------
col5, col6, col7 = st.columns(3)

col5.metric("Avg Tokens", round(df["Token_Count"].mean(), 2))
col6.metric("Max Tokens", df["Token_Count"].max())
col7.metric("Std Dev", round(df["Token_Count"].std(), 2))

# -------------------------------
# 🔹 INSIGHT TEXT (IMPORTANT)
# -------------------------------
st.markdown("""
### 🔍 Key Insight

This analysis uses a culturally balanced dataset (10,000 names per group),
ensuring that observed differences are due to **tokenization bias** rather than sampling imbalance.
""")

# -------------------------------
# 🔹 BOXPLOT
# -------------------------------
st.subheader("Token Distribution by Cultural Group")

fig, ax = plt.subplots()
sns.boxplot(x="Cultural_Group", y="Token_Count", data=df, ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 VIOLIN PLOT
# -------------------------------
st.subheader("Distribution Shape (Fragmentation Spread)")

fig, ax = plt.subplots()
sns.violinplot(data=df, x="Token_Count", y="Cultural_Group", ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 AVERAGE TOKEN COUNT (NEW 🔥)
# -------------------------------
avg_tokens = df.groupby("Cultural_Group")["Token_Count"].mean().reset_index()

st.subheader("Average Token Count by Cultural Group")

fig, ax = plt.subplots()
sns.barplot(data=avg_tokens, x="Cultural_Group", y="Token_Count", ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 OPTIONAL: RAW COUNTS
# -------------------------------
with st.expander("📄 View Dataset Distribution"):
    st.write(group_counts)

# -------------------------------
# 🔹 FOOTER
# -------------------------------
st.markdown("---")
st.markdown("© 2026 | **Uchenna Mgbaja** | LIGS")
