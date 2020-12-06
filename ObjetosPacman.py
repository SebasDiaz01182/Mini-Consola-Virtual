#Clases que se van a utilizar para el desarrollo de Pacman
#Clases
class fantasma:
    def __init__(self):
        vida = 1
        daño = 1

    def setVida(self,pvida):
        self.vida = pvida
        
    def getVida(self):
        return self.vida

    def setDaño(self, pdaño):
        self.daño = pdaño
    
    def getDaño(self):
        return self.daño
    
class Pacman:
    def __init__(self):
        daño = 1
        vida = 1
        itemsObtenidos = 0
        habilidad = False 
        
    def setdaño(self,pdaño):
        self.daño = pdaño
        
    def getdaño(self):
        return self.daño
    
    def setVida(self,pvida):
        self.vida = pvida
        
    def getVida(self):
        return self.vida
    
    def setObjetos(self, pObjetos):
        self.itemsObtenidos = pObjetos
        
    def getObjetos(self):
        return self.itemsObtenidos
    
    def setHabilidad(self, pHabilidad):
        self.habilidad = pHabilidad
        
    def getHabilidad(self):
        return self.habilidad

class Casilla:
    def __init__(self):
        enemigos = []
        personaje = []
    
    def setEnemigos(self, pEnemigos):
        self.enemigos = pEnemigos
    
    def getEnemigos(self):
        return self.enemigos
    
    def setPersonaje(self, pPersonaje):
        self.personaje[0] = pPersonaje
    
    def getPersonaje(self):
        return self.personaje
    
class Muro:
    def __init__(self):
        movimiento = False
    
    def setMovimiento(self, pMovimiento):
        self.movimiento = pMovimiento
        
    def getMovimiento(self):
        return self.movimiento

class Objeto:
    def __init__(self):
        habilidad = False
    
    def setHabilidad(self, pHabilidad):
        self.habilidad = pHabilidad
        
    def getHabilidad(self):
        return self.habilidad