import smtplib
import ssl
from email.message import EmailMessage

##let's send an email from python

# what we need for an email
# To
# From
# Subject 
# Body

recipient_email = input("who would you like to send an email to? ")
sender_email = input("enter your email address ")
subject = input("What is the subject of your email? ")
body = input("What would you like to say? ")
#we need a password, so we will generate one from Google
password = input("enter your app password ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject

message.set_content(body)
context = ssl.create_default_context()

server =  smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) 
print("Sending email")
server.login(sender_email, password)
server.sendmail(sender_email, recipient_email, message.as_string())
print("success")