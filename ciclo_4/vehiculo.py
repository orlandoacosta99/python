class Vehiculo:


    n_ruedas = 0
    placa = ''
    color = ''

    def __init__(self, n_ruedas, placa, color):
        self.n_ruedas = n_ruedas
        self.placa = placa
        self.color = color
        self.encendido = False

    def mover(self, distancia):
        pass

    def reversa(self, distancia):
        pass

    def encender(self):
        """

        :return:
        """
        if self.encendido:
            self.encendido = False
        else:
            self.encendido = True
        return self.encendido

    def frenar(self):
        pass
