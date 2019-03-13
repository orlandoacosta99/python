import unittest
import estructura_control_condicional as Test

class pruebas(unittest.TestCase):
    def test_esParentesis(self):
        self.assertEqual(Test.esParentesis('('), 'Es paréntesis')
        self.assertEqual(Test.esParentesis('k'), 'No es paréntesis')
        self.assertRaises(TypeError, lambda: Test.esParentesis('as'))


    def test_division(self):
        self.assertEqual(Test.division(4, 2), 2.0)
        self.assertEqual(Test.division(15, 3), 5.0)
        self.assertRaises(ZeroDivisionError, lambda: Test.division(5, 0))
        self.assertRaises(TypeError, lambda: Test.division('as', 5))
        self.assertRaises(TypeError, lambda: Test.division(4, 'h'))

    def test_impar_par(self):
        self.assertEqual(Test.impar_par(4), 'es par')
        self.assertEqual(Test.impar_par(7), 'es impar')
        self.assertRaises(TypeError, lambda: Test.impar_par('as'))

    def test_esDobledeunImpar(self):
        self.assertEqual(Test.esDobledeunImpar(14), '14 es doble de 7, que es impar')
        self.assertRaises(TypeError, lambda: Test.esDobledeunImpar(2.6))
        self.assertRaises(TypeError, lambda: Test.esDobledeunImpar('asd'))

    def test_num_primos_if(self):
        self.assertEqual(Test.num_primos_if(2), 'si es primo')
        self.assertEqual(Test.num_primos_if(1), 'no es primo')
        self.assertRaises(TypeError, lambda: Test.num_primos_if('as'))
        self.assertRaises(TypeError, lambda: Test.num_primos_if(2.1))

    def test_numprimos(self):
        self.assertEqual(Test.numprimos(7), 'si es primo')
        self.assertEqual(Test.numprimos(4), 'no es primo')
        self.assertRaises(TypeError, lambda: Test.numprimos('as'))
        self.assertRaises(TypeError, lambda: Test.numprimos(2.7))

    def test_Billetes(self):
        self.assertEqual(Test.Billetes(432), None != True('2 billetes de 200 euros.+1 billetes de 20 euros.+1 billetes de 10 euros.+2 monedas de 2 euros.'))
        self.assertRaises(TypeError, lambda: Test.Billetes('as'))

    def test_dias(self):
        self.assertEqual(Test.dias(5), 'viernes')
        self.assertRaises(TypeError, lambda: Test.dias('as'))
        self.assertEqual(Test.dias(8), 'debe ser mayor que 0 y menor que 8')


if __name__ == 'main':
    unittest.main()