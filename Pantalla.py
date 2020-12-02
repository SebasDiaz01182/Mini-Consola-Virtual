import socket

#Creacion del socket 
socketSI = socket.socket()
socketSI.bind(('localhost',8001))
socketSI.listen(1)

    
