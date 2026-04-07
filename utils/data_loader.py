import pandas as pd
import streamlit as st
import tiktoken

@st.cache_data
def load_data():
    df = pd.read_csv("data/final_all_names_code.csv")

    tokenizer = tiktoken.get_encoding("cl100k_base")

    # -------------------------------
    # 🔹 CREATE CULTURAL GROUP (FIX 🔥)
    # -------------------------------
    african_countries = [
        "Nigeria", "Ghana", "Kenya", "South Africa", "Ethiopia"
    ]

    asian_countries = [
        "China", "India", "Japan", "South Korea", "Indonesia"
    ]

    western_countries = [
        "United States", "Canada", "United Kingdom", "France", "Germany"
    ]

    def map_group(country):
        if country in african_countries:
            return "African"
        elif country in asian_countries:
            return "Asian"
        elif country in western_countries:
            return "Western"
        else:
            return "Other"

    df["Cultural_Group"] = df["Country"].apply(map_group)

    # -------------------------------
    # 🔹 FILTER ONLY YOUR 3 GROUPS
    # -------------------------------
    df = df[df["Cultural_Group"] != "Other"]

    # -------------------------------
    # 🔹 COMPUTE TOKEN COUNT
    # -------------------------------
    if "Token_Count" not in df.columns:
        df["Token_Count"] = df["Name"].apply(
            lambda x: len(tokenizer.encode(str(x)))
        )

    return df
