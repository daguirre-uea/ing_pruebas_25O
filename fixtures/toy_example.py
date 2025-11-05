import unittest

class TestArchivo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Configuración inicial de la clase (una vez antes de todos los tests)")

    def setUp(self):
        print("Preparando entorno para un test (antes de cada test)")
        self.archivo = open("temp.txt", "w")
        self.archivo.write("dato de prueba")

    def test_lectura(self):
        print("Ejecutando test_lectura")
        self.assertTrue(self.archivo)

    def test_instancia(self):
        print("Ejecutando test_instancia")
        self.assertIsInstance("texto", str)

    def tearDown(self):
        print("Limpiando entorno del test (después de cada test)")
        self.archivo.close()

    @classmethod
    def tearDownClass(cls):
        print("Limpiando recursos globales de la clase (una vez después de todos los tests)")

if __name__ == "__main__":
    unittest.main(verbosity=2)