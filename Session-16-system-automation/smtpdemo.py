import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email="your_email"
    receiver_email="receiver_email"
    password="enter_app_password_generated"
    # go to https://myaccount.google.com/
    # Search for app-password
    # generate one app password and use it as password

    msg= MIMEText(body)
    msg['subject']=subject
    msg['from']=sender_email
    msg['to']=receiver_email

    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls() # encrypt connection
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message send successfully")



send_email("Test Email","Checking My Mail Function")