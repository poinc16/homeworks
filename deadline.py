# "Tempos modernos"… e não nos referimos ao clássico filme de Charles Chaplin, mas sim às facilidades que a tecnologia proporciona, inimagináveis há algumas décadas. Uma dessas tecnologias é a internet, que possibilitou as compras online.

# Podemos comprar em sites de empresas e em poucos dias a mercadoria estará em nossas mãos. A Impacta Express, uma multinacional de comércio eletrônico e com sua própria logística de distribuição, quer revolucionar realizando qualquer entrega no prazo de até seis dias a partir da realização da compra.

# Por participar de sites de programação como o URI Online Judge, o coordenador de TI da Impacta Express encontrou você entre os primeiros do rank, ficou fascinado com seu desempenho e te convidou para uma entrevista!

# Como parte da entrevista, o coordenador solicitou um programa que receba como entrada dois valores: (I) uma string com um dia da semana ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação, que indica o dia que um cliente realizou a compra no site da empresa; (II) um número natural que pode variar de 0 a 6, que indica a quantidade de dias, a partir da realização da compra, que o cliente deverá aguardar para receber a mercadoria. O programa deve exibir o dia da semana que a compra será entregue.

# Note que um prazo de zero dias significa que a entrega será concluída no mesmo dia, assim como um prazo de dois dias significa que a entrega será concluída exatamente dois dias após a realização da compra. Por exemplo, se a compra foi realizada no 'sabado' e o prazo é de três dias, o cliente receberá na 'terca'. Cuidado com a acentuação, repare que ela não está presente nas entradas e nem nas saídas, nem mesmo o 'ç' de terça.

# Entrada

# A entrada é composta por duas linhas, a primeira conterá uma string que corresponde a um dia da semana, que poderá ser qualquer um destes: ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta' ou 'sabado'), sem acentuação e sem os apóstrofos, que representa o dia em que o cliente realizou a compra; a segunda linha contém um número natural entre 0 e 6 (inclusive os extremos), que indica o prazo que o cliente deve esperar até receber sua compra.

# Saída

# Uma string que indica o dia que o usuário receberá sua compra. Caso o usuário receba no mesmo dia, deverá ser exibida a string 'chega hoje!', sem apóstrofos. Caso o usuário receba em algum dos seis dias posteriores à compra, deverá ser exibida a string 'sera entregue <dia>', em que <dia> será o dia correspondente, também sem apóstrofos e sem acentuação.

weekday = input()
days_to_delivery = int(input())

weekdays = ['domingo', 'segunda', 'terca',
            'quarta', 'quinta', 'sexta', 'sabado']

if days_to_delivery == 0:
    print('chega hoje!')
else:
    if weekday == 'domingo':
        deadline = 0 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'segunda':
        deadline = 1 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'terca':
        deadline = 2 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'quarta':
        deadline = 3 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'quinta':
        deadline = 4 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'sexta':
        deadline = 5 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    elif weekday == 'sabado':
        deadline = 6 + days_to_delivery
        if deadline > 6:
            deadline = deadline - 7
            delivery_day = weekdays[deadline]
        else:
            delivery_day = weekdays[deadline]

    print(f'sera entregue {delivery_day}')
