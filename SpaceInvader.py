import socket
import json
from ObjetosSpaceInvader import *
from tkinter import messagebox
from random import * #Libreria para cosas aleatorias
import time

'''
def EnviarPantalla():
'''


socketSI = socket.socket()
socketSI.bind(('localhost',8000))
socketSI.listen(1)

def PosicionJugador(tablero):
    for i in range(50):
        for j in range(50):
            if (isinstance(tablero[i][j],Personaje)):
                return [i,j]
            else:
                pass

def Disparar(xy):
    cont = 21;
    while(cont<=44):
        if isinstance(tablero[xy[0]][cont], Alien):
            tablero[xy[0]][cont]

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
        Disparar()
    '''
    try:
        
        socketX = socket.socket()
        socketX.connect(('localhost',6000))
        datos = {'hostia':1,'auron':2}
        mensajeJSON = json.dumps(datos)
        socketX.send(mensajeJSON.encode()) #mandar al servidor lo que se ocupa
        
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


#Instanciacion del personaje
tablero[43][21] = Personaje()
tablero[43][22] = Personaje()
tablero[42][21] = Personaje()
tablero[43][20] = Personaje()
tablero[41][21] = Personaje()

#Esta al tanto del controlador recibiendo llamadas


def Principal(tablero):
    #Para inicializar todo, hay que enviar el tablero completo
    while True:
        try:
            #Recibe la entrada del controlador
            conexion, direccion = socketSI.accept()
            peticion = conexion.recv(1024).decode() #recibe la entrada que provee el controlador
            print("Respuesta desde el controlador SPACE Invader: ",peticion)
            peticion = json.loads(peticion)
            print(peticion['accion'])
            RealizarMovimiento(peticion,tablero)
        except:
            pass   
        
#Principal        
Principal(tablero)


