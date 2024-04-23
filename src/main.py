from jogo_da_velha import JogoDaVelha
from validar_input import escolher_jogador


def main():

    jogador1 = escolher_jogador()
    jogador2 = escolher_jogador(letra_invalida=jogador1)

    jogo = JogoDaVelha(jogador1=jogador1,
                       jogador2=jogador2)
    
    jogo.game_loop()


if  __name__ == "__main__":

    main()
