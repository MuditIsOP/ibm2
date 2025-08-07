
import streamlit as st
import uuid
import sqlite3
from utils.email_notify import send_email

def show_ticket_form():
    st.subheader("📋 Raise a Complaint")
    category = st.selectbox("📂 Category", ["Technical", "Account", "Service"])
    severity = st.radio("🚨 Severity", ["Low", "Medium", "High", "Critical"], horizontal=True)
    description = st.text_area("📝 Describe your issue")
    user_email = st.text_input("📧 Your Email")

    if st.button("Submit Ticket"):
        ticket_id = str(uuid.uuid4())[:8]
        assign_agent = "agent_" + category.lower()
        conn = sqlite3.connect("data/complaints.db")
        conn.execute("INSERT INTO tickets VALUES (?, ?, ?, ?, ?, ?, ?)", 
                     (ticket_id, "test_user", category, severity, "Open", assign_agent, user_email))
        conn.commit()
        send_email(user_email, ticket_id, category, severity)
        st.toast(f"🎫 Ticket #{ticket_id} created and assigned to {assign_agent}!", icon="🎉")
        st.success(f"Confirmation email sent to {user_email} 📬")

def show_ticket_dashboard():
    st.subheader("🎟️ My Tickets")
    conn = sqlite3.connect("data/complaints.db")
    rows = conn.execute("SELECT * FROM tickets").fetchall()
    for r in rows:
        with st.expander(f"Ticket #{r[0]} – {r[2]} – {r[3]} – {r[4]}"):
            st.write(f"👤 User: {r[1]}")
            st.write(f"🧑‍💼 Agent: {r[5]}")
            st.write(f"📧 Email: {r[6]}")
