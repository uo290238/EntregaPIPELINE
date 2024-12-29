
import unittest
from distancia import distancia_euclidea_2d

class TestDistanciaEuclidea(unittest.TestCase):

    def test_distancia_2d(self):
        p1 = (1, 2)
        p2 = (4, 6)
        resultado = distancia_euclidea_2d(p1, p2)
        self.assertEqual(resultado, 5)  # Sabemos que la distancia entre (1, 2) y (4, 6) es 5

if __name__ == '__main__':
    unittest.main()
