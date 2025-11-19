from unittest.mock import Mock
# Creo un objeto mock
cursor = Mock()
print(f"cursor: {type(cursor)}")
# Puedo definir métodos asociados al mock
cursor.execute = Mock()
# Puedo definir atributos asociados al mock
cursor.nombre_base_datos = "mi_base_de_datos"
# Los métodos como los atributos pueden ser mocks
print(f"El método execute() es un Mock: {type(cursor.cuenta_usuarios)}")
print(f"El atributo nombre_base_datos es una cadena: {type(cursor.nombre_base_datos)}")
print(f"El atributo connection es un Mock: {type(cursor.connection)}")
# Accediendo al valor del atributo mockeado
print(f"Nombre de la base de datos: {cursor.nombre_base_datos}")