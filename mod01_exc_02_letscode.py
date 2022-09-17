'''
    2. Faça um programa que leia a validade das informações:
        a. Idade: entre 0 e 150;
        b. Salário: maior que 0;
        c. Sexo: M, F ou Outro;
    O programa deve imprimir uma mensagem de erro para cada informação
    inválida.
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