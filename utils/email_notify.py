
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"

def send_email(recipient_email, ticket_id, category, severity):
    subject = f"Complaint Ticket #{ticket_id} Created"
    body = f"""
    Dear user,

    Your complaint has been registered successfully.

    🔹 Ticket ID: {ticket_id}
    🔹 Category: {category}
    🔹 Severity: {severity}

    Our team will get back to you shortly.

    Regards,
    Support Team
    """
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")
