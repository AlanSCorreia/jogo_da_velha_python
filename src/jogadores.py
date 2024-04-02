class Jogadores:
    def __init__(self,
                 jogador1: str,
                 jogador2: str) -> None:

        self.__jogador1 = jogador1
        self.__jogador2 = jogador2
        self.jogador_atual = None

    def __str__(self) -> str:

        return self.jogador_atual

    def definir_jogador_atual(self,
                              rodada: int) -> None:
        """ Muda o valor do atributo self.jogador_atual de acordo com o número da variavel rodada

        Esse metodo define quem é o jogador atual com base em qual rodada o jogo está:
            Se rodada for um número par, o jogador atual será o jogador1
            Se rodada for um número ímpar, o jogador atual será o jogador2
        """

        match rodada % 2:

            case 0: self.jogador_atual = self.__jogador1
            case 1: self.jogador_atual = self.__jogador2


if __name__ == '__main__':

    jogador_atual = Jogadores(jogador1='S',
                              jogador2='A')

    for rodada in range(3):
        jogador_atual.definir_jogador_atual(rodada=rodada)
        print(jogador_atual)
