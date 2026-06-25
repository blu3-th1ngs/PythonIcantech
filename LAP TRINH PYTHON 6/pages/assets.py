import streamlit as st
import pandas as pd
from database import conn

st.title("💻 Assets")

hostname = st.text_input(
    "Hostname"
)

ip = st.text_input(
    "IP Address"
)

os_name = st.selectbox(
    "Operating System",
    [
        "Windows 11",
        "Windows Server",
        "Ubuntu",
        "Kali Linux",
        "Debian"
    ]
)

owner = st.text_input(
    "Owner"
)

if st.button("Add Asset"):

    conn.execute(
        """
        INSERT INTO assets
        (hostname,ip,os,owner)
        VALUES(?,?,?,?)
        """,
        (
            hostname,
            ip,
            os_name,
            owner
        )
    )

    conn.commit()

    st.success("Asset Added")

df = pd.read_sql(
    "SELECT * FROM assets",
    conn
)

st.dataframe(
    df,
    use_container_width=True
)