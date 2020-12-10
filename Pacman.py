#Consola numero 2
#Juego pacman
#Importacion de librerias
from ObjetosPacman import *   #clases
import socket
import json
from tkinter import messagebox
from random import * #Libreria para cosas aleatorias
import time
from Conexiones import *

#Creación del socket servidor

def EnviarPantalla(mensajeJSON):
    conexion = Cliente(6000)
    conexion.EnviarMensaje(mensajeJSON)
    
def PosicionJugador(tablero):
    for i in range(0,44):
        for j in range(0,44):
            if isinstance(tablero[i][j],Pacman):
                return [i,j]
            else:
                pass

def MoverDerecha(xy):
    if ((xy[1]+1)>43) or (isinstance(tablero[xy[0]][xy[1]+1], Muro)):
        print('Movimiento invalido derecha')
    else:     
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]+1] = Pacman()
        datos={'juego':'p','accion':'derecha','x':xy[0],'y':xy[1]}   
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)    
            
def MoverIzquierda(xy):
    if ((xy[1]-1)<0) or (isinstance(tablero[xy[0]][xy[1]-1], Muro)):
        print('Movimiento invalido izquierda')
    else:
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]][xy[1]-1] = Pacman()
        datos={'juego':'p','accion':'izquierda','x':xy[0],'y':xy[1]}   
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)
        
def MoverArriba(xy):
    if ((xy[0]-1)<0) or (isinstance(tablero[xy[0]-1][xy[1]], Muro)):
        print('Movimiento invalido arriba')
    else:
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]-1][xy[1]] = Pacman()
        datos={'juego':'p','accion':'arriba','x':xy[0],'y':xy[1]}   
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)
        
def MoverAbajo(xy):
    if ((xy[0]+1)<0) or (isinstance(tablero[xy[0]+1][xy[1]], Muro)):
        print('Movimiento invalido abajo')
    else:
        tablero[xy[0]][xy[1]] = Casilla()
        tablero[xy[0]+1][xy[1]] = Pacman()
        datos={'juego':'p','accion':'abajo','x':xy[0],'y':xy[1]}   
        mensajeJSON = json.dumps(datos)
        EnviarPantalla(mensajeJSON)

    
    
#Determina cual funcion ejecuta dependiendo del boton presionado
def RealizarMovimiento(peticion,tablero):
    
    coord = PosicionJugador(tablero)
    if peticion['accion']=='izquierda':
        MoverIzquierda(coord)
    elif peticion['accion']=='derecha':
        MoverDerecha(coord)
    elif peticion['accion'] == 'arriba':
        MoverArriba(coord)
    elif peticion['accion'] == 'ejecutar':
        pass
    else:
        MoverAbajo(coord)
  
#Instanciar la pantalla del juego pacman
#Tablero de juego
tablero = []
tablero = []
for i in range(44):
    tablero.append([])
    for j in range(44):
        casilla = Casilla()
        tablero[i].append(Casilla)

#Muros
for i in range(2,8):
    tablero[2][i] = Muro()

for i in range(5,8):
    tablero[6][i] = Muro()

for i in range(2,5):
    tablero[12][i] = Muro()
#verticales
for x in range(2,13):
    tablero[x][2] = Muro()

for x in range(2,7):
    tablero[x][7] = Muro()

for x in range(7,13):
    tablero[x][5] = Muro()   

#l izquierda abajo
for x in range(31,42):
    tablero[x][2] = Muro()

for x in range(31,37):
    tablero[x][5] = Muro()

for x in range(38,42):
    tablero[x][7] = Muro()

for i in range(2,5):
    tablero[31][i] = Muro()

for i in range(2,8):
    tablero[41][i] = Muro()

for i in range(5,8):
    tablero[37][i] = Muro()


#l arriba a la derecha
for x in range(2,7):
    tablero[x][36] = Muro()

for x in range(2,13):
    tablero[x][41] = Muro()

for x in range(7,13):
    tablero[x][38] = Muro()

for i in range(36,42):
    tablero[2][i] = Muro()

for i in range(36,39):
    tablero[6][i] = Muro()

for i in range(38,42):
    tablero[12][i] = Muro()    

#l abajo de la derecha 
for x in range(31,42):
    tablero[x][41] = Muro()

for x in range(31,37):
    tablero[x][38] = Muro()

for x in range(38,42):
    tablero[x][36] = Muro()

for i in range(38,42):
    tablero[31][i] = Muro()

for i in range(36,42):
    tablero[41][i] = Muro()

for i in range(36,39):
    tablero[37][i] = Muro()


#cuadros
for i in range(13,18):
    for j in range(8,12):
        tablero[i][j] = Muro()

for i in range(26,31):
    for j in range(8,12):
        tablero[i][j] = Muro()

for i in range(13,18):
    for j in range(32,36):
        tablero[i][j] = Muro()

for i in range(26,31):
    for j in range(32,36):
        tablero[i][j] = Muro()

# rectangulos
for i in range(0,9):
    for j in range(11, 13):
        tablero[i][j] = Muro()

for i in range(35,44):
    for j in range(11, 13):
        tablero[i][j] = Muro()
        
for i in range(0,9):
    for j in range(31, 33):
        tablero[i][j] = Muro()

for i in range(35,44):
    for j in range(31, 33):
        tablero[i][j] = Muro()

#rectangulos horizontales
for i in range(7,9):
    for j in range(15, 29):
        tablero[i][j] = Muro()

for i in range(35,37):
    for j in range(15, 29):
        tablero[i][j] = Muro()

#centro del tablero
for i in range(15,20):
    tablero[12][i] = Muro()
    
for i in range(24,28):
    tablero[12][i] = Muro()

for i in range(15, 28):
        tablero[30][i] = Muro()

for x in range(12,31):
    tablero[x][15] = Muro()
    
for x in range(12,31):
    tablero[x][28] = Muro()
    
for i in range(19,23):
    for j in range(20,24):
        tablero[i][j] = Muro()

#Objetos 

tablero[9][12] = Objeto()
tablero[22][1] = Objeto()
tablero[34][7] = Objeto()
tablero[40][14] = Objeto()
tablero[23][17] = Objeto()
tablero[23][26] = Objeto()
tablero[22][33] = Objeto()
tablero[3][28] = Objeto()
tablero[7][35] = Objeto()
tablero[38][43] = Objeto()
tablero[34][35] = Objeto()
#Personaje
tablero[43][9] = Pacman()

def Principal(tablero):
    servidor = Servidor(8000)
    while True:
        peticion = servidor.RecibirPeticiones()
        RealizarMovimiento(peticion,tablero)
        
#Principal        
Principal(tablero)
