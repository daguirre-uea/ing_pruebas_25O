from unittest.mock import Mock

def mi_funcion():
    print("¡Hola, mundo!")
    
# llamamos a mi_funcion
mi_funcion()
# Mockear la función... ahora mi_funcion es un mock
mi_funcion = Mock()
#llamamos 2 veces a la función
mi_funcion()
mi_funcion()

print("Llamadas a la funcion: ",mi_funcion.call_count)