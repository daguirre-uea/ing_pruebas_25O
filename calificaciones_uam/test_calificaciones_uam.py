import unittest
from calificaciones_uam import calificacion
import sys

class test_calificacion(unittest.TestCase):
    @unittest.skip("Tiempo de procesamiento largo")
    def test_calificacionA(self):
        self.assertEqual(calificacion(9.7), "A")
        self.assertEqual(calificacion(9.8), "A")
    
    @unittest.skipIf(sys.platform == "darwin", "No se ejecuta en MacOS")
    def test_calificacionB(self):
        self.assertEqual(calificacion(8), "B")
        self.assertEqual(calificacion(8.1), "B")
    
    @unittest.skipUnless(sys.platform.startswith("darwin"), "Solo se ejecuta en MacOS")
    def test_calificacionS(self):
        self.assertEqual(calificacion(6.2), "S")
        
    def test_calificacionNA(self):
        self.assertEqual(calificacion(1), "NA")
        
    def test_puntaje_negativo_invalido(self):
        for c in range(1,10):
            with self.subTest(c=c):
                with self.assertRaises(ValueError):
                    calificacion(-c)
                    
    def test_puntaje_positivo_invalido(self):
        for c in (11,30):
            with self.subTest(c=c):
                with self.assertRaises(ValueError):
                    calificacion(c)
                    
    def test_tipo_de_dato(self):
        for c in ["x", [1,2], dict()]:
            with self.subTest(c=c):
                with self.assertRaises(TypeError):
                    calificacion(c)

#Ejecutar el codigo
if __name__ == "__main__":
    unittest.main(verbosity=1)