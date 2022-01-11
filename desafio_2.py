#1 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... 
print("---------------------FIBONACCI-------------------------")
number = int(input("Até qual número você deseja? "))
atual = 1
anterior = 1
soma = 0 

if number==1:
    print("A sequência de Fibonacci é 1")
elif number==2:
    print("A sequência de Fibonacci é 1 1")
else:
    print("A sequência de Fibonacci é 1  1  ",end='')
    while atual < number: #coloco assim para ir realmente até o número que o usuário colocou
        soma = anterior + atual
        anterior = atual
        atual = soma
        print(soma," ",end='')
print()


# 2 - Faça um programa que crie uma matriz NxN, insira os valores e imprima em formato de matriz.
print("---------------------MATRIZ-------------------------")
num = int(input("Qual a dimensão da matriz desejada? "))
print("P.S.: digite no sentido das linhas.\n")
matriz = []

for i in range(num):
    vetor = []
    for j in range(num):
        elemento = float(input("Digite o valor do elemento: "))
        vetor.append(elemento)
    matriz.append(vetor)

for j in range(num):
    print(matriz[j])

    
