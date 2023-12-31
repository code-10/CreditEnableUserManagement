from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..celery_config import celery

@celery.task
def send_confirmation_email():
    print("entered send confirmation email")
    email_user = 'nereji6806@gmx.us'
    email_password = 'nereji6806@usoplay.com'

    sender_email = email_user
    receiver_email = "manoj.code10@gmail.com"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "None"

    body = "message"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmx.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)

        print(f"Email sent to manoj.code10@gmail.com with subject: subject")

    except Exception as e:
        print(f"Failed to send email: {str(e)}")
