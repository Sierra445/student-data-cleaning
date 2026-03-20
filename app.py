import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mental Health Dashboard", layout="wide")

st.title("Mental Health Data Dashboard")

# ---------------------------
# Load data
# ---------------------------
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_data.csv")

df = load_data()

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("🔍 Filters")

# Country filter
if "entity" in df.columns:
    countries = df["entity"].unique()
    selected_country = st.sidebar.selectbox("Select Country", countries)
    df = df[df["entity"] == selected_country]

# Year filter (if exists)
if "year" in df.columns:
    years = sorted(df["year"].unique())
    selected_year = st.sidebar.selectbox("Select Year", years)
    df = df[df["year"] == selected_year]

# ---------------------------
# Main view
# ---------------------------
st.subheader("Filtered Data")
st.dataframe(df)

# ---------------------------
# Summary stats
# ---------------------------
st.subheader("Summary Statistics")
st.write(df.describe())

# ---------------------------
# Charts
# ---------------------------
st.subheader("Trend / Visualization")

# Try to find a numeric column automatically
numeric_cols = df.select_dtypes(include="number").columns

if len(numeric_cols) > 0:
    selected_metric = st.selectbox("Select metric", numeric_cols)

    st.line_chart(df[selected_metric])
else:
    st.warning("No numeric columns available for charting.")