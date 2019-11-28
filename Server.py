#!/usr/bin/python3          
import socket  
import pickle          
import time    
import Email
import dbHelper
db = dbHelper.Connection("127.0.0.1", "root", "", "PrimoEmail", False)

# processes the request based on what the request type is
def process_request(requestType, payload, clientsocket):
   # if the client sends an email payload
   if requestType == "emails":
      insert_email(payload)
   #if the client sends a message payload
   elif requestType == "messages":
      insert_message(payload)
   # if a client wants to get data
   elif requestType == "getEmail":
      send_emails_to_client(payload, clientsocket)
   elif requestType == "getMsgs":
      send_messages_to_client()

# insert email into db
def insert_email(payload):
   print(payload)
   email = pickle.loads(payload)
   print(email.body)
   insert_values= [(email.sender, email.to, email.subject, email.body, email.time_sent)]
   db.insert("emails", "sender, receiver, subject, body, sent_date", insert_values)
# insert message into db
def insert_message(payload):
   message = pickle.loads(payload)
   insert_values = [(message.chatroom_id, message.text, time.strftime('%Y-%m-%d %H:%M:%S'))]
   db.insert("messages", "chatroom_id, message, sent_date", insert_values)
# return data back to client
def send_emails_to_client(payload, clientsocket):
   request = pickle.loads(payload)
   queryBySender, address = request[0], request[1]
   emails = []
   if queryBySender:
      data = db.select("*", "emails", "sender = '{0}'".format(address))
      for entry in data:
         emails.append(Email.Email(entry[1], entry[2], entry[3], entry[4], entry[5]))
   else:
      data = db.select("*", "emails", "receiver = '{0}'".format(address))
      for entry in data:
         emails.append(Email.Email(entry[1], entry[2], entry[3], entry[4], entry[5]))
   pickled_emails = pickle.dumps(emails)
   clientsocket.send(pickled_emails)
   pass

def send_messages_to_client():
   pass

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(20)                                           

while True:
   # establish a dbection
   clientsocket,addr = serversocket.accept()      
   header = clientsocket.recv(23).decode('ascii')
   requestType, size = header.split('|')
   requestType = requestType.replace(' ', '')
   size = int(size)
   message = clientsocket.recv(size)
   process_request(requestType, message, clientsocket)
   clientsocket.close()
