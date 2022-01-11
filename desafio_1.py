"""
# 1. Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
print("-----------------NÚMERO POS, NEG OU NEUTRO----------------------")
num = int(input("Digite um número inteiro: "))

if num > 0:
    print("Esse é um número positivo!\n")
elif num == 0:
    print("Esse é um número neutro!\n")
else:
    print("Esse é um número negativo!\n")


# 2. Faça um programa que leia dois números inteiros e informe se estes são iguais ou diferentes
print("-------------------NÚMEROS IGUAIS?----------------------")
num1 = float(input("Digite o primero número: "))
num2 = float(input("Digite o segundo número: "))

if num1 == num2:
    print("Os números são iguais!\n")
else:
    print("Os números são diferentes!\n")


# 3. Faça um programa em que o usuário informe o salário recebido e o total gasto com despesas.
print("-------------------SALDO MENSAL----------------------")
salario = float(input("Você recebeu quanto de salário esse mês? "))
despesas = float(input("Quanto foi a despesa total do mês? "))

if salario>= despesas:
    print("Gastos dentro do orçamento!\n")
else:
    print("A mãe está estourada haha!\n")


# 4. Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário
print("-------------------NOVO SALÁRIO----------------------")
salario_antigo = float(input("Qual o seu salário antigo? "))

if salario_antigo < 500:
    print("O seu novo salário é",salario_antigo*1.15,"!\n")
elif salario_antigo >= 500 and salario_antigo <= 1000:
    print("O seu novo salário é",salario_antigo*1.1,"!\n")
else:
    print("O seu novo salário é",salario_antigo*1.05,"!\n")


#5. Se o nome for "Optimus Prime", imprima "Bem-vindo, você é um guerreiro de Cybertron". Caso contrário, imprima "Bom dia, NOME".
print("-------------------TESTE OPTIMUS PRIME----------------------")
nome = input("Qual o seu nome? ")

if nome == "Optimus Prime" or nome == "OPTIMUS PRIME" or nome == "optimus prime":
    print("Bem-vindo, você é um guerreiro de Cybertron!\n")
else:
    print("Bom dia,",nome,"!\n")


# 6. Escrever um programa em Python para ler um número inteiro e informar se ele é divisível por 5.
print("-------------------TESTE DIVISÍVEL POR 5----------------------")
numero = int(input("Digite o número que deseja testar: "))

if numero % 5 == 0:
    print("O número",numero,"é divisível por 5!\n")
else:
    print("O número",numero,"não é divisível por 5!\n")


# 7. Escrever um programa em linguagem Python que lê um valor i, inteiro e positivo e 3 valores a, b e c. 
# Se o valor de i é par então calcular e imprimir na tela a média aritmética de a, b e c. 
# Caso contrário, se i>10 então calcular e imprimir na tela a média aritmética e ponderada de a, b e c. 
# Os pesos dos valores são respectivamente 2, 3 e 4.
print("------------------TESTES DE NÚMEROS-----------------")
i = int(input("Digite um número inteiro e positivo:"))

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if i % 2 == 0:
    media = (a + b + c)/3
    print("A média aritmética de a, b e c é",media,"!\n")
elif i > 10:
    media_pond = ((a * 2) + (b * 3) + (c * 4))/9
    print("A média ponderada de a, b e c é",media_pond,"!\n")
"""

# 8. Escreva um programa em Python para encontrar números entre 100 e 400 (ambos inclusos), onde cada dígito de um número é um número par. 
# Os números obtidos devem ser impressos em sequência separada por vírgulas.

entre_100_400 = []

for i in range(100,400):
    i_str = str(i) #aqui é para que eu possa comparar cada termo do número
    if i % 2 == 0:
        entre_100_400.append(i)

#tenho que terminar esse






