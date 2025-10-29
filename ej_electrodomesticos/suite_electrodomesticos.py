import unittest
#Importo las clase que implementan las pruebas
from tests.test_electrodomesticos import TestElectrodomestico
from tests.test_lavadoras import TestLavadora
from tests.test_refrigeradores import TestRefrigerador

def suite_electrodomesticos():
    # Creo un cargador de prueba para cada clase prueba
    test_electro = unittest.defaultTestLoader.loadTestsFromTestCase(TestElectrodomestico)
    test_lavadora = unittest.defaultTestLoader.loadTestsFromTestCase(TestLavadora)
    test_refri = unittest.defaultTestLoader.loadTestsFromTestCase(TestRefrigerador)
    # Lista de cargadores de pruebas
    pruebas = [test_electro,test_lavadora,test_refri]
    
    # Creo la suite de pruebas
    suite = unittest.TestSuite()
    #suite = unittest.TestSuite(pruebas)
    
    # Agregamos lista de cargadores o cargadores solos
    #suite.addTest(test_electro)
    suite.addTests(pruebas)
    
    #Devolvemos la suite
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite_electrodomesticos()
    runner.run(suite)
    
    