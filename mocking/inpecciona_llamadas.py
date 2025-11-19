from unittest.mock import Mock, call
import sqlite3
# Mockeamos el módulo sqlite3
sqlite3 = Mock()
# Llamamos a connect sin argumentos
sqlite3.connect()
# La función mockeada se llama con un argumento nombrado
sqlite3.connect(database="mi_base_de_datos.db")
# Llamamos a connect con un argumento posicional
sqlite3.connect("mi_base_de_datos.db")
# Inspeccionamos las llamadas realizadas a connect
print(f"Número de llamadas a sqlite3.connect: {sqlite3.connect.call_count}")
print(f"Lista de llamadas a sqlite3.connect: {sqlite3.connect.call_args_list}")
print(f"Argumentos de la última llamada: {sqlite3.connect.call_args}")