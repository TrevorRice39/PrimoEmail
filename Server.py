#!/usr/bin/python3          
import socket               
import dbHelper
conn = dbHelper.Connection("127.0.0.1", "root", "", "PrimoEmail", False)

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
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   print("Got a connection from %s" % str(addr))
   header = clientsocket.recv(23).decode('ascii')
   
   messageType, size = header.split('|')
   messageType = messageType.replace(' ', '')
   print("type=", messageType, "|")
   
   if messageType != "blank":
      size = int(size)
      message = clientsocket.recv(size)
      conn.insert(messageType, "message", [message])
   clientsocket.close()