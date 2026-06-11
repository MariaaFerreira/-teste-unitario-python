# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, poten, calcular_media


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar_dois_inteiros_positivos(self):
        """Testa a multiplicação de dois inteiros positivos."""
        self.assertEqual(multiplicar(3, 4), 12)

    def test_multiplicar_com_zero(self):
        """Testa a multiplicação de um número por zero."""
        self.assertEqual(multiplicar(5, 0), 0)

    def test_multiplicar_positivo_por_negativo(self):
        """Testa a multiplicação de número positivo por negativo."""
        self.assertEqual(multiplicar(6, -2), -12)

    def test_multiplicar_dois_numeros_negativos(self):
        """Testa a multiplicação de dois números negativos."""
        self.assertEqual(multiplicar(-3, -4), 12)

    def test_multiplicar_com_numero_decimal(self):
        """Testa a multiplicação com número decimal."""
        self.assertEqual(multiplicar(2.5, 4), 10.0)

    def test_multiplicar_dois_zeros(self):
        """Testa a multiplicação de dois zeros."""
        self.assertEqual(multiplicar(0, 0), 0)

    def test_multiplicar_por_numero_muito_grande(self):
        """Testa a multiplicação por número muito grande."""
        self.assertEqual(multiplicar(10**10, 10**5), 10**15)

    def test_multiplicar_string_por_numero(self):
        """Testa o comportamento do Python ao multiplicar string por número."""
        self.assertEqual(multiplicar("abc", 2), "abcabc")

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

    def test_divisao_exata(self):
        """Testa divisão exata."""
        self.assertEqual(dividir(10, 2), 5.0)

    def test_divisao_com_resultado_decimal(self):
        """Testa divisão com resultado decimal."""
        self.assertEqual(dividir(5, 2), 2.5)

    def test_divisao_de_numero_negativo(self):
        """Testa divisão de número negativo."""
        self.assertEqual(dividir(-10, 2), -5.0)

    def test_divisao_de_dois_numeros_negativos(self):
        """Testa divisão de dois números negativos."""
        self.assertEqual(dividir(-10, -2), 5.0)

    def test_divisao_de_zero_por_outro_numero(self):
        """Testa divisão de zero por outro número."""
        self.assertEqual(dividir(0, 5), 0.0)

    def test_poten(self):
        self.assertEqual(poten(2, 3), 8)
        self.assertEqual(poten(10, 2), 100)
        self.assertEqual(poten(5, 0), 1)

    def test_inteiros(self):
        self.assertEqual(calcular_media([10, 20, 30]), 20)

    def test_decimais(self):
        self.assertEqual(calcular_media([1.5, 2.5]), 2.0)

    def test_um_numero(self):
        self.assertEqual(calcular_media([7]), 7)

    def test_lista_vazia(self):
        with self.assertRaises(ValueError):
            calcular_media([])


if __name__ == "__main__":
    unittest.main()