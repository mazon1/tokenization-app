import pandas as pd
import streamlit as st
import tiktoken

@st.cache_data
def load_data():
    df = pd.read_csv("data/final_all_names_code.csv")

    tokenizer = tiktoken.get_encoding("cl100k_base")

    # -------------------------------
    # 🔹 DEBUG (IMPORTANT)
    # -------------------------------
    st.write("Columns found:", df.columns.tolist())

    # -------------------------------
    # 🔹 DETECT NAME COLUMN
    # -------------------------------
    name_col = next(
        (col for col in df.columns if col.lower() in ["name"]),
        None
    )

    if name_col is None:
        st.error("No name column found")
        st.stop()

    # -------------------------------
    # 🔹 DETECT CULTURAL GROUP COLUMN
    # -------------------------------
    group_col = next(
        (col for col in df.columns if col.lower() in [
            "cultural_group", "culture", "group", "region"
        ]),
        None
    )

    if group_col is None:
        st.error(f"No cultural group column found. Columns: {df.columns.tolist()}")
        st.stop()

    # Rename to standard name
    df.rename(columns={group_col: "Cultural_Group"}, inplace=True)

    # -------------------------------
    # 🔹 COMPUTE TOKEN COUNT
    # -------------------------------
    if "Token_Count" not in df.columns:
        df["Token_Count"] = df[name_col].apply(
            lambda x: len(tokenizer.encode(str(x)))
        )

    return df
