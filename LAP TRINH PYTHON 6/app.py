import streamlit as st
from auth import login, register

st.set_page_config(
    page_title="CyberGuard",
    page_icon="🛡️",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ==================
# LOGIN PAGE
# ==================
if not st.session_state.logged_in:

    choice = st.sidebar.selectbox(
        "Menu",
        ["Login", "Sign Up"]
    )

    if choice == "Login":

        st.title("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user = login(username, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()

            else:
                st.error("Invalid credentials")

    else:

        st.title("📝 Sign Up")

        username = st.text_input("Create Username")
        password = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Register"):

            if register(username, password):
                st.success(
                    "Account created successfully"
                )
            else:
                st.error(
                    "Username already exists"
                )

# ==================
# DASHBOARD
# ==================
else:

    st.sidebar.success(
        f"Logged in as {st.session_state.username}"
    )

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.title("🛡️ CyberGuard Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Critical", 12)

    with col2:
        st.metric("High", 25)

    with col3:
        st.metric("Resolved", 18)

    st.write(
        "Welcome to CyberGuard Vulnerability Management System."
    )