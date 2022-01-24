# 1. Programa que peça dois números e imprima o maior.
print("------------------MAIOR DE DOIS NÚMEROS----------------------")
num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))

if num1 >= num2:
    print("O maior número é: ",num1,"\n")
else:
    print("O maior número é: ",num2)


# 2. Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print("------------------NÚMERO POSITIVO OU NEGATIVO----------------------")
num = float(input("Digite o valor do número: "))

if num >= 0:
    print("O número",num,"é positivo.\n")
else:
    print("O número",num,"é negativo.\n")


# 3. IMC e as suas categorias
print("------------------ÍNDICE DE MASSA CORPORAL----------------------")
peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso/(altura**2)

print("O seu IMC é",imc)

if  imc < 18.49:
    print("Você está na categoria desnutrição!\n")
elif imc >= 18.5 and imc <= 24.99:
    print("Você está na categoria eutrofia\n!")
elif imc >= 25 and imc <= 29.99:
    print("Você está na categoria sobrepeso\n!")
elif imc >= 30 and imc <= 34.9:
    print("Você está na categoria obesidade grau I !\n")
elif imc >= 35 and imc <= 39.99:
    print("Você está na categoria obesidade grau II (severa)!\n")
elif imc >= 40:
    print("Você está na categoria obesidade grau III (mórbita)!\n")

# 4. Programa que verifica o tipo da letra 
print("------------------FEMININO OU MASCULINO----------------------")
letra = input("Digite F para feminino ou M para masculino: ")

if letra == "F":
    print("F - Feminino!\n")
elif letra == "M":
    print("M - Masculino!\n")
else:
    print("Sexo inválido!\n")


# 5. Programa que verifique se uma letra digitada é vogal ou consoante.
print("--------------------VOGAL OU CONSOANTE---------------------")
letter = input("Digite alguma letra do alfabeto: ")
vogais = ["a","e","i","o","u","A","E","I","O","U"]

if letter in vogais: #esse comando é para ver se o elemento está na lista
    print("Essa letra",letter,"é uma vogal!\n")
else:
    print("Essa letra",letter,"é uma consoante!\n")


# 6. O programa deve calcular a média alcançada por aluno
print("--------------------MÉDIA ALUNO---------------------")
nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))

media = (nota1 + nota2)/2

print("A sua média é",media)

if media == 10:
    print("Aprovado com distinção!\n")
elif media < 10 and media >= 7:
    print("Aprovado!\n")
else:
    print("Reprovado!\n")


# 7. Programa que peça três números e imprima o maior.
print("------------------MAIOR DE TRÊS NÚMEROS----------------------")
numero1 = float(input("Digite o valor do primeiro número: "))
numero2 = float(input("Digite o valor do segundo número: "))
numero3 = float(input("Digite o valor do terceiro número: "))

if numero1 >= numero2 and numero1 >= numero3:
    print("O maior número é: ",numero1,"\n")
elif numero2 >= numero1 and numero2 >= numero3:
    print("O maior número é: ",numero2,"\n")
else:
    print("O maior número é: ",numero3,"\n")


# 8. Programa que peça três números e imprima o maior e o menor.
print("------------------MAIOR DE TRÊS NÚMEROS----------------------")
number1 = float(input("Digite o valor do primeiro número: "))
number2 = float(input("Digite o valor do segundo número: "))
number3 = float(input("Digite o valor do terceiro número: "))

if number1 >= number2 and number1 >= number3:
    print("O maior número é: ",number1)
    if number2 >= number3:
        print("O menor número é",number3,"\n")
    else:
        print("O menor número é",number2,"\n")
elif number2 >= number1 and number2 >= number3:
    print("O maior número é: ",number2)
    if number3 >= number1:
        print("O menor número é",number1,"\n")
    else:
        print("O menor número é",number3,"\n")
else:
    print("O maior número é: ",number3)
    if number1 >= number2:
        print("O menor número é",number2,"\n")
    else:
        print("O menor número é",number1,"\n")


