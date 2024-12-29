import unittest
from factorial import calcular_factorial

class TestCalcularFactorial(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(calcular_factorial(5), 120)
        self.assertEqual(calcular_factorial(0), 1)
        self.assertEqual(calcular_factorial(1), 1)

    def test_factorial_negativo(self):
        with self.assertRaises(ValueError):
            calcular_factorial(-5)

if __name__ == '__main__':
    unittest.main()
