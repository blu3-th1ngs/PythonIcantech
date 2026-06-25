import streamlit as st

st.title("⚙️ Settings")

theme = st.selectbox(
    "Theme",
    [
        "Dark",
        "Light"
    ]
)

notifications = st.checkbox(
    "Enable Notifications",
    value=True
)

if st.button("Save"):

    st.success(
        "Settings Saved"
    )