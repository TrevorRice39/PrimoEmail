#!/usr/bin/python3  

import socket
import pickle


host = socket.gethostname()                           
port = 9999
header_max_length = 8 # length of longest header
message_max_size = 14 # 10^14 bytes possible

# creates a meta data header to request/send info from/to server
def create_header(request_type, info):
    len_info = str(len(info))
    header = request_type.ljust(header_max_length) + '|' + len_info.zfill(message_max_size)
    return header

def new_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.connect((host, port))  
    return s

def send_email(email):
    s = new_socket(host, port)
    message = email.body
    pickled_email = pickle.dumps(email)
    header = create_header("emails", pickled_email)
    s.sendall(header.encode('ascii'))                             
    s.sendall(pickled_email)
    s.close()

def send_message(message):
    s = new_socket(host, port)
    pickled_message = pickle.dumps(message)
    header = create_header("messages", pickled_message)
    s.sendall(header.encode('ascii'))                         
    s.sendall(pickled_message)
    s.close()

def request_emails(bySender, address):
    s = new_socket(host, port) 
    request = [bySender, address]
    pickled_request = pickle.dumps(request)
    header = create_header("getEmail", pickled_request)    
    s.sendall(header.encode('ascii'))                         
    s.sendall(pickled_request)
    received_data = b""
    data = s.recv(5000)
    while len(data) != 0:
        received_data += data
        data = s.recv(5000)
    print(received_data)
    emails = pickle.loads(received_data)
    print(emails)
    for email in emails:
        print(email.sender, email.to, email.subject, email.body, email.time_sent)
    s.close()

def request_messages(chatroomId, index):
    pass
