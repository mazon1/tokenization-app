import pandas as pd
import streamlit as st
import tiktoken

# Initialize tokenizer once
tokenizer = tiktoken.get_encoding("cl100k_base")


# -------------------------------
# 🔹 RAW DATA
# -------------------------------
@st.cache_data
def load_raw_data():
    df = pd.read_csv("data/final_all_names_code.csv")

    # -------------------------------
    # 🔹 CREATE CULTURAL GROUP (IMPROVED 🔥)
    # -------------------------------
    def map_group(country):
        country = str(country).lower()

        if any(x in country for x in [
            "nigeria", "ghana", "kenya", "ethiopia", "south africa"
        ]):
            return "African"

        elif any(x in country for x in [
            "china", "india", "japan", "korea", "indonesia"
        ]):
            return "Asian"

        elif any(x in country for x in [
            "united states", "usa", "canada", "uk",
            "united kingdom", "france", "germany"
        ]):
            return "Western"

        else:
            return "Other"

    df["Cultural_Group"] = df["Country"].apply(map_group)

    # -------------------------------
    # 🔹 COMPUTE TOKEN COUNT
    # -------------------------------
    if "Token_Count" not in df.columns:
        df["Token_Count"] = df["Name"].apply(
            lambda x: len(tokenizer.encode(str(x)))
        )

    return df


# -------------------------------
# 🔹 BALANCED DATA
# -------------------------------
@st.cache_data
def load_balanced_data():
    df = pd.read_csv("data/final_balanced_dataset.csv")

    return df
