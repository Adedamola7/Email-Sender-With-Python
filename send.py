from email.message import EmailMessage
import ssl
import smtplib


email_sender = 'adekeyedamola72@gmail.com'
email_password = 'jwnotsctzsaxgeli'
email_receiver = 'adekeyedamola72@gmail.com'
subject = 'This is a test email'
body = """
My name is Adedamola. I am software developer in Adroit Solutions Ltd. 
"""


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em['']
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())