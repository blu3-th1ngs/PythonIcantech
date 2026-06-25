import streamlit as st
import pandas as pd
from database import conn

st.title("👤 Users")

users = pd.read_sql(
    """
    SELECT id, username
    FROM users
    """,
    conn
)

st.dataframe(
    users,
    use_container_width=True
)