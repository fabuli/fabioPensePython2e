    Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros recursos que aprendemos até agora.

    Escreva uma função que desenhe uma grade como a seguinte:

        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +

    Dica: para exibir mais de um valor em uma linha, podemos usar uma sequência de valores separados por vírgula:

    print('+', '-')

    Por padrão, print avança para a linha seguinte, mas podemos ignorar esse comportamento e inserir um espaço no fim, desta forma:

    print('+', end=' ')
     print('-')

    A saída dessas instruções é + -. Uma instrução print sem argumento termina a linha atual e vai para a próxima linha.

    Escreva uma função que desenhe uma grade semelhante com quatro linhas e quatro colunas.

def imprime():
    print('+', '-' * 4, '+', '-' * 4, '+')
    print('|', ' ' * 4, '|', ' ' * 4, '|') 
    print('|', ' ' * 4, '|', ' ' * 4, '|') 
    print('|', ' ' * 4, '|', ' ' * 4, '|') 
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-' * 4, '+', '-' * 4, '+')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('|', ' ' * 4, '|', ' ' * 4, '|')
    print('+', '-' * 4, '+', '-' * 4, '+')
    
