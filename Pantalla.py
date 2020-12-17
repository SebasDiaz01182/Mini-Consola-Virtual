#Importacion de librerias
from tkinter import * #Interfaz
from tkinter import messagebox #Interfaz
import socket #Libreria de socket
import sys #Libreria para cerrar el programa en caso de error
import json #Libreria para utilizar objetos JSON
from random import *
import threading
import time
from Conexiones import *
from PIL import ImageTk, Image
from ObjetosPacman import *
from ObjetosSpaceInvader import *




matrizPixeles = []#Matriz de pixeles de toda la pantalla
class Pantalla:
    def __init__(self,tipo):
        super().__init__()
        #Creacion de la ventana
        pantalla = Tk()
        pantalla.geometry('1601x1080')
        pantalla.resizable(False,False)
        pantalla.title('Vista')
        for i in range(44):
            matrizPixeles.append([])
            for j in range(44):
                matrizPixeles[i].append(None)

        for r in range(44):
            for c in range(44):
                pixel = Label(pantalla,text="",bg="black")
                pixel.config(width=4,height=0)
                pixel.grid(row=r,column=c,padx=1,pady=1)
                matrizPixeles[r][c] = pixel

        if tipo=='pacman':
            #horizontales
            for i in range(2,8):
                matrizPixeles[2][i].config(bg='navy')

            for i in range(5,8):
                matrizPixeles[6][i].config(bg='navy')

            for i in range(2,5):
                matrizPixeles[12][i].config(bg='navy')
            #verticales
            for x in range(2,13):
                matrizPixeles[x][2].config(bg='navy')

            for x in range(2,7):
                matrizPixeles[x][7].config(bg='navy')

            for x in range(7,13):
                matrizPixeles[x][5].config(bg='navy')   

            #l izquierda abajo
            for x in range(31,42):
                matrizPixeles[x][2].config(bg='navy')

            for x in range(31,37):
                matrizPixeles[x][5].config(bg='navy')

            for x in range(38,42):
                matrizPixeles[x][7].config(bg='navy')

            for i in range(2,5):
                matrizPixeles[31][i].config(bg='navy')

            for i in range(2,8):
                matrizPixeles[41][i].config(bg='navy')

            for i in range(5,8):
                matrizPixeles[37][i].config(bg='navy')


            #l arriba a la derecha
            for x in range(2,7):
                matrizPixeles[x][36].config(bg='navy')

            for x in range(2,13):
                matrizPixeles[x][41].config(bg='navy')

            for x in range(7,13):
                matrizPixeles[x][38].config(bg='navy')

            for i in range(36,42):
                matrizPixeles[2][i].config(bg='navy')

            for i in range(36,39):
                matrizPixeles[6][i].config(bg='navy')

            for i in range(38,42):
                matrizPixeles[12][i].config(bg='navy')    

            #l abajo de la derecha 
            for x in range(31,42):
                matrizPixeles[x][41].config(bg='navy')

            for x in range(31,37):
                matrizPixeles[x][38].config(bg='navy')

            for x in range(38,42):
                matrizPixeles[x][36].config(bg='navy')

            for i in range(38,42):
                matrizPixeles[31][i].config(bg='navy')

            for i in range(36,42):
                matrizPixeles[41][i].config(bg='navy')

            for i in range(36,39):
                matrizPixeles[37][i].config(bg='navy')


            #cuadros
            for i in range(13,18):
                for j in range(8,12):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(26,31):
                for j in range(8,12):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(13,18):
                for j in range(32,36):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(26,31):
                for j in range(32,36):
                    matrizPixeles[i][j].config(bg='navy')

            # rectangulos
            for i in range(0,9):
                for j in range(11, 13):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(35,44):
                for j in range(11, 13):
                    matrizPixeles[i][j].config(bg='navy')
                    
            for i in range(0,9):
                for j in range(31, 33):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(35,44):
                for j in range(31, 33):
                    matrizPixeles[i][j].config(bg='navy')

            #rectangulos horizontales
            for i in range(7,9):
                for j in range(15, 29):
                    matrizPixeles[i][j].config(bg='navy')

            for i in range(35,37):
                for j in range(15, 29):
                    matrizPixeles[i][j].config(bg='navy')

            #centro del tablero
            for i in range(15,20):
                matrizPixeles[12][i].config(bg='navy')
                
            for i in range(24,28):
                matrizPixeles[12][i].config(bg='navy')

            for i in range(15, 28):
                    matrizPixeles[30][i].config(bg='navy')

            for x in range(12,31):
                matrizPixeles[x][15].config(bg='navy')
                
            for x in range(12,31):
                matrizPixeles[x][28].config(bg='navy')
                
            for i in range(19,23):
                for j in range(20,24):
                    matrizPixeles[i][j].config(bg='navy')
                    
            #Objetos 

            matrizPixeles[9][12].config(bg = 'red2')
            matrizPixeles[22][1].config(bg = 'red2')
            matrizPixeles[34][7].config(bg = 'red2')
            matrizPixeles[40][14].config(bg = 'red2')
            matrizPixeles[23][17].config(bg = 'red2')
            matrizPixeles[23][26].config(bg = 'red2')
            matrizPixeles[22][33].config(bg = 'red2')
            matrizPixeles[3][28].config(bg = 'red2')
            matrizPixeles[7][35].config(bg = 'red2')
            matrizPixeles[38][43].config(bg = 'red2')
            matrizPixeles[34][35].config(bg = 'red2')
            #personaje
            matrizPixeles[43][9].config(bg='gold')
        else:
            matrizPixeles[43][21].config(bg="red")
            matrizPixeles[43][22].config(bg="red")
            matrizPixeles[42][21].config(bg="red")
            matrizPixeles[43][20].config(bg="red")
            matrizPixeles[41][21].config(bg="gray")


            colores = {1:"lightgreen", 2:"yellow",3:"lightblue",4:"orange",5:"purple",6:"pink",7:"blue",8:"sea green",9:"gold",10:"saddle brown",11:"cyan",12:"darkOrchid4"}
            x = 0 
            y = 0
            cont = 0

            while x <=18:
                if y+4 < 44:
                    colorRandom = randint(1,10)
                    matrizPixeles[x][y+4].config(bg = colores[colorRandom])
                    cont+=1
                    y+=4
                elif cont%2==0:
                    x+=3
                    y=0
                else:
                    cont+=1
                    y+=1

        #Cambiar color de enemigos
        pantalla.mainloop()


