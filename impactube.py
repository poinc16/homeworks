# A ImpacTube, uma famosa empresa de compartilhamento de vídeos, quer premiar alguns de seus mais notáveis criadores de conteúdo. Para isso, a ImpacTube montará uma tabela com alguns dos canais que possuem grande quantidade de usuários inscritos.

# No site da ImpacTube, os canais geram renda para seus criadores de conteúdo por meio de diversos mecanismos, a conhecida "monetização", o que geralmente é influenciado pela quantidade de inscritos no canal e que acessam aos vídeos postados.

# Para possibilitar a premiação, cada registro da tabela (vide exemplo na Figura 1) terá quatro campos dispostos em colunas na seguinte ordem:

# O nome do canal;A quantidade atual de inscritos; A monetização do último mês do canal e;Um valor indicando se o canal produz conteúdo premium, que são vídeos exclusivos para usuários que pagam uma mensalidade à ImpacTube.

# Com esses dados será possível definir a bonificação de cada canal, que será composta pelo valor "monetização" da tabela acrescido de um valor fixo para cada mil inscritos. 

# O valor fixo será definido pela ImpacTube, sendo X para canais com conteúdo premium e Y para os que não possuem conteúdo premium.

# Você foi escolhido para desenvolver um programa que receberá como entrada os dados de cada canal, gerando internamente a tabela modelo, e que mostrará os nomes dos canais, na ordem em que foram dados na entrada, acompanhados do valor que receberão como bonificação. Observe cuidadosamente o formato de entrada e o formato de saída especificados.
# Entrada
# Na primeira linha será informado um número inteiro que representa a quantidade N (1 <= N <= 200) de canais da tabela;
# Em cada uma das N linhas seguintes serão informados os registros que compõem a tabela, com os valores das colunas separados por um ponto e vírgula, nesta ordem: (1) uma string com o nome do canal que será bonificado; (2) um número natural que é a quantidade de inscritos no canal; (3) um número real simbolizando a monetização do canal no mês anterior (dado em reais R$) e; (4) uma string 'sim' ou 'não', sem apóstrofos e completamente em minúsculo, que indica se o canal produz conteúdo premium;
# Por fim, serão informados dois números reais X e Y, um em cada linha, que indicam o valor fixo (em reais R$) que os canais receberão a mais para cada mil inscritos no canal. O primeiro valor é X e refere-se aos canais que possuem conteúdo premium. O segundo valor é Y e refere-se aos canais que não possuem conteúdo premium.
# Saída
# O cabeçalho contém três linhas,  sendo a primeira e a terceira compostas por apenas cinco hifens, e a segunda composta unicamente pela palavra 'BÔNUS', sem apóstrofos e completamente em maiúsculo. Nas próximas N linhas, estão os nomes dos canais, na mesma ordem em que foram dados na entrada, acompanhados à direita pelo valor que receberão como bonificação, em reais e com duas casas decimais, exatamente como consta nos exemplos.

def write_channels(number_channels):
    names = []
    followers = []
    money = []
    premium = []
    i = 0
    while i < number_channels:
        temp_channel = input().split(';')
        names.append(temp_channel[0])
        followers.append(int(temp_channel[1]))
        money.append(float(temp_channel[2]))
        premium.append(temp_channel[3])
        i += 1
    return names, followers, money, premium


def calc_bonus(premium_bonus, not_premium_bonus, followers, is_premium, money):
    bonus_list = []
    cont = 0
    for i in followers:
        number_to_bonus, trash = divmod(i/1000, 1)
        if is_premium[cont].lower() == 'sim':
            bonus_list.append((number_to_bonus*premium_bonus) + money[cont])
        else:
            bonus_list.append(
                (number_to_bonus*not_premium_bonus) + money[cont])
        cont += 1
    return bonus_list


def show(channel_name, bonus, number):
    print('-----')
    print('BÔNUS')
    print('-----')
    for j in range(0, number):
        print(f'{channel_name[j]}: R$ {bonus[j]:.2f}')
    return


channels = int(input())
names, followers, money, premium = write_channels(channels)

yes_premium = float(input())
not_premium = float(input())

bonus = calc_bonus(yes_premium, not_premium, followers, premium, money)

show(names, bonus, channels)
