import Client 
class Message:

    def __init__(self, chatroom_id, text):
        self.chatroom_id = chatroom_id
        self.text = text
        

    def send(self):
        Client.send_message(self)