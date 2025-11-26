from db_manager import DBManager
import unittest
from unittest.mock import Mock, call

class TestClientes(unittest.TestCase):
    def setUp(self):
        #Creamos mocks para la conexión a la BD y el cursor
        self.mock_conn = Mock()
        self.mock_cursor = Mock()
        
        # La conexión debe devolver un cursor
        self.mock_conn.cursor.return_value = self.mock_cursor
        
        #Creamos un mock que simula ser una instancia de DBManager
        self.dbm = DBManager(self.mock_conn)
        
    def test_add_cliente_valido(self):
        # Definimos el cliente valido a insertar
        cliente_valido = ("Juan", "juan@uam.mx")
        
        # Llamar a la función a probar
        self.dbm.add_cliente(cliente_valido[0],cliente_valido[1])
        
        # Verificar las llamadas
        # Llamada 1: execute('INSERT...')
        self.assertEqual(self.mock_cursor.execute.call_args_list.
              count(
                  call('INSERT INTO clientes (nombre, correo) VALUES (?, ?)', cliente_valido)),
              1
              )
        # Llamada 2: commit()

if __name__ == "__main__":
    unittest.main(verbosity=2)