import smtplib
import os
from email.message import EmailMessage
def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(
    os.getenv("MAIL_EMAIL"),
    os.getenv("MAIL_PASSWORD")
)
    msg=EmailMessage()
    msg['FrOM']='msai05072005@gmail.com' 
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()
    