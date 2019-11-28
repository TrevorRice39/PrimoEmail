
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Client 
class Email:

    def __init__(self, sender, to, subject, body):
        self.sender = sender
        self.to = to
        self.subject = subject
        self.body = body
        

    def send(self):
        Client.send_email(self)