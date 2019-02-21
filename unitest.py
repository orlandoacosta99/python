import unittest
import funtions

class TestCalc(unittest.TestCase):

    def test_add(self):

        result= funtions.add(10,5)

        self.assertEqual(result,15)

        self.assertEqual(funtions.add(10, 5), 15)

    def test_rest(self):
        result = funtions.rest(10, 5)

        self.assertEqual(result, 5)

        self.assertEqual(funtions.rest(10, 5), 5)

    def test_mul(self):
        result = funtions.mul(10, 5)

        self.assertEqual(result, 50)

        self.assertEqual(funtions.mul(10, 5), 50)

    def test_div(self):
        result = funtions.div(10, 5)

        self.assertEqual(result, 2)

        self.assertEqual(funtions.div(10, 5), 2)

    def test_por(self):
        result = funtions.mul(10, 5)

        self.assertEqual(result, 0)

        self.assertEqual(funtions.mul(10, 5), 0)


if __name__ == '__main__':
    unittest.main()

