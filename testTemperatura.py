import unittest
from temperatura import celsius_a_fahrenheit, fahrenheit_a_celsius

class TestTemperatura(unittest.TestCase):

    def test_celsius_a_fahrenheit(self):
        self.assertEqual(celsius_a_fahrenheit(0), 32)
        self.assertEqual(celsius_a_fahrenheit(100), 212)
        self.assertEqual(celsius_a_fahrenheit(-40), -40)

    def test_fahrenheit_a_celsius(self):
        self.assertEqual(fahrenheit_a_celsius(32), 0)
        self.assertEqual(fahrenheit_a_celsius(212), 100)
        self.assertEqual(fahrenheit_a_celsius(-40), -40)

if __name__ == '__main__':
    unittest.main()
