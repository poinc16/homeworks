# Escreva um programa que receba como entrada dois números inteiros quaisquer A e B e exiba todas as tabuadas existentes no intervalo fechado crescente [ A..B ].

# Entrada

# Dois números inteiros, um em cada linha.

# Saída

# As tabuadas de todos os valores inteiros no intervalo fechado crescente [ A..B ]. Ao fim de cada tabuada, exibir uma linha com dez hifens ('-'). Caso A seja maior do que B, o intervalo será vazio e, neste caso, deve ser exibida somente a frase 'Nenhuma tabuada no intervalo!', sem apóstrofos. Obs.: Lembre-se de não exibir texto no input.

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
    print('----------')
    return


n1 = int(input())
n2 = int(input())

if n1 <= n2:
    for i in range(n1, n2+1):
        multiplication_tables(i)
else:
    print('Nenhuma tabuada no intervalo!')
