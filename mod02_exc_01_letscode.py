'''
    1.  Faça um programa que olhe todos os itens de uma lista e diga quantos deles
        são pares.

'''
lista = []
while True:
    temp = input("Digite um numero para adicionar a lista, para sair digite sair: ")
    if temp.lower() == "sair":
        break
    
    if temp.lstrip('-').isnumeric() == True:
        lista.append(int(temp))
        #print(lista)
    else:
        print("Valor inválido...")
cont = 0
for i in range(len(lista)):
    if lista[i]%2 == 0 and lista[i] != 0:
        cont += 1
print(f"Você digitou {cont} numeros pares")