import unittest
import adn as Test

class pruebas(unittest.TestCase):

    def test_obtener_complemento(self):
        self.assertEqual(Test.obtener_complemento(),)
    """   
    def test_generar_cadena_complementaria(self):
        self.assertEqual(Test.generar_cadena_complementaria(),)
        
    def test_calcular_correspondencia(self):
        self.assertEqual(Test.calcular_correspondencia(),)
        
    def test_corresponden(self):
        self.assertEqual(Test.corresponden(), )
    
    def test_es_cadena_valida(self):
        self.assertEqual(Test.es_cadena_valida(), )
    
    def test_es_base(self):
        self.assertEqual(Test.es_base(), )
    
    def test_es_subcadena(self):
        self.assertEqual(Test.es_subcadena(), )
    
    def test_reparar_dano(self):
        self.assertEqual(Test.reparar_dano(), )

    def test_obtener_secciones(self):
        self.assertEqual(Test.obtener_secciones(), )

    def test_obtener_complementos(self):
        self.assertEqual(Test.obtener_complementos(), )
    
    def test_unir_cadena(self):
        self.assertEqual(Test.unir_cadena(), )
        
    def test_complementar_cadenas(self):
        self.assertEqual(Test.complementar_cadenas(), )
    """

if __name__ == 'main':
    unittest.main()