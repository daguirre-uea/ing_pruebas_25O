import unittest
from calificaciones_uam import calificacion

class test_calificacion(unittest.TestCase):
    def test_excepciones(self):
        """Prueba de excepciones y mensaje"""
        with self.assertRaisesRegex(ValueError,r"^El puntaje está fuera de rango, se recibió "):
            calificacion(13)
            
        with self.assertRaisesRegex(TypeError,r"^El puntaje debe ser int o float, se recibió "):
            calificacion("13")
        
    def test_puntaje_invalido_negativo(self):
        """Prueba de puntaje inválido negativo"""
        for i in range (-10, 0):
            puntaje = str(i/10)
            with self.subTest(puntaje=puntaje):
                with self.assertRaisesRegex(TypeError, r"^El puntaje debe ser int o float, se recibió "):
                    calificacion(puntaje)
    
    def test_puntaje_invalido_positivo(self):
        """Prueba de puntaje inválido positivo"""
        for i in range (11,21):
            puntaje = -i
            with self.subTest(puntaje=puntaje):
                with self.assertRaisesRegex(ValueError, r"^El puntaje está fuera de rango, se recibió "):
                    calificacion(puntaje)
                
    def test_calificacionA(self):
        """Prueba de calificación A"""
        for i in range(90,101):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "A")
    
    def test_calificacionB(self):
        """Prueba de calificación B"""
        for i in range(75,90):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "B")
    
    def test_calificacionS(self):
        """Prueba de calificación S"""
        for i in range(60,75):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "S")
        
    def test_calificacionNA(self):
        """Prueba de calificación NA"""
        for i in range(0,60):
            puntaje = i/10
            with self.subTest(puntaje=puntaje):
                self.assertEqual(calificacion(puntaje), "NA")

#Ejecutar el codigo
if __name__ == "__main__":
    unittest.main(verbosity=2)