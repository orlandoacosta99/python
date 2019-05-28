from frutas import Frutas

class Ensalada:
    nombre = ''
    tamano = ''
    ingredientes = ''
    crema = False


    def __init__(self, nombre, tamano, ingredientes, crema ):
        self.nombre = nombre
        self.tamano = tamano
        self.ingredientes = ingredientes


    def alistar(self, nombre, tamano, ingredientes, crema):


    def c_crema(self):
        if self.crema== 'crema':
            self.crema = True
            return self.crema

        raise ValueError('sin crema')

