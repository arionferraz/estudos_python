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

from pickle import TRUE


idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida, digite um valor entre 0 e 150: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    salario = int(input("Salario inválido, digite um valor acima 0: "))

sexo = input("Digite M para masculino, F para feminino e Outro para outras: ")

while True:
    if sexo == "M":
        break
    elif sexo == "F":
        break
    elif sexo == "outro":
        break
    else:
        sexo = input("Sexo inválido, digite M para masculino, F para feminino e outro para outras: ")