#archivo que contiene la informacion de las conexiones
import socket #Libreria de socket
import sys #Libreria para cerrar el programa en caso de error
import json #Libreria para utilizar objetos JSON

class Cliente:
    def __init__(self,puerto):
        self.socketC = socket.socket()
        self.socketC.connect(('localhost',puerto))
        

    def EnviarMensaje(self,mensajeJSON):
        self.socketC.send(mensajeJSON.encode())

    def CerrarConexion(self):
        self.socketC.close()



class Servidor:
    def __init__(self,puerto):
        self.socketS = socket.socket()
        self.socketS.bind(('localhost',puerto))
        self.socketS.listen(1)

    def RecibirPeticiones(self):
        #Recibe la entrada del controlador
        try:
            conexion, direccion = self.socketS.accept()
            peticion = conexion.recv(1024).decode() #recibe la entrada que provee el controlador
            print("Respuesta desde el controlador SPACE Invader: ",peticion)
            peticion = json.loads(peticion)
            return peticion
        except:
            print('excepcion en conexion')
        