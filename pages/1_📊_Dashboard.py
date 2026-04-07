import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_raw_data, load_balanced_data

st.set_page_config(layout="wide")

st.title("📊 Dataset Dashboard")

# -------------------------------
# 🔹 DATA SELECTION
# -------------------------------
dataset_option = st.radio(
    "Select Dataset View",
    ["Balanced Dataset (Research)", "Raw Dataset (Original)"]
)

if dataset_option == "Balanced Dataset (Research)":
    df = load_balanced_data()
else:
    df = load_raw_data()

# -------------------------------
# 🔹 HANDLE RAW DATA (ADD TOKEN COUNT)
# -------------------------------
if "Token_Count" not in df.columns:
    import tiktoken
    tokenizer = tiktoken.get_encoding("cl100k_base")

    df["Token_Count"] = df["Name"].apply(
        lambda x: len(tokenizer.encode(str(x)))
    )

# -------------------------------
# 🔹 HANDLE RAW DATA (CREATE GROUP)
# -------------------------------
if "Cultural_Group" not in df.columns:

    def assign_group(country):
        country = str(country).lower()

        if any(x in country for x in ["nigeria", "ghana", "kenya"]):
            return "African"
        elif any(x in country for x in ["india", "china", "japan"]):
            return "Asian"
        elif any(x in country for x in ["usa", "canada", "uk"]):
            return "Western"
        else:
            return "Other"

    df["Cultural_Group"] = df["Country"].apply(assign_group)

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
# 🔹 DATASET LABEL
# -------------------------------
if dataset_option == "Balanced Dataset (Research)":
    st.success("Using balanced dataset (10,000 per group)")
else:
    st.info("Using raw dataset (unbalanced, real-world distribution)")

# -------------------------------
# 🔹 VISUALS
# -------------------------------
st.subheader("Token Distribution by Cultural Group")

fig, ax = plt.subplots()
sns.boxplot(x="Cultural_Group", y="Token_Count", data=df, ax=ax)
st.pyplot(fig)

# -------------------------------
# 🔹 AVERAGE COMPARISON
# -------------------------------
avg_tokens = df.groupby("Cultural_Group")["Token_Count"].mean().reset_index()

st.subheader("Average Token Count")

fig, ax = plt.subplots()
sns.barplot(data=avg_tokens, x="Cultural_Group", y="Token_Count", ax=ax)
st.pyplot(fig)
