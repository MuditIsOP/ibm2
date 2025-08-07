
import streamlit as st

def render_sidebar():
    st.sidebar.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=40)
    st.sidebar.title("🧾 Complaint System")
    options = ["Login", "Register", "My Tickets", "Chatbot", "Admin", "Feedback"]
    return st.sidebar.radio("🚪 Navigate", options)

def custom_footer():
    st.markdown("""
    <hr style="border: 1px solid #30363d; margin-top: 2rem;">
    <div style='text-align: center; color: #8b949e;'>
        <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="20">
        Built with ❤️ by <strong>Mudit Sharma</strong>
    </div>
    """, unsafe_allow_html=True)
