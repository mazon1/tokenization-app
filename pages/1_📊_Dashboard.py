import streamlit as st
from utils.data_loader import load_data
import seaborn as sns
import matplotlib.pyplot as plt

# MUST be first Streamlit command
st.set_page_config(layout="wide")

# -------------------------------
# 🔹 LOAD DATA
# -------------------------------
df = load_data()

st.title("📊 Dataset Dashboard")

# -------------------------------
# 🔹 SAFE COLUMN DETECTION
# -------------------------------
columns = [col.lower() for col in df.columns]

# Detect Token_Count
if "token_count" not in columns:
    st.error(f"Token_Count column missing. Available columns: {df.columns.tolist()}")
    st.stop()

# Detect Cultural_Group dynamically
group_col = next(
    (col for col in df.columns if col.lower() in [
        "cultural_group", "culture", "group", "region"
    ]),
    None
)

if group_col is None:
    st.error(f"No cultural group column found. Columns: {df.columns.tolist()}")
    st.stop()

# Standardize column name
df.rename(columns={group_col: "Cultural_Group"}, inplace=True)

# Normalize group labels
df["Cultural_Group"] = df["Cultural_Group"].astype(str).str.strip().str.title()

# -------------------------------
# 🔹 KPI SECTION
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
if group_counts.nunique() == 1 and len(group_counts) >= 3:
    st.success("✅ Balanced dataset: 10,000 names per group")
else:
    st.warning("⚠️ Dataset imbalance detected or unexpected labels")

# -------------------------------
# 🔹 SECONDARY METRICS
# -------------------------------
token_col = next(col for col in df.columns if col.lower() == "token_count")

col5, col6, col7 = st.columns(3)

col5.metric("Avg Tokens", round(df[token_col].mean(), 2))
col6.metric("Max Tokens", df[token_col].max())
col7.metric("Std Dev", round(df[token_col].std(), 2))

# -------------------------------
# 🔹 INSIGHT TEXT
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
sns.boxplot(x="Cultural_Group", y=token_col, data=df, ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 VIOLIN PLOT
# -------------------------------
st.subheader("Distribution Shape (Fragmentation Spread)")

fig, ax = plt.subplots()
sns.violinplot(data=df, x=token_col, y="Cultural_Group", ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 AVERAGE TOKEN COUNT
# -------------------------------
avg_tokens = df.groupby("Cultural_Group")[token_col].mean().reset_index()

st.subheader("Average Token Count by Cultural Group")

fig, ax = plt.subplots()
sns.barplot(data=avg_tokens, x="Cultural_Group", y=token_col, ax=ax)
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
