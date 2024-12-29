import unittest
from maximo import encontrar_maximo

class TestEncontrarMaximo(unittest.TestCase):

    def test_lista_valores(self):
        self.assertEqual(encontrar_maximo([1, 2, 3, 4, 5]), 5)
        self.assertEqual(encontrar_maximo([-10, -5, -1, -20]), -1)

    def test_lista_vacia(self):
        with self.assertRaises(ValueError):
            encontrar_maximo([])

if __name__ == '__main__':
    unittest.main()
