import Client 
class Email:

    def __init__(self, sender, to, subject, body, time_sent):
        self.sender = sender
        self.to = to
        self.subject = subject
        self.body = body
        self.time_sent = time_sent

    def send(self):
        Client.send_email(self)