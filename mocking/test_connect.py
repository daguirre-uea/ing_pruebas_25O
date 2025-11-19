import unittest 
from unittest.mock import patch, call
import sqlite3

class TestConnect(unittest.TestCase):
    @patch("sqlite3.connect")
    def test_llamdas_ordenas(self,connect_mock):
        #Simulamos llamadas
        sqlite3.connect("mi_base.db")
        sqlite3.connect()
        sqlite3.connect(bd="bd")
        sqlite3.connect()
        
        #obtengo las llamadas realizadas
        llamadas_realizadas = connect_mock.call_args_list
        #definir lista de llamadas esperadas
        llamadas_esperadas = [call("mi_base.db"),call(),call(bd="bd"),call()]
        
        #verifica que se llamo a la función dos veces sin argumentos
        self.assertEqual(connect_mock.call_args_list.count(call()),2)
        
        # verifica que la lista de llamadas esperadas es igual que las realizadas
        self.assertEqual(llamadas_esperadas, llamadas_realizadas)
        #verifica el numero de llamadas
        self.assertEqual(connect_mock.call_count,4)
        
        # verifica que cada llamada se realice en el orden esperado
        for i in range(3):
            arg_esperados = llamadas_esperadas[i]
            arg_reales = llamadas_realizadas[i]
            with self.subTest(arg_esperados = arg_reales):
                self.assertEquals(arg_esperados,arg_reales)

if __name__ == "__main__":
    unittest.main(verbosity=2)