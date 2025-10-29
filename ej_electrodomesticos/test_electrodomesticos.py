import unittest
from electrodomesticos import Electrodomestico, Refrigerador, Lavadora
class TestElectrodomestico(unittest.TestCase):
    def test_fabrica_varios_electrodomesticos(self):
        """Usa la fábrica para crear objetos y probarlos con subTest"""
        """Configura varios electrodomésticos para las pruebas"""
        self.lavadora = Lavadora("LG", "TwinWash", 10)
        self.refrigerador = Refrigerador("Samsung", "FamilyHub", 350)
        productos = [self.lavadora, self.refrigerador]
        for producto in productos:
            with self.subTest(producto=producto):
                self.assertIsInstance(producto, Electrodomestico)
                self.assertIsNotNone(producto.marca)
                self.assertIsNotNone(producto.modelo)
        
    def test_tipo_incorrecto(self):
        """Pruebas para crear objetos con tipos de datos incorrectos"""
        # Prueba Lavadora
        with self.assertRaisesRegex(TypeError, r"Marca y modelo deben ser strings"):
            Lavadora(123, "FamilyHub", 100)
        #Prueba Refrigerador   
        with self.assertRaisesRegex(TypeError, r"El volumen debe ser de tipo entero"):
            Refrigerador("LG", "MX200", "40")
        
if __name__ == "__main__":
    unittest.main(verbosity=2)