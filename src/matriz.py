class Matriz:
    def __init__(self) -> None:

        self.__matriz = [[' ' for _ in range(3)] for _ in range(3)]

    def __str__(self) -> str:
        """ Retorna um valor string da instância da classe quando utilizado o metodo str() ou print()

         Dunder Method que retorna a grade com elementos da matriz em formato de string
        """

        return self.__imprimir()

    def __getitem__(self,
                    item: int) -> list[str]:
        """ Retorna uma string de uma lista de strings

        Dunder Method que retona uma linha da matriz direto da instância da classe
        """

        return self.__matriz[item]

    def __setitem__(self,
                    indice,
                    valor) -> None:
        """ Atribui um valor a uma string de uma lista de strings usando o indice da mesma

         Dunder Method que atribui um valor a um atributo utilizando o indice
        """

        self.__matriz[indice] = valor

    def __imprimir(self) -> str:
        """ Retorna uma lista de strings convertida em uma string

        Função que junta os elementos da matriz em uma grade de jogo da velha
        """

        grade = [
            f' {self.__matriz[0][0]} | {self.__matriz[0][1]} | {self.__matriz[0][2]} \n',
            '---+---+---\n',
            f' {self.__matriz[1][0]} | {self.__matriz[1][1]} | {self.__matriz[1][2]} \n',
            '---+---+---\n',
            f' {self.__matriz[2][0]} | {self.__matriz[2][1]} | {self.__matriz[2][2]} \n'
        ]

        return ''.join(grade)


if __name__ == '__main__':
    matriz = Matriz()
    print(matriz)
