
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class Email:

    def __init__(self, sender, to, subject, body, server):
        self.msg = MIMEMultipart()
        self.msg['from'] = sender
        self.msg['to'] = to
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(body, 'plain'))
        self.server = server
        

    def send(self):
        self.server.send_message(self.msg)
        del self.msg

