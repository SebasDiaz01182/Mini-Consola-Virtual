#Este modulo contiene las clases que se van a utilizar en el space invader

#Clases
class Alien:
    def __init__(self):
        vida = 500

    def setVida(self,pvida):
        self.vida = pvida
        
    def getVida(self):
        return self.vida

class Personaje:
    def __init__(self):
        daño = 250
        
    def setdaño(self,pdaño):
        self.daño = pdaño
        
    def getdaño(self):
        return self.daño

class Casilla:
    def __init__(self):
        enemigos = []
        personaje = []
    
    def setEnemigos(self, pEnemigos):
        self.enemigos[0] = pEnemigos
    
    def getEnemigos(self):
        return self.enemigos
    
    def setPersonaje(self, pPersonaje):
        self.personaje[0] = pPersonaje
    
    def getPersonaje(self):
        return self.personaje
