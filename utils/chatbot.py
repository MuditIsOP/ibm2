
import streamlit as st

def show_chatbot():
    st.subheader("🤖 AI Chatbot")
    user_input = st.text_input("Ask your question...")
    if st.button("Ask"):
        st.info("🧠 Gemini is typing...")
        st.success("Here's a sample response! (Replace with Gemini output)")
