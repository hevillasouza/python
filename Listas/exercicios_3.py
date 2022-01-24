# 1. Faça um Programa que leia 5 números inteiros, insira em uma lista e mostre-os.
print("---------------CRIAÇÃO DE LISTA-------------------")
lista = []

for i in range(0,5):
    num = float(input("Digite um número real: "))
    lista.append(num)
print(f"A lista de números que você digitou é {lista}!\n")


# 2. Programa que leia 10 números reais, insira em uma lista e mostre-os na ordem crescente
print("---------------LISTA ORDENADA-------------------")
lis_ta = []

for i in range(0,10):
    num = float(input("Digite um número real: "))
    lis_ta.append(num)
print(f"A lista de números que você digitou ordenada é {sorted(lis_ta)}!\n")


# 3. Programa que leia N (peça pro usuário) notas insira em uma lista e calculea média 
print("--------------------MÉDIAS NOTAS---------------------")
N = int(input("Quantas notas você deseja adicionar? "))
soma = 0

for n in range(0,N):
    print(f"Nota {n+1}: ",end='') #aqui é para que o próximo print seja impresso na mesma linha
    nota = float(input(" digite o valor - "))
    soma += nota
print(f"A média das notas é {soma/N} ! \n")


# 4. Programa que peça informações N pessoas, armazene em uma lista e depois insira em lista_pessoas. 
# Por fim, imprima o nome e peso de cada pessoa, e diga se ela é maior ou menor de idade.

n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []

for j in range(n):
    nome = input("\nDigite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    altura = float(input("Digite a sua altura: "))
    nova_pessoa = [nome, idade,altura]
    lista_pessoas.append(nova_pessoa)

for pessoa in lista_pessoas:
    print(f"\nO seu nome é {pessoa[0]}, você tem {pessoa[1]} anos e sua altura é {pessoa[2]}!")
    if pessoa[1] >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")


# 5. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.(usar for com range)
print("----------------NÚMEROS EM SEQUÊNCIA---------------------")

for k in range(1,21): #tem que dizer para colocar de 1, porque por defaut é 0 e tem que ir até 21, para completar os 20
    print(k)


# 6. Programa que leia 5 números e informe o maior número.
print("----------------MAIOR DA LISTA---------------------")
lisTa = []

for a in range(5):
    num = float(input("Digite um número: "))
    lisTa.append(num)

lisTa.sort() #aqui altera a ordenação da própria lista
print(f"O maior número é {lisTa[-1]}!\n")


# 7. Programa que imprima na tela apenas os números ímpares entre 1 e 50.
print("----------------ÍMPARES DE 1 A 50---------------------")

for b in range(1,50):
    if b % 2 != 0:
        print(b)


# 8. Programa que receba dois números inteiros e gere os números inteiros que estão no intervalo entre eles.
# FIQUEI EM DÚVIDA SE É SÓ ENTRE ELES
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))

if int1 >= int2:
    maior = int1
    menor = int2
else:
    menor = int1
    maior = int2

intervalo = menor + 1
for b in range(intervalo,maior):
    while intervalo < maior:
        print(intervalo)
        intervalo += 1


# 9. programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
print("----------------MAIOR, MENOR E SOMA DA LISTA---------------------")
listinha = []
sominha = 0
ene = int(input("Quantos números você quer adicionar: "))

for c in range(ene):
    num = float(input("Digite um número: "))
    listinha.append(num)

listinha.sort() #aqui altera a ordenação da própria lista
print(f"O maior número é {listinha[-1]}, o menor número é {listinha[0]} e a soma é {listinha[-1]+listinha[0]}!\n")  


# 10.Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
# O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
print("-------------------TABUADA---------------------")
number = int(input("Qual tabuada você deseja (de 1 a 10)? "))

print(f"\n___________Tabuada de {number}___________")
for d in range(11):
    print(f"\t    {d} x {number} = {d*number}")
print()



   
