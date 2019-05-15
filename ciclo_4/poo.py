class Casa:

    num_banos = 0
    num_abitaciones = 0


    def __init__(self, direccion):

        self.direccion = direccion

    def __repr__(self):

        return f'Casa ubicada en {self.direccion}'

    def __eq__(self, other):

        return self.num_banos == other.num_banos and self.num_abitaciones == other.num_abitaciones



class Punto:

    def __init__(self, x, y ):

        self.x = x
        self.y = y

    def __repr__(self):

        return f' para x es {self.x} y para y es {self.y}'

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y

    def desplazar_x(self.x):
        return f''

    #
    # def desplazar_y(self.y):
    #     return f''
    #
    # def hallar_pendiente(self.other):
    #     return f''