# 9. Programa para determinar qual produto comprar
print("------------------LISTA DE COMPRAS----------------------")
produto1 = input("Qual o primeiro produto que deseja comprar? ")
preco1 = float(input("Qual o preço do primeiro produto? "))
produto2 = input("Qual o segundo produto que deseja comprar? ")
preco2 = float(input("Qual o preço do segundo produto? "))
produto3 = input("Qual o terceiro produto que deseja comprar? ")
preco3 = float(input("Qual o preço do terceiro produto? "))

if preco1 <= preco2 and preco1 <= preco3:
    print("Você deve comprar o produto",produto1,"\n")
elif preco2 <= preco1 and preco2 <= preco3:
    print("Você deve comprar o produto",produto2,"\n")
else:
    print("Você deve comprar o produto",produto3,"\n")


# 10.Faça um Programa que leia três números e mostre-os em ordem decrescente
print("--------------------ORDEM DECRESCENTE----------------------")
n1 = float(input("Digite o valor do primeiro número: "))
n2 = float(input("Digite o valor do segundo número: "))
n3 = float(input("Digite o valor do terceiro número: "))

if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        print("A ordem dos números é: ",n1,",",n2,",",n3,"\n")
    else:
        print("A ordem dos números é: ",n1,",",n3,",",n2,"\n")
elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        print("A ordem dos números é: ",n2,",",n1,",",n3,"\n")
    else:
        print("A ordem dos números é: ",n2,",",n3,",",n1,"\n")
else:
    if n2 >= n1:
        print("A ordem dos números é: ",n3,",",n2,",",n1,"\n")
    else:
        print("A ordem dos números é: ",n3,",",n1,",",n2,"\n")


# 11. Faça um Programa que pergunte em que turno você estuda
print("--------------------TURNO DE ESTUDO----------------------")
print("Digite a letra do turno que você estuda segundo a legenda abaixo")
turno = input("M-Matutino, V-Vespertino ou N- Noturno: ")

if turno == "M":
    print("Bom dia!\n")
elif turno == "V":
    print("Boa tarde!\n")
elif turno == "N":
    print("Boa noite!\n")
else:
    print("Valor inválido!\n")


# 12. Faça um Programa que determine se o número é par ou impar
print("--------------------PAR OU ÍMPAR---------------------")
n_um = int(input("Digite um número: "))

if n_um % 2 == 0:
    print("O número",n_um,"é par!")
else:
    print("O número",n_um,"é ímpar!")


# 13. O programa deve calcular o conceito do aluno
print("--------------------CONCEITO DO ALUNO---------------------")
nota_1 = float(input("Digite o valor da primeira nota: "))
nota_2 = float(input("Digite o valor da segunda nota: "))

med = (nota_1 + nota_2)/2

print("A sua média é",med)

if  med <= 10 and med > 9:
    print("O seu conceito é A!\n")
elif med <= 9 and med > 7.5:
    print("O seu conceito é B!\n")
elif med <= 7.5 and med > 6:
    print("O seu conceito é C!\n")
elif med <= 6 and med > 4:
    print("O seu conceito é D!\n")
elif med <= 4 and med >= 0:
    print("O seu conceito é E!\n")


# 14. O programa que leia um número e exiba o dia correspondente da semana
print("--------------------DIA DA SEMANA---------------------")
dia = int(input("Digite o número do dia da semana: "))

if  dia == 1:
    print("Domingo!\n")
elif dia == 2:
    print("Segunda-feira!\n")
elif dia == 3:
    print("Terça-feira!\n")
elif dia == 4:
    print("Quarta-feira!\n")
elif dia == 5:
    print("Quinta-feira!\n")
elif dia == 6:
    print("Sexta-feira!\n")
elif dia == 7:
    print("Sábado!\n")
else:
    print("Valor inválido!")


# 15. Programa que permita o usuário escolher entre três opções debebidas e mostre na tela a bebida escolhida
print("____________________MENU____________________")
print("\t1. Água")
print("\t2. Refrigerante")
print("\t3. Suco\n")

bebida = int(input("Digite o valor da bebida que deseja: "))

if bebida == 1:
    print("\nVocê escolheu água!\n")
elif bebida == 2:
    print("\nVocê escolheu refrigerante!\n")
elif bebida == 3:
    print("\nVocê escolheu suco!\n")


