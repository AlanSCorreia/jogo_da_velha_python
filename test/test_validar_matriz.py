import unittest
from src.validar_matriz import ValidarMatriz
from src.matriz import Matriz


class TestUnitSucessos(unittest.TestCase):
    jogador = 'A'

    def test_deveria_preencher_primeira_linha_vertical_com_caracteres_iguais(self):

        # Arrange
        matriz = Matriz()
        expectativa = True

        # Act
        for n in range(3):
            matriz[0][n] = self.jogador

        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertTrue(resultado)

    def test_deveria_preencher_primeira_linha_horizontal_com_caracteres_iguais(self):

        # Arange
        matriz = Matriz()
        expectativa = True

        # Act
        for n in range(3):
            matriz[n][0] = self.jogador

        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertTrue(resultado)

    def test_deveria_preencher_linha_diagonal_direita_com_caracteres_iguais(self):

        # Arrange
        matriz = Matriz()
        expectativa = True

        # Act
        for n in range(3):
            matriz[n][2-n] = self.jogador

        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertTrue(resultado)


class TestUnitFalhas(unittest.TestCase):
    jogador = "A"

    def test_deveria_preencher_primeira_linha_vertical_com_caracteres_iguais_entao_adicionar_um_caractere_diferente(self):

        # Arrange
        matriz = Matriz()
        expectativa = False

        # Act
        for n in range(3):
            matriz[0][n] = self.jogador

        matriz[0][0] = 'S'
        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertFalse(resultado)

    def test_deveria_preencher_primeira_linha_horizontal_com_caracteres_iguais_entao_adicionar_um_caractere_diferente(self):

        # Arrange
        matriz = Matriz()
        expectativa = False

        # Act
        for n in range(3):
            matriz[n][0] = self.jogador

        matriz[0][0] = 'S'
        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertFalse(resultado)

    def test_deveria_preencher_linha_diagonal_direita_com_caracteres_iguais_entao_adicionar_um_caractere_diferente(self):

        # Arrange
        matriz = Matriz()

        # Act
        for n in range(3):
            matriz[n][2-n] = self.jogador

        matriz[0][2] = 'S'

        resultado = ValidarMatriz(matriz=matriz, jogador=self.jogador).validar()

        # Assert
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
