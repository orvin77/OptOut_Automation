from email.message import EmailMessage
import ssl
import smtplib
import re

email_sender = 'desbungie123@gmail.com'
email_password = 'wjsh dxqg nqmy qcjs'
recipient = 'oxa220025@utdallas.edu'

def send_email(user, recipient, link): 
    
    subject = 'Testing email'
    body = """
        This is a test for email sending
    """

    em = EmailMessage()
    em['From'] = user['Email']
    em['To'] = recipient
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(user['Email'], user['Password'])
        smtp.sendmail(email_sender, recipient, em.as_string())
        

# def use_regex(input_text):
#     pattern = re.compile(r"[A-Za-z0-9]+@[A-Za-z]+\.com", re.IGNORECASE)
#     return pattern.match(input_text)

# print(use_regex(email_sender))