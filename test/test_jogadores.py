import unittest
from src.jogadores import Jogadores


class JogadoresTestCase(unittest.TestCase):
    jogadores = Jogadores(jogador1='X',
                          jogador2='O')

    def test_primeira_jogada(self):

        self.jogadores.definir_jogador_atual(rodada=0)
        self.assertEqual('X', str(self.jogadores))

    def test_segunda_jogada(self):

        self.jogadores.definir_jogador_atual(rodada=1)
        self.assertEqual('O', str(self.jogadores))


if __name__ == '__main__':
    unittest.main()
