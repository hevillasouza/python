# 1. Leia números reais, quando for zero deverá apresentar uma lista com todos os números e sair do laço while.
print("-------------LISTA DE NÚMEROS, MENOS ZERO-------------")
lista = []

while True:
    num = float(input("Digite um número: "))
    if num != 0:
        lista.append(num)
    else:
        break
print(f"{lista}\n")


# 2. Programa que receba um usuário e senha. Se a senha de entrada for igual ao usuário, deverá ser 
# apresentada a mensagem “Senha Inválida”, e pedir pro usuário inserir a senha novamente. 
print("-------------USUÁRIO E SENHA-------------")

nome = input("\nQual o seu nome de usuário? ")
while True:
    senha = input("Qual a sua senha? ")
    if senha == nome:
        print("Senha inválida, por favor corrija a informação!\n")
    else:
        print("Senha válida!\n")
        break


# 3. Faça um programa que lê um número inteiro n. Escrever a soma de todos os números de 1 até n. Use while.
print("----------SOMA DOS NÚMEROS INTEIROS----------")

i = 1
soma = 0
n = int(input("\nDigite um número inteiro: "))

while i <= n:
    soma = soma + i
    i = i + 1
print(f"A soma de todos os números de 1 até {n} é {soma}!\n")


# 4. Faça um programa para ler um número inteiro n. Escrever a soma de todos os números pares de 2 até n.
print("----------SOMA DOS NÚMEROS INTEIROS PARES----------")

j = 0
soma_pares = 0
ene = int(input("\nDigite um número inteiro: "))

if ene % 2 == 0:
    while j <= ene:
        soma_pares = soma_pares + j
        j = j + 2
else:
    while j < ene:
        soma_pares = soma_pares + j
        j = j + 2

print(f"A soma de todos os números de 2 até {ene} é: {soma_pares}!\n")


# 5. Faça um programa que lê um número inteiro n. E verifique se n é um número par, se não for pedir para inserir outro número até que seja par. 
print("----------NÚMERO PAR----------")

while True:
    numero = int(input("\nDigite um número inteiro: "))
    if numero % 2 == 0:
        break
    else:
        print("Esse número não é par!")
print(f"O número par digitado é {numero}!\n")


# 6. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
print("----------NÚMERO PARES E ÍMPARES----------")
k = 0
pares = []
impares = []

print()
while k < 10:
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    k = k + 1

print(f"\nOs números pares são {pares}!")
print(f"Os números ímpares são {impares}!\n")
