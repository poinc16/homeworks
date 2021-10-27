# Sua tarefa é construir um programa que receba como entrada um número natural N (0 <= N <= 10) e exibir a tabuada de N de 1 até 10.

# Entrada

# Um número natural N (0 <= N <= 10).

# Saída

# Exibir a tabuada do valor dado na entrada, conforme o modelo de saída dos exemplos.

def multiplication_tables(number):
    print(f'{number} x 1 = {number*1}')
    print(f'{number} x 2 = {number*2}')
    print(f'{number} x 3 = {number*3}')
    print(f'{number} x 4 = {number*4}')
    print(f'{number} x 5 = {number*5}')
    print(f'{number} x 6 = {number*6}')
    print(f'{number} x 7 = {number*7}')
    print(f'{number} x 8 = {number*8}')
    print(f'{number} x 9 = {number*9}')
    print(f'{number} x 10 = {number*10}')
    return


n = int(input())

multiplication_tables(n)
