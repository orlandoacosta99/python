from frutas import Frutas

class Jugo:
    nombre = ''
    tamano = 0
    ingredientes = ''
    azucar = False
    nivel_agua = 0

    def __init__(self, nombre, tamano, ingredientes, azucar, nivel_agua):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.azucar = azucar
        self.nivel_agua = nivel_agua

    def preparar(self, nombre, tamano, ingredientes, azucar, porcentajeagua):


    def c_azucar(self):
            if self.azucar == 'azucar':
                self.crema = True
                return self.crema
            raise ValueError('sin azucar')



