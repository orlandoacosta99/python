class Frutas:

    sabor = ''
    pelada = False
    cantidad = 0

    def __init__(self, sabor, cantidad):
        self.sabor = sabor
        self.cantidad = cantidad

    def pelar(self):

        if not self.pelada:
            self.pelada = True
            return self.pelada
        raise ValueError('la fruta esta pelada')

    def cortar(self, cantidad__usar):



    def licuar(self, cantidad_usar):

        pass