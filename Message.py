import Client


# simple class for a instant message
class Message:

    # constructor
    # chatroom_id: what chatroom is this sent to
    # text: the message
    # send_date_time: what day and time was this message sent
    def __init__(self, email_address, chatroom_id, text, sent_date_time):
        self.sender_address = email_address
        self.chatroom_id = chatroom_id
        self.text = text
        self.sent_date_time = sent_date_time
        self.id = -1
    # send the message
    def send(self):
        Client.send_message(self)

    def set_id(self, id):
        self.id = id

    def __str__(self):
        output = ""
        sent_dat_time = self.sent_date_time
        output += sent_dat_time.strftime('%Y-%m-%d %H:%M:%S') + "\n"
        output += self.sender_address + "\n\n"
        output += self.text + "\n\n"
        output += "____________________________________________________________________________________________________"
        return output