def MoverIzquierda(x, y):
    matrizPixeles[x][y].config( bg = "black")
    matrizPixeles[x][y-1].config(bg = "grey")
    
    matrizPixeles[x+1][y].config( bg = "black")
    matrizPixeles[x+1][y-1].config(bg = "red")

    matrizPixeles[x+2][y-1].config(bg = "red")
    
    matrizPixeles[x+2][y+1].config( bg = "black")
    matrizPixeles[x+2][y-1].config(bg = "red")

    matrizPixeles[x+2][y-2].config(bg = "red")
    
def MoverDerecha(x, y):
    matrizPixeles[x][y].config( bg = "black")
    matrizPixeles[x][y+1].config(bg = "grey")
    
    matrizPixeles[x+1][y].config( bg = "black")
    matrizPixeles[x+1][y+1].config(bg = "red")

    matrizPixeles[x+2][y+1].config(bg = "red")

    matrizPixeles[x+2][y+1+1].config(bg = "red")

    matrizPixeles[x+2][y-1].config(bg = "black")
    
    
def Disparar(x,y):
    e = 40
    while e!=x:
        matrizPixeles[e][y].config(bg="yellow")
        time.sleep(0.1)
        matrizPixeles[e][y].config(bg="black")
        e-=1 
    matrizPixeles[x][y].config(bg="black")


