import unittest
from app import saludo

class TestHola(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo(), "Hola Mundo")

if __name__ == "__main__":
    unittest.main()