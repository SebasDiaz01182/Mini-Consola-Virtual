import socket
import json
from ObjetosSpaceInvader import *
from tkinter import messagebox
from random import * #Libreria para cosas aleatorias

#Creacion del socket servidor
socketSI = socket.socket()
socketSI.bind(('localhost',8000))
socketSI.listen(1)

'''
def EnviarPantalla():
'''


def PosicionJugador(tablero):
    for i in range(50):
        for j in range(50):
            if (isinstance(tablero[i][j],Personaje)):
                return [i,j]
            else:
                pass


def MovIzq(xy):
    if (xy[1]-1)<0:
        print('Movimiento invalido izq')
    else: 
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]-1] = Personaje()

def MovDer(xy):
    if (xy[1]+1)>49:
        print('Movimiento invalido der')
    else: 
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]+1] = Personaje()
    

#Determina cual funcion ejecuta dependiendo del boton presionado
def RealizarMovimiento(peticion,tablero):
    '''
    coord = PosicionJugador(tablero)
    if peticion['accion']=='izquierda':
        MovIzq(coord,peticion)
    elif peticion['accion']=='derecha':
        MovDer(coord,peticion)
    else:
        funcion d
    '''
    try:
        socketX = socket.socket()
        socketX.connect(('localhost',6000))
        datos = {'hostia':1,'auron':2}
        mensajeJSON = json.dumps(datos)
        socketX.send(mensajeJSON.encode()) #mandar al servidor lo que se ocupa
    except:
        pass


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
for i in range(44):
    tablero.append([])
    for j in range(44):
        casilla = Casilla()
        tablero[i].append(casilla)

#Instanciacion de los enemigos

posicion = {1:3, 2:2, 3:4}
for x in range(21):
    for y in range(44): 
        clavePos = randint(1,3)
        if y + clavePos<44:
            tablero[x][y + clavePos] = Alien()
        else:
            pass


#Instanciacion del personaje
tablero[43][21] = Personaje()
tablero[43][22] = Personaje()
tablero[42][21] = Personaje()
tablero[43][20] = Personaje()
tablero[41][21] = Personaje()

   
#Principal        
Principal(tablero)

'''
Por hacer Sebix:
-Funcion que espamee enemigos aleatoriamente en la matriz logica ////Listo
-Funcion que identifique enemigos en la logica y los represente en la grafica ////Listo
-Funcion que haga daño a los aliens
-Revisar el movimiento del jugador
-Instanciar al personaje /////////Listo
'''
def Disparar(xy):
    cont = 21;
    while(cont<=44):
        if isinstance(tablero[xy[0]][cont], Alien):
            tablero[xy[0]][cont]