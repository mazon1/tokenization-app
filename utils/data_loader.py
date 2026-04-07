import pandas as pd
import streamlit as st
import tiktoken

@st.cache_data
def load_data():
    df = pd.read_csv("data/final_all_names_code.csv")

    tokenizer = tiktoken.get_encoding("cl100k_base")

    # Detect correct name column
    name_col = "Name" if "Name" in df.columns else "name"

    # Compute Token_Count if missing
    if "Token_Count" not in df.columns:
        df["Token_Count"] = df[name_col].apply(
            lambda x: len(tokenizer.encode(str(x)))
        )

    return df
