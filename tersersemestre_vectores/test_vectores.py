import unittest
import vectores as Test

class TestCalc(unittest.TestCase):
    def test_producto_escalar(self):
        self.assertEqual(Test.producto_escalar(2,[1, 2, 3]), [2, 4, 6])
        self.assertEqual(Test.producto_escalar(3, [3, 2, 1,4]), [9, 6, 3, 12])
        self.assertEqual(Test.producto_escalar(6, [2, 1, 2]), [12, 6, 12])

    def test_suma_productos(self):
        self.assertEqual(Test.suma_productos([1, 2, 3],[2, 1, 3]), [3, 3, 6])
        self.assertEqual(Test.suma_productos([4, 7, 1], [8, 5, 2]), [12, 12, 3])
        self.assertEqual(Test.suma_productos([2, 4, 2], [3, 2, 8]), [5, 6, 10])

    def test_producto_puntos(self):
        self.assertEqual(Test.producto_puntos([1, 2, 3],[2, 1, 3]), 13)
        self.assertEqual(Test.producto_puntos([1, 2, -3], [-2, 4, 1]), 3)
        self.assertEqual(Test.producto_puntos([2, 1, 2], [2, 4, 1]), 10)

    def test_elemento_mayor(self):
        self.assertEqual(Test.elemento_mayor([2, 4, 1]), 4)
        self.assertEqual(Test.elemento_mayor([8, 5, 2]), 8)
        self.assertEqual(Test.elemento_mayor([9, 6, 3, 12]), 12)

    def test_elemento_menor(self):
        self.assertEqual(Test.elemento_menor([2, 4, 6, 7, 5]), 2)
        self.assertEqual(Test.elemento_menor([1, 2, 5, 1, 6]), 1)
        self.assertEqual(Test.elemento_menor([21, 42, 2, 12, 5]), 2)

    def test_prom(self):
        self.assertEqual(Test.prom([1, 2, 4, 2, 1, 2]), 2.0)
        self.assertEqual(Test.prom([2, 1, 3, 5, 6, 2]), 3.1666666666666665)
        self.assertEqual(Test.prom([2, 2, 2, 1, 5, 5, 6]), 3.2857142857142856)

    def test_desviacion_est(self):
        self.assertEqual(Test.desviacion_est([2, 34, 3, 2 , 1, 4]), 12.940891262454324)
        self.assertEqual(Test.desviacion_est([2, 4, 5, 6, 8, 1, 2]), 2.516611478423583)
        self.assertEqual(Test.desviacion_est([3, 5, 6, 8, 1, 3]), 2.503331114069145)

    def test_elemento_igual(self):
        self.assertEqual(Test.elemento_igual([2, 5, 6, 7, 8]), 'no hay elementos repetidos')
        self.assertEqual(Test.elemento_igual([1, 2, 1, 5, 2, 1]), [1, 2])
        self.assertEqual(Test.elemento_igual([2, 1, 3, 5, 6, 8, 4]), 'no hay elementos repetidos')
        self.assertEqual(Test.elemento_igual([2, 1, 3, 3, 2]), [3, 2])

    def test_Norma_vec(self):
        self.assertEqual(Test.Norma_vec([2, 4, 1, 5]), 6.782329983125268)
        self.assertEqual(Test.Norma_vec([2, 3, 2, 1]), 4.242640687119285)
        self.assertEqual(Test.Norma_vec([1, -3, 5, 2, 2]), 6.557438524302)

    def test_Moda_vec(self):
        self.assertEqual(Test.Moda_vec([1, 2, 5, 2, 1, 3, 1]), [1])
        self.assertEqual(Test.Moda_vec([2, 1, 2, 2, 5, 3, 3, 1]), [2])
        self.assertEqual(Test.Moda_vec([1, 2, 3, 4, 5, 2, 4, 3]), [2, 3, 4])

if __name__ == '__main__':
    unittest.main()