def PMoverIzquierda(x,y):
    print(x,',',y)
    matrizPixeles[x][y].config(bg='black')
    matrizPixeles[x][y-1].config(bg='gold')
def PMoverDerecha(x,y):
    print(x,',',y)
    matrizPixeles[x][y].config(bg='black')
    matrizPixeles[x][y+1].config(bg='gold')
def PMoverArriba(x,y):
    print(x,',',y)
    matrizPixeles[x][y].config(bg='black')
    matrizPixeles[x-1][y].config(bg='gold')

def PMoverAbajo(x,y):
    print(x,',',y)
    matrizPixeles[x][y].config(bg='black')
    matrizPixeles[x+1][y].config(bg='gold')


def DeterminarHacer(peticion):
    
    if peticion['juego']=='s':
        if peticion['accion']=='izquierda':
            MoverIzquierda(peticion['x'],peticion['y'])
        elif peticion['accion']=='derecha':
            MoverDerecha(peticion['x'],peticion['y'])
        else:
            Disparar(peticion['x'],peticion['y'])

    elif peticion['juego']=='p':
        if peticion['accion']=='izquierda':
            PMoverIzquierda(peticion['x'],peticion['y'])
        elif peticion['accion']=='derecha':
            PMoverDerecha(peticion['x'],peticion['y'])
        elif peticion['accion']=='arriba':
            PMoverArriba(peticion['x'],peticion['y'])
        elif peticion['accion']=='abajo':
            PMoverAbajo(peticion['x'],peticion['y'])
        else:
            pass

    else:
       pass
        


def AtenderConsola():
    servidor = Servidor(6000)
    while True:
        peticion=servidor.RecibirPeticiones()
        hilo5 = threading.Thread(target=DeterminarHacer(peticion))
        hilo5.start()

    
def RecibirPrincipal():
    #Creacion del socket
    
    hilo = threading.Thread(target=AtenderConsola)
    hilo.start()
    pantalla = Pantalla('pacman')
        

#Main
RecibirPrincipal()




