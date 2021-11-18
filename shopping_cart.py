# Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho. Cada item é representado no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você decidiu guardar os itens adicionados ao carrinho em uma lista, e para testar o seu programa, implementou alguns comandos básicos para simular uma interação do usuário com o sistema:

# adicionar: inclui o código de um novo produto à lista;remover: remove o código de um produto da lista;exibir: exibe os itens da lista em ordem crescente;encerrar: exibe os itens da lista, assim como no comando exibir, em ordem crescente, e encerra o programa.

# A primeira linha poderá conter uma lista de inteiros separados por espaços, representando produtos que já estavam no carrinho, por exemplo, de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras já com os códigos dessa lista, que devem ser números inteiros.

# Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum texto ou caractere.

# Entrada

# A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha em branco;

# Cada linha seguinte conterá um dos comandos listados acima e, para os comandos "adicionar" e "remover", conterá também o código de um produto separado por um espaço;

# A entrada termina sempre com o comando "encerrar".

# Saída

# A saída deve conter:

# A exibição dos códigos na lista, separados por espaço, de acordo com a execução dos comandos "exibir" e "encerrar";A mensagem "código <código> não encontrado", quando o comando remover é executado com um código que não esteja presente na lista. Substitua <código> pelo número do código em questão (veja os exemplos para maiores detalhes).

# Obs.: Lembre-se de não exibir texto no input.

def add(cod, cart):
    cart.append(cod)
    return


def remove(cod, cart):
    try:
        cart.remove(cod)
    except:
        print(f'código {cod} não encontrado')
    return


def show(cart):
    bubble_sort(cart, len(cart))
    number_of_codes = len(cart)
    v = 0
    for k in cart:
        v += 1
        if v == number_of_codes:
            print(k)
        else:
            print(k, end=' ')
    return


def bubble_sort(l, n):
    tam = n
    while tam > 1:
        i = 0
        while i < tam-1:
            if l[i] > l[i+1]:
                change(i, i+1, l)
            i += 1
        tam -= 1
    return


def change(v1, v2, l):
    temp = l[v1]
    l[v1] = l[v2]
    l[v2] = temp
    return


cart = []

before = input()
if before != '':
    list_before = before.split()

    for i in list_before:
        cod = int(i)
        add(cod, cart)

while True:
    action = input()
    action_list = action.split()
    try:
        cod = int(action_list[1])
    except:
        pass

    if action_list[0] == 'adicionar':
        add(cod, cart)

    elif action_list[0] == 'remover':
        remove(cod, cart)

    elif action_list[0] == 'exibir':
        show(cart)

    elif action_list[0] == 'encerrar':
        show(cart)
        break
