#!/usr/bin/python3  

import socket


def send_message(type, message_text):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))     
    len_of_message = str(len(message_text))
    if type != "emails" and type != "messages":
        type = "blank"
    elif type == "emails":
        type += "  "
    info = type + '|' + len_of_message.zfill(14)        
    s.sendall(info.encode('ascii'))    
    msg = message_text                           
    s.sendall(msg.encode())
    s.close()