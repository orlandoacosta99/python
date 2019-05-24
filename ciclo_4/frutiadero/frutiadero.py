from ensalada import Ensalada

from jugo import Jugo

from frutas import Frutas

class Frutiadero:
    tipo = ''
    ingredientes = ''

    def __init__(self, tipo, ingredientes):

        self.tipo = tipo
        self.ingredientes = ingredientes

    def preparar(self, tipo, ingredientes):

        if tipo == 'ensalada':
            return Ensalada.alistar(ingredientes)

        elif tipo == 'jugo':
            return Jugo.preparar(ingredientes)

        else:
            return ValueError('No hay este tipo de preparacion')
