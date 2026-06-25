import streamlit as st
import pandas as pd
from database import conn

st.title("🐞 Vulnerabilities")

tab1, tab2 = st.tabs(
    ["Add", "Manage"]
)

with tab1:

    title = st.text_input("Title")

    severity = st.selectbox(
        "Severity",
        [
            "Critical",
            "High",
            "Medium",
            "Low"
        ]
    )

    status = st.selectbox(
        "Status",
        [
            "Open",
            "In Progress",
            "Fixed"
        ]
    )

    description = st.text_area(
        "Description"
    )

    if st.button("Add Vulnerability"):

        conn.execute(
            """
            INSERT INTO vulnerabilities
            (title,severity,status,description)
            VALUES(?,?,?,?)
            """,
            (
                title,
                severity,
                status,
                description
            )
        )

        conn.commit()

        st.success("Added")

with tab2:

    df = pd.read_sql(
        "SELECT * FROM vulnerabilities",
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    delete_id = st.number_input(
        "Delete ID",
        min_value=1
    )

    if st.button("Delete"):

        conn.execute(
            "DELETE FROM vulnerabilities WHERE id=?",
            (delete_id,)
        )

        conn.commit()

        st.success("Deleted")