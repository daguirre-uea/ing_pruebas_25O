# usar src como carpeta base para importar módulos
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from src.electrodomesticos import Electrodomestico, Refrigerador, Lavadora
class TestElectrodomestico(unittest.TestCase):
    def setUp(self):
        """Configura varios electrodomésticos para las pruebas"""
        self.lavadora = Lavadora("LG", "TwinWash", 10)
        self.refrigerador = Refrigerador("Samsung", "FamilyHub", 350)
        
    def test_fabrica_varios_electrodomesticos(self):
        """Usa la fábrica para crear objetos y probarlos con subTest"""
        productos = [self.lavadora, self.refrigerador]
        for producto in productos:
            with self.subTest(producto=producto):
                self.assertIsInstance(producto, Electrodomestico)
                self.assertIsNotNone(producto.marca)
                self.assertIsNotNone(producto.modelo)