'''
    3.  Faça uma função que recebe duas listas e retorna a soma item a item dessas
        listas.
        Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve
        retornar [1+3, 4+5, 3+1] = [4, 9, 4].
'''
lista1 = []
lista2 = []
soma = []
while True:
    temp = input("Digite um numero para adicionar à primeira lista, digite seguinte ir para próxima lista: ")
    if temp.lower() == "seguinte":
        break
    
    if temp.lstrip('-').isnumeric() == True:
        lista1.append(int(temp))
        #print(lista1)
    else:
        print("Valor inválido...")

for i in range(len(lista1)):
    temp = input("Digite um numero para adicionar à segunda lista, digite soma para mostrar o resultado: ")
    if temp.lower() == "soma":
        break
    
    if temp.lstrip('-').isnumeric() == True:
        lista2.append(int(temp))
        #print(lista2)
    else:
        print("Valor inválido...")

saida = "["
for i in range(len(lista1)):
    soma.append(lista1[i]+lista2[i])
    if i < (len(lista1) -1):
        saida = saida + str(lista1[i]) + " + " + str(lista2[i]) + ", "
    if i == (len(lista1)-1):
        saida = saida + str(lista1[i]) + " + " + str(lista2[i]) + "] = "

saida = saida + str(soma)

print("Efetuando a soma entre os respectivos itens das listas informadas:\n" + saida)
    
