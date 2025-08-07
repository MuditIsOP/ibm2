
import streamlit as st
from utils.auth import show_login, show_register
from utils.ticketing import show_ticket_dashboard, show_ticket_form
from utils.chatbot import show_chatbot
from utils.ui_helpers import render_sidebar, custom_footer
from utils.db import init_db

init_db()
st.set_page_config(page_title="Complaint Management System", layout="wide", page_icon="💻")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stButton>button { background-color: #238636; color: white; border: none; border-radius: 8px; }
    .stTextInput>div>div>input { background-color: #161b22; color: white; }
    footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

page = render_sidebar()

if page == "Login":
    show_login()
elif page == "Register":
    show_register()
elif page == "My Tickets":
    show_ticket_dashboard()
elif page == "Chatbot":
    show_chatbot()
elif page == "Admin":
    show_ticket_form()
elif page == "Feedback":
    st.success("📬 Feedback module coming soon!")

custom_footer()
