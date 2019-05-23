from unittest import TestCase
from Inventario import Instrumentos

class TestInstrumentos(TestCase):
    def test_cantidad(self):
        dado = Instrumentos('Violonchelo', 'La', 'jazz', 'cuerdas')
        espero = 4
        recibo = dado.cantidad(4)
        self.assertEqual(espero, recibo)

        self.assertRaises(ValueError, dado.cantidad, -2)

    # def test_tipo_instrumento(self):
    #     dado = Instrumentos('guitarra', 'RE', 'rock')
    #     espero = ''
    #     recibo = dado.tipo_instrumento('cuerdas')
    #     self.assertEqual(espero, recibo)
    #
    #     dado = Instrumentos('caja', 'no tiene', 'vallenato')
    #     espero = ''
    #     recibo = dado.tipo_instrumento('percucion')
    #     self.assertEqual(espero, recibo)
    #
    #     dado = Instrumentos('cordeon', ' SOL', 'vallenato', ' ')
    #     self.assertRaises(ValueError, dado.tipo_instrumento, ' ')

    def test_cuerdas(self):
        dado = Instrumentos('Violin', 'MI', 'Jazz', 'cuerdas')
        espero = 'el instrumento Violin tiene 4 cuerdas y estan afinadas en MI,LA,RE,SOL'
        resultado = dado.cuerdas(4, 'MI,LA,RE,SOL')
        self.assertEqual(espero, resultado)

        dado = Instrumentos('Bajo', 'MI', 'ROCK', 'cuerdas')
        self.assertRaises(ValueError, dado.cuerdas, -4, 'Mi, La, Re, Sol')


    def test_percusion(self):
        dado = Instrumentos('Tambor', 'no tiene', 'jazz', 'percucion')
        espero = 'el instrumento Tambor tiene un diametro de 25 cm y una frecuencia de vibracion es de 40 hz'
        resultado = dado.percusion(25, 40)
        self.assertEqual(espero, resultado)

        dado = Instrumentos('Tambora', 'no tiene', 'merengue', 'percucion')
        self.assertRaises(ValueError, dado.percusion, -11, 271)
