import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

def send_verification_email(to_email: str, code: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your DocSync Verification Code"
    msg["From"] = os.getenv("EMAIL_FROM")
    msg["To"] = to_email

    html = f"""
    <html>
      <body>
        <p>Your DocSync verification code is: <b>{code}</b></p>
      </body>
    </html>
    """
    msg.attach(MIMEText(html, "html"))

    server = smtplib.SMTP(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")))
    server.starttls()
    server.login(os.getenv("EMAIL_FROM"), os.getenv("EMAIL_PASSWORD"))
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()
