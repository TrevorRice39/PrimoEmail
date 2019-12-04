

class ChatroomList:

    class Chatroom:

        def __init__(self, chatroom_id, list_of_users, name):
            self.name = name
            self.list_of_users = list_of_users
            self.chatroom_id = chatroom_id;
            # self.care = macmiller;

    def __init__(self):
        self.chatrooms = dict()

    def add_chatroom(self, chatroom_id, list_of_users, name):
        chatroom = self.Chatroom(chatroom_id, list_of_users, name)
        self.chatrooms[chatroom.chatroom_id] = chatroom

    def get_list_of_users(self, chatroom_id):
        return self.chatrooms[chatroom_id].list_of_users

    def get_chatroom(self, id):
        return self.chatrooms[id]

    def get_all_ids(self):
        return [*self.chatrooms]

    def get_users(self, id):
        return self.chatrooms[id].list_of_users