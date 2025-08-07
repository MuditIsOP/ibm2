
import streamlit as st
import sqlite3
import hashlib

def hash_pass(password):
    return hashlib.sha256(password.encode()).hexdigest()

def show_login():
    st.subheader("🔐 Login")
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")
    if st.button("Login"):
        if validate_user(username, hash_pass(password)):
            st.success(f"✅ Welcome back, {username}!")
        else:
            st.error("❌ Invalid credentials")

def show_register():
    st.subheader("📝 Register")
    username = st.text_input("👤 Create Username")
    password = st.text_input("🔑 Create Password", type="password")
    if st.button("Register"):
        register_user(username, hash_pass(password))
        st.success("🎉 Registered successfully!")

def validate_user(username, hashed_pw):
    conn = sqlite3.connect('data/complaints.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_pw))
    return cursor.fetchone()

def register_user(username, hashed_pw):
    conn = sqlite3.connect('data/complaints.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_pw))
    conn.commit()
