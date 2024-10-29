import unittest
from unittest.mock import patch
from io import StringIO

def celsiusafahrenheit():
    c = float(input("Introduce los grados celsius: "))
    t = (c * 9/5) + 32
    print(f"{c} ºC equivalen a {t} ºF")

def fahrenheitacelsius():
    f = float(input("Introduce los grados fahrenheit: "))
    t = (f - 32) * 5/9
    print(f"{f} ºF equivalen a {t} ºC")

class TestConversor(unittest.TestCase):

    @patch('builtins.input', side_effect=['0'])  # Simula la entrada del usuario
    @patch('sys.stdout', new_callable=StringIO)  # Captura la salida impresa
    def test_celsius_a_fahrenheit(self, mock_stdout, mock_input):
        celsiusafahrenheit()
        self.assertEqual(mock_stdout.getvalue().strip(), "0.0 ºC equivalen a 32.0 ºF")  # Esta prueba debería pasar

    @patch('builtins.input', side_effect=['32'])  # Simula la entrada del usuario
    @patch('sys.stdout', new_callable=StringIO)  # Captura la salida impresa
    def test_fahrenheit_a_celsius(self, mock_stdout, mock_input):
        fahrenheitacelsius()
        self.assertEqual(mock_stdout.getvalue().strip(), "32.0 ºF equivalen a 0.0 ºC")  # Esta prueba debería pasar

    @patch('builtins.input', side_effect=['100'])  # Simula la entrada del usuario
    @patch('sys.stdout', new_callable=StringIO)  # Captura la salida impresa
    def test_fahrenheit_a_celsius_falla(self, mock_stdout, mock_input):
        fahrenheitacelsius()
        self.assertEqual(mock_stdout.getvalue().strip(), "100.0 ºF equivalen a 37.0 ºC")  # Esta prueba fallará intencionadamente

if __name__ == '__main__':
    unittest.main()
