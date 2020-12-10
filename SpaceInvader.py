import socket
import json
from ObjetosSpaceInvader import *
from tkinter import messagebox
from random import * #Libreria para cosas aleatorias
import time
from Conexiones import *

def EnviarPantalla(mensajeJSON):
    conexion = Cliente(6000)
    conexion.EnviarMensaje(mensajeJSON)


def PosicionJugador(tablero):
    for i in range(44):
        if isinstance(tablero[41][i],Personaje):
            return [41,i]
        else:
            pass


def Disparar(xy):
    i = 41
    while(i>=0):
        if isinstance(tablero[i][xy[1]],Alien):
            tablero[i][xy[1]] = Casilla()
            datos = {'juego':'s','accion':'disparo','x':i,'y':xy[1]}
            mensajeJSON = json.dumps(datos)
            EnviarPantalla(mensajeJSON)
            break
        else:
            i-=1


def MovIzq(xy):
    if (xy[1]-2)<0:
        print('Movimiento invalido izq')
    else:
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]-1] = Personaje()
        
        tablero[xy[0]+1][xy[1]] = Casilla()
        tablero[xy[0]+1][xy[1]-1] = Personaje()

        tablero[xy[0]+2][xy[1]] = Casilla()
        tablero[xy[0]+2][xy[1]-1] = Personaje()

        tablero[xy[0]+2][xy[1]+1] = Casilla()
        tablero[xy[0]+2][xy[1]-1] = Personaje()

        tablero[xy[0]+2][xy[1]-1] = Casilla()
        tablero[xy[0]+2][xy[1]-2] = Personaje()

        datos = {'juego':'s','accion':'izquierda','x':xy[0],'y':xy[1]}
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)


def MovDer(xy):
    if (xy[1]+2)>44:
        print('Movimiento invalido der')
    else: 
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]+1] = Personaje()
        
        tablero[xy[0]+1][xy[1]] = Casilla()
        tablero[xy[0]+1][xy[1]+1] = Personaje()

        tablero[xy[0]+2][xy[1]] = Casilla()
        tablero[xy[0]+2][xy[1]+1] = Personaje()

        tablero[xy[0]+2][xy[1]+1] = Casilla()
        tablero[xy[0]+2][xy[1]+1+1] = Personaje()

        tablero[xy[0]+2][xy[1]-1] = Casilla()
        tablero[xy[0]+2][xy[1]] = Personaje()

        datos = {'juego':'s','accion':'derecha','x':xy[0],'y':xy[1]}
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)
    

#Determina cual funcion ejecuta dependiendo del boton presionado
def RealizarMovimiento(peticion,tablero):
    
    coord = PosicionJugador(tablero)
    if peticion['accion']=='izquierda':
        MovIzq(coord)
    elif peticion['accion']=='derecha':
        MovDer(coord)
    elif peticion['accion']=='ejecutar':
        Disparar(coord)
    else:
        pass
    


#Inicializar la matriz logica
tablero = []
for i in range(44):
    tablero.append([])
    for j in range(44):
        casilla = Casilla()
        tablero[i].append(casilla)

#Instanciacion de los enemigos
x = 0
y=0
cont=0
while x <=18:
    if y+4 < 44:
        tablero[x][y+4] = Alien()
        cont+=1
        y+=4
    elif cont%2==0:
        x+=3
        y=0
    else:
        cont+=1
        y+=1

#Instanciacion del personaje
tablero[43][21] = Personaje()
tablero[43][22] = Personaje()
tablero[42][21] = Personaje()
tablero[43][20] = Personaje()
tablero[41][21] = Personaje()

#Esta al tanto del controlador recibiendo llamadas


def Principal(tablero):
    servidor = Servidor(8000)
    while True:
        peticion = servidor.RecibirPeticiones()
        RealizarMovimiento(peticion,tablero)  

#Principal        
Principal(tablero)



    
