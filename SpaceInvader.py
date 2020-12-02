import socket
import json
from ObjetosSpaceInvader import *

#Creacion del socket servidor
socketSI = socket.socket()
socketSI.bind(('localhost',8000))
socketSI.listen(1)


def RealizarMovimiento(peticion,tablero):
    decision = {'izquierda':1,'derecha':2,'arriba':3,'abajo':4,'ejecutar':5}
    print(decision[peticion['accion']])

#Esta al tanto del controlador recibiendo llamadas
def Principal(tablero):
    while True:
        try:
            #Recibe la entrada del controlador
            conexion, direccion = socketSI.accept()
            peticion = conexion.recv(1024).decode() #recibe la entrada que provee el controlador
            print("Respuesta desde el cliente: ",peticion)
            peticion = json.loads(peticion)
            print(peticion['accion'])
            RealizarMovimiento(peticion,tablero)
        except:
            pass


#Llamado de funciones
tablero = []
for i in range(50):
    tablero.append([])
    for j in range(50):
        casilla = Casilla()
        tablero[i].append(casilla)

#Instanciacion de los enemigos
contx = 0
conty = 0
for x in tablero:
    contx+=1
    for y in x:
        if (conty%4)==0 and (contx%2)==0:
            enemigo = Alien()
            y.setEnemigos(enemigo)
        elif (conty%7)==0:
            enemigo = Alien()
            y.setEnemigos(enemigo)
        else:
            pass
        
#Principal        
Principal(tablero)

