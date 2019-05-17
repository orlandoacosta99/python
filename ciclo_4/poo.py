class Casa:

    num_banos = 0
    num_abitaciones = 0


    def __init__(self, direccion):

        self.direccion = direccion

    def __repr__(self):

        return f'Casa ubicada en {self.direccion}'

    def __eq__(self, other):

        return self.num_banos == other.num_banos and self.num_abitaciones == other.num_abitaciones

import math

class Punto:

    def __init__(self, x, y ):

        self.x = x
        self.y = y

    def __repr__(self):

        return f' para x es {self.x} y para y es {self.y}'

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def desplazarX(self, x):
        return Punto(self.x + x, self.y)

    def desplazarY(self, y):
        return Punto(self.x, self.y + y)

    def hallar_pendiente(self, other):
        return (self.y - other.y) / (self.x - other.x)

    def hallar_distancia(self, other):
        return math.sqrt(((self.y - other.y)**2) + ((self.x - other.x)**2))

    def __repr__(self):
        return f'El punto esta {self.x, self.y}'

