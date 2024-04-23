from matriz import Matriz


def validar_input(mensagem: str) -> int:

    while True:

        try:
            output = int(input(mensagem))

            if output in range(1, 4):
                return output
            
            else:
                print("Erro: O número informado precisa estar entre 1 e 3, tente novamente.")

        except ValueError:
            print("Erro: O valor informado precisa ser um inteiro, tente novamente.")


def esta_elemento_vazio(matriz: Matriz,
                      linha: int,
                      coluna: int) -> bool:
    return matriz[linha][coluna] == ' '


def input_manager(matriz: Matriz) -> list[int]:

    linha = validar_input("Escolha uma linha entre [1 / 2 / 3]: ") - 1
    coluna = validar_input("Escolha uma coluna entre [1 / 2 / 3]: ") - 1

    while not esta_elemento_vazio(matriz=matriz, linha=linha, coluna=coluna):

        print("Este indice já foi utilizado, escolha novamente.")
        linha = validar_input("Escolha uma linha entre [1 / 2 / 3]: ") - 1
        coluna = validar_input("Escolha uma coluna entre [1 / 2 / 3]: ") - 1

    return [linha, coluna]


def escolher_jogador(letra_invalida: str = ' '):

    while True:

        try:
            jogador = input("Escolha uma letra para representa-lo: ").upper().strip()

            if jogador.isalpha() and jogador != letra_invalida:
                return jogador[0]
                    
            elif jogador.isnumeric():
                print("Apenas letras são válidas.")

            else:
                print("Valor inválido, tente novamente.")

        except ValueError:
            print("Valor inválido, tente novamente.")


if __name__ == '__main__':

    m = Matriz()
    m[0][0] = 'A'
    linha, coluna = input_manager(m)

    print(linha)
    print(coluna)
