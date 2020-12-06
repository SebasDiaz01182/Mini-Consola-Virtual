#Consola numero 2
#Juego pacman
#Importacion de librerias
from ObjetosPacman import *   #clases
import socket
import json
from tkinter import messagebox
from random import * #Libreria para cosas aleatorias
import time

#Creación del socket servidor

def EnviarPantalla(mensajeJSON):
    try:
        socketX = socket.socket()
        socketX.connect(("Direccion del servidor"))
        socketX.send(mensajeJSON.encode()) #mandar al servidor lo que se ocupa
        socketX.close()
    except:
        pass
    
def PosicionJugador(tablero):
    for i in range(44):
        if isinstance(tablero[41][i],Pacman):
            return [41,i]
        else:
            pass

def MoverDerecha(xy):
    if ((xy[1]+2)<0) or (isinstance(xy[1]+2, Muro)):
        print('Movimiento invalido derecha')
        
    elif (isinstance(tablero[xy[0]][xy[1]+2]), Objeto):
        tablero[xy[0]][xy[1]].setObjetos(tablero[xy[0]][xy[1]].getObjetos()+1)
        if(tablero[xy[0]][xy[1]+2]).getHabilidad() :
            #Pacman modo matanza
            tablero[xy[0]][xy[1]].setHabilidad(True) 
            
    if (isinstance(tablero[xy[0]][xy[1]+2], fantasma)) and (tablero[xy[0]][xy[1]].getHabilidad()):
            #Matar fantasma
            tablero[xy[0]][xy[1]+2] = Casilla()      
            
    tablero[xy[0]][xy[1]] = Casilla()
    tablero[xy[0]][xy[1]+1] = Pacman()   
            
            
def MoverIzquierda(xy):
    if ((xy[1]-2)<0) or (isinstance(tablero[xy[0]][xy[1]-2], Muro)):
        print('Movimiento invalido izquierda')
    elif (isinstance(tablero[xy[0]][xy[1]-2]), Objeto):
        tablero[xy[0]][xy[1]].setObjetos(tablero[xy[0]][xy[1]].getObjetos()+1)
        if(tablero[xy[0]][xy[1]-2]).getHabilidad == True :
            #Pacman modo matanza
        
def MoverArriba(xy):
    if ((xy[0]-2)<0) or (isinstance(tablero[xy[0]-2][xy[1]], Muro)):
        print('Movimiento invalido arriba')
    elif (isinstance(tablero[xy[0]-2][xy[1]]), Objeto):
        xy[1].setObjetos(tablero[xy[0]][xy[1]].getObjetos()+1)
        if(xy[0]-2).getHabilidad == True :
            #Pacman modo matanza
        
def MoverAbajo(xy):
    if ((xy[0]+2)<0) or (isinstance(tablero[xy[0]+2][xy[1]], Muro)):
        print('Movimiento invalido abajo')
    elif (isinstance(tablero[xy[0]+2][xy[1]]), Objeto):
        xy[1].setObjetos()+1
        if(xy[0]+2).getHabilidad == True :
            #Pacman modo matanza

    
#Determina cual funcion ejecuta dependiendo del boton presionado
def RealizarMovimiento(peticion,tablero):
    
    coord = PosicionJugador(tablero)
    if peticion['accion']=='izquierda':
        MoverIzquierda(coord)
    elif peticion['accion']=='derecha':
        MoverDerecha(coord)
    elif peticion['accion'] == 'arriba':
        MoverArriba(coord)
    else:
        MoverAbajo(coord)
  
#Instanciar la pantalla del juego pacman
#Tablero de juego
tablero = []
#Jugador

#Enemigos

#Objetos
  
#Esta al tanto del controlador recibiendo llamadas

def Principal(tablero):
    #Para inicializar todo, hay que enviar el tablero completo
    while True:
        try:
            #Recibe la entrada del controlador
        except:
            pass   
        
#Principal        
Principal(tablero)