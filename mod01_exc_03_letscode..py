'''
    3.  Vamos fazer um programa para verificar quem é o assassino de um crime.
        Para descobrir o assassino, a polícia faz um pequeno questionário com 5
        perguntas onde a resposta só pode ser sim ou não:

        a. Mora perto da vítima?
        b. Já trabalhou com a vítima?
        c. Telefonou para a vítima?
        d. Esteve no local do crime?
        e. Devia para a vítima?

        Cada resposta sim dá um ponto para o suspeito. A polícia considera que os
        suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são cúmplices e
        2 pontos são apenas suspeitos, necessitando outras investigações. Valores
        iguais ou abaixo de 1 são liberados.
'''
print('Para descobrir o assassino, responda à polícia o pequeno questionário asseguir com 5 perguntas onde a resposta só pode ser sim ou não:')

cont =0
while True:
    resposta = input('Mora perto da vítima? ')
    if resposta=="sim":
        cont+=1
        break
    elif resposta == 'não':
        break
    else:
        print('Responda sim ou não" ')

while True:
    resposta = input('Já trabalhou com a vítima? ')
    if resposta=="sim":
        cont+=1
        break
    elif resposta == 'não':
        break
    else:
        print('Responda sim ou não" ')

while True:
    resposta = input('Telefonou para a vítima? ')
    if resposta=="sim":
        cont+=1
        break
    elif resposta == 'não':
        break
    else:
        print('Responda sim ou não" ')

while True:
    resposta = input('Esteve no local do crime? ')
    if resposta=="sim":
        cont+=1
        break
    elif resposta == 'não':
        break
    else:
        print('Responda sim ou não" ')

while True:
    resposta = input('Devia para a vítima? ')
    if resposta=="sim":
        cont+=1
        break
    elif resposta == 'não':
        break
    else:
        print('Responda sim ou não" ')

if cont == 1:
    print('É inocente, está iberado!!')
elif cont == 2:
    print('É suspeito, serão feitas maiores investigações!!')
elif cont == 3 or cont == 4:
    print('É cumplice, ficará detido!!')
elif cont == 5:
    print('É assassino, ficará detido!!')