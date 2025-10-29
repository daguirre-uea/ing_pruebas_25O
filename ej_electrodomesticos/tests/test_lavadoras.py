# usar src como carpeta base para importar módulos
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from src.electrodomesticos import Lavadora
class TestLavadora(unittest.TestCase):
    def setUp(self):
        """Crea una Lavadora"""
        self.lavadora = Lavadora("LG", "TwinWash", 10)
        
    def test_instancia_lavadora(self):
        # Prueba Lavadora
        self.assertIsInstance(self.lavadora, Lavadora)