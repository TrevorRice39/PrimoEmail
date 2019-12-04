#!/usr/bin/python3          
import socket  # socket programming
import pickle  # turns objects into bytes to be sent to and from a server
import time  # date and time library
import Email  # custom email class
import Message  # custom Message class
import dbHelper  # class to help with db statements
import ChatroomList
import User
# connect to db
db = dbHelper.Connection("127.0.0.1", "root", "", "PrimoEmail", False)

# processes the request based on what the request type is
def process_request(requestType, payload, clientsocket):
    # if the client sends an email payload
    if requestType == "emails":
        insert_email(payload)
    # if the client sends a message payload
    elif requestType == "messages":
        insert_message(payload)
    # if a client wants to get emails
    elif requestType == "getEmail":
        send_emails_to_client(payload, clientsocket)
    # if a client wants to get messages
    elif requestType == "getMsgs":
        send_messages_to_client(payload, clientsocket)
    elif requestType == "getCR":
        send_chatrooms_to_client(payload, clientsocket)
    elif requestType == "makeCR":
        make_chatroom(payload, clientsocket)
    elif requestType == "getID":
        send_client_max_id(clientsocket)

def send_client_max_id(clientsocket):
    id = db.select("max(chatroom_id)", "chatroom", "")
    pickled_id = pickle.dumps(id[0][0])
    clientsocket.sendall(pickled_id)
def make_chatroom(payload, clientsocket):
    # pickle the email into bytes
    id, name, user_address = pickle.loads(payload)

    # prepare the values to be inserted
    insert_values = [(id, name)]

    # calling db.insert() to insert data
    db.insert("chatroom", "chatroom_id, chatroom_name", insert_values)

    # prepare the values to be inserted
    insert_values = [(id, user_address)]

    # calling db.insert() to insert data
    db.insert("email_chatroom", "chatroom_id, address", insert_values)

def get_users_in_chatroom(chatroom_id):
    # list of user's emails
    users = []

    # select all emails where sender = address
    data = db.select("*", "email_chatroom", "chatroom_id = '{0}'".format(chatroom_id))
    # append them to the list
    for entry in data:
        users.append(entry[1])
    return users

def get_chatroom_name(id):
    name = db.select("*", "chatroom", "chatroom_id = '{0}'".format(id))
    return name[0][1]

def send_chatrooms_to_client(payload, clientsocket):
    # load the address from the payload
    address = pickle.loads(payload)

    # list of chatroom ids
    chatroom_ids = []

    # select all emails where sender = address
    data = db.select("*", "email_chatroom", "address = '{0}'".format(address))
    # append them to the list
    for entry in data:
        chatroom_ids.append(entry[0])

    # our chat room list
    chatrooms = ChatroomList.ChatroomList()
    for id in chatroom_ids:
        list_of_users = get_users_in_chatroom(id)

        list_of_users = [User.User(user, "") for user in list_of_users]

        chatrooms.add_chatroom(id, list_of_users, get_chatroom_name(id))
    # pickle the list of users into bytes
    pickled_chatrooms = pickle.dumps(chatrooms)
    # send them back to the client
    clientsocket.sendall(pickled_chatrooms)


# insert email into db
def insert_email(payload):
    # pickle the email into bytes
    email = pickle.loads(payload)

    # prepare the values to be inserted
    insert_values = [(email.sender, email.to, email.subject, email.body, email.time_sent)]

    # calling db.insert() to insert data
    db.insert("emails", "sender, receiver, subject, body, sent_date", insert_values)


# insert message into db
def insert_message(payload):
    # pickle the message into bytes
    message = pickle.loads(payload)

    # prepare the value to be inserted
    insert_values = [(message.sender_address, message.chatroom_id, message.text, time.strftime('%Y-%m-%d %H:%M:%S'))]

    # calling db.insert() to insert data
    db.insert("messages", "sender_address, chatroom_id, message, sent_date", insert_values)


# return emails back to client
# payload consists of two peices of data, a boolean on which column to search for the address (sender or reciever)
def send_emails_to_client(payload, clientsocket):
    # load the request from the payload
    request = pickle.loads(payload)

    # unpack the boolean and address
    queryBySender, address = request[0], request[1]

    # list of emails
    emails = []

    # if we are searching by sender
    if queryBySender:
        # select all emails where sender = address
        data = db.select("*", "emails", "sender = '{0}'".format(address))
        # append them to the list
        for entry in data:
            emails.append(Email.Email(entry[1], entry[2], entry[3], entry[4], entry[5]))
    else:  # if we are searching by the reciever
        data = db.select("*", "emails", "receiver = '{0}' order by sent_date desc".format(address))
        for entry in data:
            email = Email.Email(entry[1], entry[2], entry[3], entry[4], entry[5])
            email.set_id(entry[0])
            emails.append(email)

    # pickle the emails into bytes
    pickled_emails = pickle.dumps(emails)
    # send them back to the client
    clientsocket.send(pickled_emails)


# sending messages back to the client
# payload consists of a chatroom Id and an offset for the query
def send_messages_to_client(payload, clientsocket):
    # load the request from the payload
    request = pickle.loads(payload)

    # unpack the chatroom id and the offset
    chatroom_id, offset = request[0], request[1]

    # list of messages
    messages = []

    # prepare our select statement, where chatroom id = our chatroom id, and offset it by our offset
    data = db.select("*", "messages", "chatroom_id = '{0}'".format(chatroom_id, offset))
    # append all the message objects
    for entry in data:
        message = Message.Message(entry[0], entry[2], entry[3], entry[4])
        message.set_id(entry[1])
        messages.append(message)

    # pickle the messages
    pickled_messages = pickle.dumps(messages)
    # send the messags back to the client
    clientsocket.send(pickled_messages)


# create a socket object
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# host ip
host = socket.gethostname()

# port
port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(20)

while True:
    # found a connection
    clientsocket, addr = serversocket.accept()

    # get the header the client sent (23 bytes exactly)
    # will look like:
    # "dataReq |0000000000size"
    header = clientsocket.recv(23).decode('ascii')
    # unpack the request type and size of message
    requestType, size = header.split('|')
    # make sure there are no spaces (because of formatting)
    requestType = requestType.replace(' ', '')
    # get the size of the requests
    size = int(size)
    # receive the message
    message = clientsocket.recv(size)
    # process the request
    process_request(requestType, message, clientsocket)
    # close the client socket
    clientsocket.close()
