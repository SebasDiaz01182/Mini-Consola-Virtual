#Importacion de librerias
from tkinter import * #Interfaz
from tkinter import messagebox #Interfaz
import socket #Libreria de socket
import sys #Libreria para cerrar el programa en caso de error
import json #Libreria para utilizar objetos JSON
from random import *
import threading
import time






matrizPixeles = []#Matriz de pixeles de toda la pantalla


class Pantalla:
    def __init__(self):
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
                if (c%2==0):
                    pixel = Label(pantalla,text="",bg="black")
                    pixel.config(width=4,height=0)
                    pixel.grid(row=r,column=c,padx=1,pady=1)
                    matrizPixeles[r][c] = pixel
                else:
                    pixel = Label(pantalla,text="",bg="black")
                    pixel.config(width=4,height=0)
                    pixel.grid(row=r,column=c,padx=1,pady=1)
                    matrizPixeles[r][c] = pixel
                    
        matrizPixeles[43][21].config(bg="red")
        matrizPixeles[43][22].config(bg="red")
        matrizPixeles[42][21].config(bg="red")
        matrizPixeles[43][20].config(bg="red")
        matrizPixeles[41][21].config(bg="grey")
        
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

def DeterminarHacer(peticion):
    
    if peticion['accion']=='izquierda':
        #llama a cambiar izquierda
    elif peticion['accion']=='derecha':
        #llama a cambiar izquierda
    else:
        #disparar



def AtenderConsola():
    socketP = socket.socket()
    socketP.bind(('localhost',6000))
    socketP.listen(1)
    while True:
        print('hostia')
        try:
            #Recibe la entrada del controlador
            conexion, direccion = socketP.accept()
            peticion = conexion.recv(1024).decode() #recibe la entrada que provee el controlador
            peticion = json.loads(peticion)
            DeterminarHacer(peticion)            
        except:
            pass


def RecibirPrincipal():
    #Creacion del socket
    hilo = threading.Thread(target=AtenderConsola)
    hilo.start()
    pantalla = Pantalla()
    


#Main
RecibirPrincipal()
