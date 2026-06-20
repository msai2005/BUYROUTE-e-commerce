import smtplib
from email.message import EmailMessage

def send_mail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('msai05072005@gmail.com','qkqc dyjb ixsl egid')
    msg=EmailMessage()
    msg['FrOM']='msai05072005@gmail.com' 
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()