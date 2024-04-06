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


def is_elemento_vazio(matriz: Matriz,
                      linha: int,
                      coluna: int) -> bool:

    return matriz[linha][coluna] == ' '


def input_manager(matriz: Matriz) -> tuple[int, int]:

    linha = validar_input("Escolha uma linha entre [1 / 2 / 3]: ") - 1
    coluna = validar_input("Escolha uma coluna entre [1 / 2 / 3]: ") - 1

    while not is_elemento_vazio(matriz=matriz, linha=linha, coluna=coluna):

        print("Este indice já foi utilizado, escolha novamente.")
        linha = validar_input("Escolha uma linha entre [1 / 2 / 3]: ") - 1
        coluna = validar_input("Escolha uma coluna entre [1 / 2 / 3]: ") - 1

    return linha, coluna


if __name__ == '__main__':

    m = Matriz()
    m[0][0] = 'A'
    linha, coluna = input_manager(m)

    print(linha)
    print(coluna)
