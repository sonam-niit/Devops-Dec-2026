import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email(subject,body):
    sender_email="your_email"
    receiver_email="receiver_email"
    password="enter_app_password_generated"

    msg= MIMEMultipart()
    msg['subject']=subject
    msg['from']=sender_email
    msg['to']=receiver_email

    # add message
    msg.attach(MIMEText("<h1>"+body+"</h1>",'html')) # formatted text message in HTML
    filename="app.log" # my attachment file
    with open(filename,"rb") as attachment: # read in binary mode
        mime_base=MIMEBase("application","octet-stream") # creating container for binary data
        mime_base.set_payload(attachment.read())# reading file and add in MIME Object

    # Encode file in ASCII for Email
    # email we can't send in raw binary format for that converted into Base64 encoded string
    encoders.encode_base64(mime_base)
    mime_base.add_header('content-disposition',f"attachment",filename='bank-statement.log')
    # use app.log file as ban-statement.log and take it as attachment
    msg.attach(mime_base)
    with smtplib.SMTP("smtp.gmail.com",587) as server:
        server.starttls() # encrypt connection
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message send successfully")



send_email("Test Email","Checking My Mail Function")