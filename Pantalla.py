#Importacion de librerias
from tkinter import * #Interfaz
from tkinter import messagebox #Interfaz
import socket #Libreria de socket
import sys #Libreria para cerrar el programa en caso de error
import json #Libreria para utilizar objetos JSON
import random #Libreria para cosas aleatorias

'''
#Creacion del socket 
socketSI = socket.socket()
socketSI.bind(('localhost',6000))
socketSI.listen(1)
'''

    
class Pantalla:
    def __init__(self):
        super().__init__()
        

        #Creacion de la ventana
        pantalla = Tk()
        pantalla.geometry('1601x1080')
        pantalla.resizable(False,False)
        pantalla.title('Vista')
        matrizPixeles=[]
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
        pantalla.mainloop() # bucle infinito de la interfaz

'''
def RecibirPrincipal():
    #Creacion del socket servidor
    socketP = socket.socket()
    socketP.bind(('localhost',6000))
    socketP.listen(1)
    while True:
        try:
            #Recibe la entrada del controlador
            conexion, direccion = socketP.accept()
            peticion = conexion.recv(1024).decode() #recibe la entrada que provee el controlador
            print("Respuesta desde el cliente: ",peticion)
        except:
            pass
'''

'''
colores{1:"blue",2:"yellow",3:"red"}
clave = randint(1,3)
matrizPixeles=[x][y].config(bg=colores[clave])
'''

#Main
#RecibirPrincipal()
x = Pantalla()
