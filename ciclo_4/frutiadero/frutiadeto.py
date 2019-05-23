
class Frutiadero:
    tipo = ''
    inventario = {'banano': [5, 100],
                  'manzana': [6, 50],
                  'pera': [5, 70],
                  'piña': [60, 1500],
                  'papaya': [130, 2200]}
    ingredientes = ''

    def __init__(self, tipo, ingredientes):

        self.tipo = tipo
        self.ingredientes = ingredientes

    def preparar(self, tipo, ingredientes):
        if tipo == 'ensalada':
            return Ensalada.alistar(ingredientes)

        elif tipo == 'jugo':
            return Jugo.preparar(ingredientes)
