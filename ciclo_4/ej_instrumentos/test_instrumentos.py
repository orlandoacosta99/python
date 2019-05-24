from unittest import TestCase
from Inventario import Instrumentos
from Inventario import Cuerdas
from Inventario import Percusion

class TestInstrumentos(TestCase):
    def test_clas_instrumento(self):
        dado = Instrumentos('Violonchelo', 'cuerdas', 4)
        espero = 'el instrumento Violonchelo es de cuerdas'
        recibo = dado.clas_instrumento()
        self.assertEqual(espero, recibo)


        dado = Instrumentos('bombo', 'percusion', 5)
        espero = 'el instrumento bombo es de percusion'
        recibo = dado.clas_instrumento()
        self.assertEqual(espero, recibo)

        dado = Instrumentos('trompeta', 'aire', 5)
        self.assertRaises(ValueError, dado.clas_instrumento)

    def test_cantidad(self):

        dado = Instrumentos('guitarra', 'cuerdas', 10)
        espero = 'el instrumento guitarra es de cuerdas y tinene la cantidad de 10 instrumentos'
        recibo = dado.cantidad()
        self.assertEqual(espero, recibo)

        dado = Instrumentos('caja', 'percusion', 7)
        espero = 'el instrumento caja es de percusion y tinene la cantidad de 7 instrumentos'
        recibo = dado.cantidad()
        self.assertEqual(espero, recibo)

        dado = Instrumentos('ukelele', 'cuerdas', -82)
        self.assertRaises(ValueError, dado.cantidad)

class TestCuerdas(TestCase):
    def test_cuerdas(self):
        dado = Cuerdas('Violin', 'cuerdas', 12)
        espero = 'el instrumento Violin  es de cuerdas, tiene 4 cuerdas y estan afinadas en MI,LA,RE,SOL y tiene  la cantidad de 12 instrumentos'
        resultado = dado.cuerdas(4, 'MI,LA,RE,SOL')
        self.assertEqual(espero, resultado)

        dado = Cuerdas('Bajo', 'cuerdas', '12')
        espero = 'el Bajo no puede tener cuerdas negativas'
        resultado= dado.cuerdas
        self.assertRaises(ValueError, dado.cuerdas, -4, 'Mi, La, Re, Sol')

class TestPercusion(TestCase):

    def test_percusion(self):
        dado = Percusion('Tambor', 'percucion', 8)
        espero = 'el instrumento Tambor es de percucion,  tiene un diametro de 25 cm y una frecuencia de vibracion es de 40 hz y tiene  la cantidad de 8 instrumentos'
        resultado = dado.percusion(25, 40)
        self.assertEqual(espero, resultado)

        dado = Percusion('Tambora', 'percucion', 4)
        self.assertRaises(ValueError, dado.percusion, -11, 271)
