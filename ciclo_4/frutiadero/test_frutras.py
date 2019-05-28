from unittest import TestCase
from frutas import Frutas

class TestFrutras(TestCase):
    def test_pelar(self):
        dado = Frutas('banano', 10)
        espero = True
        real = dado.pelar()

        self.assertEqual(real, espero)
        self.assertRaises(ValueError, dado.pelar)

    def test_cortar(self):
        dado = Frutas('papaya', 1000)
        espero = 130
        real = dado.cortar(1)
        self.assertEqual(espero, real)
        dado = Frutas('piña', 2500)
        espero = 360
        real = dado.cortar(6)
        self.assertEqual(espero, real)

        dado = Frutas('manzana', 100)
        espero = 'No tiene frutas para cortar'
        self.assertRaises(ValueError, dado.cortar, 0)
        dado = Frutas('pera', 300)
        espero = 'No tiene frutas para cortar'
        self.assertRaises(ValueError, dado.cortar, -1)

    def test_licuar(self):
        dado = Frutas('papaya', 1000)
        espero = 11000
        real = dado.licuar(5)
        self.assertEqual(espero, real)
        dado = Frutas('piña', 2500)
        espero = 9000
        real = dado.licuar(6)
        self.assertEqual(espero, real)

        dado = Frutas('manzana', 100)
        espero = 'No tiene frutas para cortar'
        self.assertRaises(ValueError, dado.licuar, 0)
        dado = Frutas('pera', 300)
        espero = 'No tiene frutas para cortar'
        self.assertRaises(ValueError, dado.licuar, -1)