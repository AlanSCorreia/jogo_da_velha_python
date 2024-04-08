from src.matriz import Matriz
type Jogador = str


class ValidarMatriz:
    def __init__(self,
                 matriz: Matriz,
                 jogador: Jogador):

        self.__matriz = matriz
        self.__jogador = jogador

    def __horizontal_vertical(self):

        for linha in range(3):

            horizontal = all([(self.__matriz[coluna][linha] == self.__jogador) for coluna in range(3)])
            vertical = all([(self.__matriz[linha][coluna] == self.__jogador) for coluna in range(3)])

            if horizontal or vertical:
                return True

        return False

    def __diagonais(self):

        diagonal_esquerda = all([self.__matriz[indice][indice] == self.__jogador for indice in range(3)])
        diagonal_direita = all([self.__matriz[indice][2-indice] == self.__jogador for indice in range(3)])

        return diagonal_esquerda or diagonal_direita

    def validar(self):

        validar_vitoria = (self.__horizontal_vertical() or self.__diagonais())
        return validar_vitoria
