class Frutas:

    sabor = ''
    pelada = False
    cantidad = 0
    __TIPOS__ = {'banano': [5, 100],
                 'manzana': [6, 50],
                 'pera': [5, 70],
                 'piña': [60, 1500],
                 'papaya': [130, 2200]
                 }

    def __init__(self, sabor, cantidad):
        self.sabor = sabor if sabor in self.__TIPOS__ else 'banano'
        self.cantidad = cantidad

    def pelar(self):

        if not self.pelada:
            self.pelada = True
            return self.pelada
        raise ValueError('la fruta esta pelada')

    def cortar(self, cantidad_usar):

        self.cantidad_usar = cantidad_usar

        if not self.pelada and cantidad_usar > 0 and self.sabor == 'banano':
            return cantidad_usar * 5

        elif not self.pelada and cantidad_usar > 0 and self.sabor == 'manzana':
            return cantidad_usar * 6

        elif not self.pelada and cantidad_usar > 0 and self.sabor == 'pera':
            return cantidad_usar * 5

        elif not self.pelada and cantidad_usar > 0 and self.sabor == 'piña':
            return cantidad_usar * 60

        elif not self.pelada and cantidad_usar > 0 and self.sabor == 'papaya':
            return cantidad_usar * 130

        elif cantidad_usar <= 0 or self.pelada:
            raise ValueError('No tiene frutas para cortar')



    def licuar(self, cantidad_usar):

        self.cantidad_usar = cantidad_usar

        if not self.pelada and self.cortar and cantidad_usar > 0 and self.sabor == 'banano':
            return cantidad_usar * 100
        elif not self.pelada and self.cortar and cantidad_usar > 0 and self.sabor == 'manzana':
            return cantidad_usar * 50
        elif not self.pelada and self.cortar and cantidad_usar > 0 and self.sabor == 'pera':
            return cantidad_usar * 70
        elif not self.pelada and self.cortar and cantidad_usar > 0 and self.sabor == 'piña':
            return cantidad_usar * 1500
        elif not self.pelada and self.cortar and cantidad_usar > 0 and self.sabor == 'papaya':
            return cantidad_usar * 2200

        elif self.pelada or cantidad_usar <= 0:
            raise ValueError('No se puede hacer jugo')

