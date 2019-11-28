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

    # connection to hostname on the port.
    s.connect((host, port))     
    len_of_message = str(len(message))
    info = "messages" + '|' + len_of_message.zfill(14)        
    s.sendall(info.encode('ascii'))                         
    s.send(message)
    s.close()