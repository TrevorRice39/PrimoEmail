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
    print(len_email)
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