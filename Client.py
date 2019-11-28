#!/usr/bin/python3  

import socket
import pickle

def send_email(email):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999

    message = email.body
    pickled_email = pickle.dumps(email)
    len_email = str(len(pickled_email))
    # connection to hostname on the port.
    s.connect((host, port))     
    info = "emails  " + '|' + len_email.zfill(14)        
    s.sendall(info.encode('ascii'))                             
    s.sendall(pickled_email)
    s.close()

def send_message(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999
    pickled_message = pickle.dumps(message)
    len_message = str(len(pickled_message))
    # connection to hostname on the port.
    s.connect((host, port))     
    info = "messages" + '|' + len_message.zfill(14)        
    s.sendall(info.encode('ascii'))                         
    s.sendall(pickled_message)
    s.close()

def request_emails(bySender, address):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999
    request = [bySender, address]
    pickled_request = pickle.dumps(request)
    len_request = str(len(pickled_request))
    # connection to hostname on the port.
    s.connect((host, port))     
    info = "getEmail" + '|' + len_request.zfill(14)        
    s.sendall(info.encode('ascii'))                         
    s.sendall(pickled_request)
    received_data = s.recv(20000)
    emails = pickle.loads(received_data)
    print(emails)
    for email in emails:
        print(email.sender, email.to, email.subject, email.body, email.time_sent)
    s.close()
    pass

def request_messages(chatroomId, index):
    pass
