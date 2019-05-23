from frutas import Frutas
from frutiadero import Frutiadero

class Jugo:
    nombre = ''
    tamano = ''
    ingredientes = ''
    azucar = 0
    nivel_agua = 0

    def __init__(self, nombre, tamano, ingredientes, azucar, nivel_agua):
        self.nombre = nombre
        self.tamano = tamano
        self.ingredientes = ingredientes
        self.azucar = azucar
        self.nivel_agua = nivel_agua

    def preparar(self, nombre, tamano, ingredientes, azucar, porcentajeagua):

