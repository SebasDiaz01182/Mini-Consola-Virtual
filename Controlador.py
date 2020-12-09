#Importacion de librerias
from tkinter import * #Interfaz
from tkinter import messagebox #Interfaz
import socket #Libreria de socket
import sys #Libreria para cerrar el programa en caso de error
import json #Libreria para utilizar objetos JSON
from Conexiones import *

#CONEXION CON EL SOCKET
#Conexion con el servidor de space Invader
#Funcion que envia el JSON correspondiente a la entrada del usuario
def EnviarEntrada(mensajeJSON):
    conexion = Cliente(8000)
    conexion.EnviarMensaje(mensajeJSON)

#Funciones de los botones de movimiento
def Accion():
    peticion = {'accion':'ejecutar'}
    mensajeJSON = json.dumps(peticion)
    EnviarEntrada(mensajeJSON)

def BotonIzquierda():
    #Funciones que realizan cada boton de la interfaz
    peticion = {'accion':'izquierda'}
    mensajeJSON = json.dumps(peticion)
    EnviarEntrada(mensajeJSON)

def BotonDerecha():
    #Funciones que realizan cada boton de la interfaz
    peticion = {'accion':'derecha'}
    mensajeJSON = json.dumps(peticion)
    EnviarEntrada(mensajeJSON)

def BotonArriba():
    #Funciones que realizan cada boton de la interfaz
    peticion = {'accion':'arriba'}
    mensajeJSON = json.dumps(peticion)
    EnviarEntrada(mensajeJSON)

def BotonAbajo():
    #Funciones que realizan cada boton de la interfaz
    peticion = {'accion':'abajo'}
    mensajeJSON = json.dumps(peticion)
    EnviarEntrada(mensajeJSON)
     
class Ventana:
    def __init__(self):
        super().__init__()
        #Creacion de ventana
        ventana = Tk() #creacion  de la ventana
        ventana.geometry('600x300') #tamaño de la ventana
        ventana.title('Control')#titulo de la ventana

        #Creacion de los botones de las flechas

        #Direccionales
        botonIzq = Button(ventana,text='<-',command = BotonIzquierda)
        botonIzq.pack()
        botonIzq.place(x=50,y=125,width=55,height=40)

        botonDer = Button(ventana,text='->',command=BotonDerecha)
        botonDer.pack()
        botonDer.place(x=200,y=125,width=55,height=40)

        botonAr = Button(ventana,text='Arriba',command=BotonArriba)
        botonAr.pack()
        botonAr.place(x=130,y=60,width=55,height=50)

        botonAb = Button(ventana,text='Abajo',command=BotonAbajo)
        botonAb.pack()
        botonAb.place(x=130,y=175,width=55,height=50)

        #Boton de Accion
        botonAccion = Button(ventana,text='X',command=Accion)
        botonAccion.pack()
        botonAccion.place(x=400,y=125,width=55,height=40)

        ventana.mainloop() #bucle infinito

def main():
   interfaz = Ventana()


#Main
main()