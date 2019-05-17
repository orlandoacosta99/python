from ciclo_4.vehiculo import Vehiculo

class Carro(Vehiculo):

    def __init__(self, placa, color):
        super().__init__(4, placa, color)

    def mover(self, distancia):
        if self.encendido:
            return f'Moviendose {distancia}'
        else:
            raise Exception('el carro no esta encendico')

    def reversa(self, disancia):
        super().reversa()

    def encender(self):
        return super().encender()

    def frenar(self):
        super().frenar()
