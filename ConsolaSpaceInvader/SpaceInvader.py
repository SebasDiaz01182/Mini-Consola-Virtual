import socket

#Creacion del socket 
socketSI = socket.socket()
socketSI.bind(('localhost',8000))
socketSI.listen(5)

while True:
    conexion, direccion = socketSI.accept()
    print('Conexion establecida satisfactoriamente')
    print('Direccion: ',direccion)
    peticion = conexion.recv(1024) #recibir
    conexion.send('Hola, te slaudo desde el servidor')
    conexion.close()



