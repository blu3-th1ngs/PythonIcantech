import streamlit as st
import pandas as pd
from database import conn

st.title("📊 Reports")

df = pd.read_sql(
    "SELECT * FROM vulnerabilities",
    conn
)

severity = st.selectbox(
    "Filter Severity",
    [
        "All",
        "Critical",
        "High",
        "Medium",
        "Low"
    ]
)

if severity != "All":
    df = df[
        df["severity"] == severity
    ]

st.dataframe(
    df,
    use_container_width=True
)

csv = df.to_csv(
    index=False
)

st.download_button(
    "Download CSV",
    csv,
    "report.csv",
    "text/csv"
)