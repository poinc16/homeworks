# Os números primos têm diversas aplicações, principalmente na criptografia utilizada pelo aplicativo de seu banco e nos sites de compra que nos trazem tanta comodidade.

# Um número natural é considerado primo quando possui somente dois divisores, o número um e ele próprio. O número zero e o número um não são primos e o número dois é o único primo par.

# Seu objetivo é criar um programa que receba como entrada dois números naturais, INÍCIO e FIM, e exibe os números primos que existem no intervalo fechado [ INÍCIO..FIM ]. Ao final, o programa também deve exibir a quantidade de primos encontrados no intervalo.

# Entrada

# Dois números naturais, INÍCIO e FIM, respectivamente, um por linha. Adote (INICIO <= FIM <= 5000).

# Saída

# Os números primos presentes no intervalo fechado [ INÍCIO..FIM ] e a quantidade de números primos do intervalo, conforme o padrão exibido nos exemplos.

def prime_numbers(initial, final):
    cont = 0
    for i in range(initial, (final+1)):
        verify = 0
        if i == 1 or i == 0:
            verify += 1
        for j in range(2, (i)):
            if i % j == 0 and j != i:
                verify += 1
        if verify == 0:
            print(i)
            cont += 1
    print(f'primos: {cont}')
    return


n1 = int(input())
n2 = int(input())

prime_numbers(n1, n2)
