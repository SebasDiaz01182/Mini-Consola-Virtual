from tkinter import *
import socket

#Conexion con el servidor de space Invader
'''
socketC = socket.socket()
socketC.connect(('localhost','8000'))
socketC.send('Hola desde el cliente') #mandar al servidor lo que se ocupa
respuesta = socketC.recv(1024)
print(respuesta)
'''
class Ventana:
    def __init__(self):
        super().__init__()
        #Creacion de ventana
        ventana = Tk()#creacion  de la ventana
        ventana.geometry('600x300') #tamaño de la ventana
        ventana.title('Control')#titulo de la ventana

        #Funciones de los botones de movimiento


        #Creacion de los botones de las flechas
        botonIzq = Button(ventana,text='<-')
        botonIzq.pack()
        botonIzq.configure()


        ventana.mainloop() #bucle infinito



def main():
    ventana = Ventana()



#Main
main()
