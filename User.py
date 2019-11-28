import smtplib, socket

class User:
    email_address = None
    name = None
    contact_list = None
    received_emails = None
    sent_emails = None
    spam_folder = None
    server = None


    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password

    def start_server(self):
        self.server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        self.server.starttls()
        if len(self.email_address) == 0 or len(self.password) == 0:
            return False
        try:
            self.server.login(self.email_address, self.password)
        except smtplib.SMTPException:
            return False
        return True
