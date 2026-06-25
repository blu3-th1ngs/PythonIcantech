import streamlit as st
import pandas as pd
import plotly.express as px
from database import conn

st.title("🏠 Dashboard")

vulns = pd.read_sql(
    "SELECT * FROM vulnerabilities",
    conn
)

if vulns.empty:
    st.warning("No vulnerabilities found.")
    st.stop()

critical = len(vulns[vulns["severity"] == "Critical"])
high = len(vulns[vulns["severity"] == "High"])
medium = len(vulns[vulns["severity"] == "Medium"])
resolved = len(vulns[vulns["status"] == "Fixed"])

c1, c2, c3, c4 = st.columns(4)

c1.metric("Critical", critical)
c2.metric("High", high)
c3.metric("Medium", medium)
c4.metric("Resolved", resolved)

st.subheader("Severity Distribution")

fig = px.bar(
    vulns.groupby("severity").size().reset_index(name="count"),
    x="severity",
    y="count"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Recent Vulnerabilities")

st.dataframe(
    vulns.tail(10),
    use_container_width=True
)