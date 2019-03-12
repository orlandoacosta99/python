import unittest
import estructura_control_condicional as Test

class pruebas(unittest.TestCase):
    def test_esParentesis(self):
        self.assertEqual(Test.esParentesis('('), 'Es paréntesis')
        self.assertEqual(Test.esParentesis('k'), 'No es paréntesis')
        self.assertEqual(Test.esParentesis('as'), TypeError(str(caracter) + ' no es un parentesis'))

    def test_division(self):
        self.assertEqual(Test.division(4, 2), 2.0)
        self.assertEqual(Test.division(15, 3), 5.0)
        self.assertEqual(Test.division(5, 0), ZeroDivisionError('La división en cero no es posible'))
        self.assertEqual(Test.division('as', 5), TypeError(str(dividendo) + ' no es numerico'))
        self.assertEqual(Test.division(4, 'h'), TypeError(str(divisor) + ' no es numerico'))

    def test_impar_par(self):
        self.assertEqual(Test.impar_par(4), 'es par')
        self.assertEqual(Test.impar_par(7), 'es impar')
        self.assertEqual(Test.impar_par('as'), TypeError(str(num) + ' no es numerico'))

    def test_esDobledeunImpar(self):
        self.assertEqual(Test.esDobledeunImpar(14), '14 es doble de 7, que es impar')
        self.assertEqual(Test.esDobledeunImpar(2.6),TypeError(str(num) + ' no es numero o entero'))
        self.assertEqual(Test.esDobledeunImpar('asd'), TypeError(str(num) + ' no es numero o entero'))

    def test_numprimos(self):
        self.assertEqual(Test.numprimos(7), 'si es primo')
        self.assertEqual(Test.numprimos(4), 'no es primo')
        self.assertEqual(Test.numprimos('as'), TypeError(str(num) + ' no es numero o entero'))
        self.assertEqual(Test.numprimos(2.7), TypeError(str(num) + ' no es numero o entero'))

if __name__ == 'main':
    unittest.main()