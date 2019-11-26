#!/usr/bin/python3           # This is client.py file

import socket


def send_message(type, message_text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))     
    len_of_message = str(len(message_text))
    if type == "chat":
        type += '*'
    elif type != "email":
        return
    info = type + '|' + len_of_message.zfill(14)        
    s.sendall(info.encode())    
    msg = message_text                           
    s.sendall(msg.encode())

    # Receive no more than 1024 bytes
    msg = s.recv(1024)         
    s.close()
    print (msg.decode('ascii'))
send_message("emfail", "here is my email")
send_message("chat", "here is my message")