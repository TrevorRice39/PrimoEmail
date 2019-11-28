#!/usr/bin/python3  

import socket


def send_email(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))     
    len_of_message = str(len(message))
    info = "emails  " + '|' + len_of_message.zfill(14)        
    s.sendall(info.encode('ascii'))                             
    s.sendall(message.encode())
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
    s.sendall(message.encode())
    s.close()