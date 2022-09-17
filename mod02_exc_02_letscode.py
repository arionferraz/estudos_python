'''
    2.  Faça um programa que peça para o usuário digitar uma palavra e imprima
        cada letra em uma linha.

'''
palavra = input("Digite uma palavra: ")
print("A palavra que você digitou tem as seguintes letras: \n")
for i in range(len(palavra)):
    print(palavra[i])