import unittest
from src.matriz import Matriz


class MatrizTestCase(unittest.TestCase):
    def test_imprimir_matriz(self):

        matriz = Matriz()
        for linha in range(3):
            for coluna in range(3):
                matriz[linha][coluna] = 'X'

        self.assertEqual(' X | X | X \n---+---+---\n X | X | X \n---+---+---\n X | X | X \n', str(matriz))


if __name__ == '__main__':
    unittest.main()
