import unittest
from unittest.mock import Mock, patch
import utils
    
class TestVeficaLlamadas1(unittest.TestCase):
    
    @patch('utils.adios') #utils.mi_funcion = mi_funcion_mock = Mock()
    def test_adios(self, adios_mock):
        utils.adios()
        utils.adios()
        utils.adios()
        self.assertEqual(adios_mock.call_count,3)
    
    @patch('utils.mi_funcion') #utils.mi_funcion = mi_funcion_mock = Mock()
    def test_llamadas_mock(self, mi_funcion_mock):
        # Llamamos a la función
        utils.mi_funcion()
        utils.mi_funcion()
        # El mock tiene métodos para verificar las llamadas:
        # Para verificar N veces, se usa call_count:
        self.assertEqual(mi_funcion_mock.call_count, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)