'''
#figura de las L's
if tipo=='pacman':
#arriba a la izquierda

#horizontales
for i in range(2,8):
    matrizPixeles[2][i].config(bg='navy')

for i in range(5,8):
    matrizPixeles[6][i].config(bg='navy')

for i in range(2,5):
    matrizPixeles[12][i].config(bg='navy')
#verticales
for x in range(2,13):
    matrizPixeles[x][2].config(bg='navy')

for x in range(2,7):
    matrizPixeles[x][7].config(bg='navy')

for x in range(7,13):
    matrizPixeles[x][5].config(bg='navy')   

#l izquierda abajo
for x in range(31,42):
    matrizPixeles[x][2].config(bg='navy')

for x in range(31,37):
    matrizPixeles[x][5].config(bg='navy')

for x in range(38,42):
    matrizPixeles[x][7].config(bg='navy')

for i in range(2,5):
    matrizPixeles[31][i].config(bg='navy')

for i in range(2,8):
    matrizPixeles[41][i].config(bg='navy')

for i in range(5,8):
    matrizPixeles[37][i].config(bg='navy')


#l arriba a la derecha
for x in range(2,7):
    matrizPixeles[x][36].config(bg='navy')

for x in range(2,13):
    matrizPixeles[x][41].config(bg='navy')

for x in range(7,13):
    matrizPixeles[x][38].config(bg='navy')

for i in range(36,42):
    matrizPixeles[2][i].config(bg='navy')

for i in range(36,39):
    matrizPixeles[6][i].config(bg='navy')

for i in range(38,42):
    matrizPixeles[12][i].config(bg='navy')    

#l abajo de la derecha 
for x in range(31,42):
    matrizPixeles[x][41].config(bg='navy')

for x in range(31,37):
    matrizPixeles[x][38].config(bg='navy')

for x in range(38,42):
    matrizPixeles[x][36].config(bg='navy')

for i in range(38,42):
    matrizPixeles[31][i].config(bg='navy')

for i in range(36,42):
    matrizPixeles[41][i].config(bg='navy')

for i in range(36,39):
    matrizPixeles[37][i].config(bg='navy')


#cuadros
for i in range(13,18):
    for j in range(8,12):
        matrizPixeles[i][j].config(bg='navy')

for i in range(26,31):
    for j in range(8,12):
        matrizPixeles[i][j].config(bg='navy')

for i in range(13,18):
    for j in range(32,36):
        matrizPixeles[i][j].config(bg='navy')

for i in range(26,31):
    for j in range(32,36):
        matrizPixeles[i][j].config(bg='navy')

# rectangulos
for i in range(0,9):
    for j in range(11, 13):
        matrizPixeles[i][j].config(bg='navy')

for i in range(35,44):
    for j in range(11, 13):
        matrizPixeles[i][j].config(bg='navy')
        
for i in range(0,9):
    for j in range(31, 33):
        matrizPixeles[i][j].config(bg='navy')

for i in range(35,44):
    for j in range(31, 33):
        matrizPixeles[i][j].config(bg='navy')

#rectangulos horizontales
for i in range(7,9):
    for j in range(15, 29):
        matrizPixeles[i][j].config(bg='navy')

for i in range(35,37):
    for j in range(15, 29):
        matrizPixeles[i][j].config(bg='navy')

#centro del tablero
for i in range(15,20):
    matrizPixeles[12][i].config(bg='navy')
    
for i in range(24,28):
    matrizPixeles[12][i].config(bg='navy')

for i in range(15, 28):
        matrizPixeles[30][i].config(bg='navy')

for x in range(12,31):
    matrizPixeles[x][15].config(bg='navy')
    
for x in range(12,31):
    matrizPixeles[x][28].config(bg='navy')
    
for i in range(19,23):
    for j in range(20,24):
        matrizPixeles[i][j].config(bg='navy')
        
#Objetos 

matrizPixeles[9][12].config(bg = 'red2')
matrizPixeles[22][1].config(bg = 'red2')
matrizPixeles[34][7].config(bg = 'red2')
matrizPixeles[40][14].config(bg = 'red2')
matrizPixeles[23][17].config(bg = 'red2')
matrizPixeles[23][26].config(bg = 'red2')
matrizPixeles[22][33].config(bg = 'red2')
matrizPixeles[3][28].config(bg = 'red2')
matrizPixeles[7][35].config(bg = 'red2')
matrizPixeles[38][43].config(bg = 'red2')
matrizPixeles[34][35].config(bg = 'red2')

#Fantasma

matrizPixeles[27][21].config(bg = 'seagreen1')
matrizPixeles[32][21].config(bg = 'seagreen1')
matrizPixeles[15][21].config(bg = 'seagreen1')
matrizPixeles[40][21].config(bg = 'seagreen1')
matrizPixeles[3][21].config(bg = 'seagreen1')
matrizPixeles[10][21].config(bg = 'seagreen1')
matrizPixeles[23][8].config(bg = 'seagreen1')
matrizPixeles[23][39].config(bg = 'seagreen1')

#personaje
matrizPixeles[43][9].config(bg='gold')

else:
matrizPixeles[43][21].config(bg="red")
matrizPixeles[43][22].config(bg="red")
matrizPixeles[42][21].config(bg="red")
matrizPixeles[43][20].config(bg="red")
matrizPixeles[41][21].config(bg="gray")


colores = {1:"lightgreen", 2:"yellow",3:"lightblue",4:"orange",5:"purple",6:"pink",7:"blue",8:"sea green",9:"gold",10:"saddle brown",11:"cyan",12:"darkOrchid4"}
x = 0 
y = 0
cont = 0

while x <=18:
    if y+4 < 44:
        colorRandom = randint(1,10)
        matrizPixeles[x][y+4].config(bg = colores[colorRandom])
        cont+=1
        y+=4
    elif cont%2==0:
        x+=3
        y=0
    else:
        cont+=1
        y+=1

'''