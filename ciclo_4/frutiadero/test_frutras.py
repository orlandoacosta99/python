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
        dado= Frutas(5)
        espero = ()


    def test_licuar(self):
        pass