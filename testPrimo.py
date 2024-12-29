import unittest
from primo import es_primo

class TestEsPrimo(unittest.TestCase):

    def test_primos(self):
        self.assertTrue(es_primo(2))
        self.assertTrue(es_primo(11))

    def test_no_primos(self):
        self.assertFalse(es_primo(1))
        self.assertFalse(es_primo(15))
        self.assertFalse(es_primo(0))

if __name__ == '__main__':
    unittest.main()
