import Client 
# simple class for a instant message
class Message:

    # constructor
    # chatroom_id: what chatroom is this sent to
    # text: the message
    # send_date_time: what day and time was this message sent
    def __init__(self, chatroom_id, text, sent_date_time):
        self.chatroom_id = chatroom_id
        self.text = text
        self.sent_date_time = sent_date_time
        
    # send the message
    def send(self):
        Client.send_message(self)