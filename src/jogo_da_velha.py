from matriz import Matriz
from jogadores import Jogadores
from validar_matriz import ValidarMatriz
from validar_input import input_manager


class JogoDaVelha:
    def __init__(self,
                 jogador1: str,
                 jogador2: str):

        self.matriz = Matriz()
        self.jogadores = Jogadores(jogador1=jogador1,
                                   jogador2=jogador2)

    def game_loop(self):

        for rodada in range(10):

            if rodada == 9:

                print(self.matriz)
                print("E M P A T E ! ! !")
                break

            print(self.matriz)
            self.jogadores.definir_jogador_atual(rodada=rodada)
            linha, coluna = input_manager(matriz=self.matriz)

            self.matriz[linha][coluna] = self.jogadores.jogador_atual
            is_jogador_atual_vencendor = ValidarMatriz(matriz=self.matriz,
                                                       jogador=str(self.jogadores)).validar()

            if is_jogador_atual_vencendor:
                print(self.matriz)
                print(f"O jogador {self.jogadores} é o vencedor")
                break


if __name__ == '__main__':

    jogo = JogoDaVelha()
    jogo.game_loop()
