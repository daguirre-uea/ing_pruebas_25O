from unittest.mock import Mock
import sqlite3
# Mockeamos el módulo sqlite3
# Ahora todas sus funciones y atributos serán mocks
sqlite3 = Mock()
print(f"El módulo sqlite3 es un Mock: {type(sqlite3)}")
# La función original connect recibe el nombre de la base de datos como argumento
# pero el mock que definimos no recibe argumentos
sqlite3.connect()
print(f"Los métodos de sqlite3 son Mocks: {type(sqlite3.connect)}")
# Podemos definir atributos y métodos en el mock del módulo
sqlite3.mi_atributo = "3.35.4"