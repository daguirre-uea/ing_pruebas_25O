# usar src como carpeta base para importar módulos
#import sys
#import os
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from src.electrodomesticos import Electrodomestico, Refrigerador, Lavadora
class TestRefrigerador(unittest.TestCase):
    def setUp(self):
        """Crea un refrigerador para las pruebas"""
        self.refri = Refrigerador("Samsung", "FamilyHub", 350)
    
        
    def test_instancia_Refrigerador(self):
        """Pruebas para instancias de Refrigerador"""
        # Prueba Refrigerador
        self.assertIsInstance(self.refri,Refrigerador)
        