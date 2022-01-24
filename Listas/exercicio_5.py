import math

# 1. Função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.
print("---------POSITIVO, NEGATIVO OU NEUTRO---------")
def pos_neg(num):
    if num > 0:
        return True
    elif num < 0:
        return False

num = int(input("Digite um valor inteiro: "))
if pos_neg(num) == True:
    print(f"{num} é um número positivo!\n")
elif pos_neg(num) == False:
    print(f"{num} é um número negativo!\n")
else:
    print(f"{num} é o número neutro!\n")


# 2. Função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A função deve retornar um valor booleano.
print("---------POSITIVO, NEGATIVO OU NEUTRO---------")
def par_impar(number):
    if number % 2 == 0:
        return True
    else:
        return False

number = int(input("Digite um valor inteiro: "))
if par_impar(number) == True:
    print(f"{number} é um número par!\n")
else:
    print(f"{number} é o número ímpar!\n")


# 3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
print("-------SOMA DE TRÊS NÚMEROS-------")

def soma():
    num1 = float(input("\nDigite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    soma = num1 + num2 + num3
    return soma

print(f"A soma dos três números é {soma()}!")


# 4. Função com um argumento, que retorna o valor de caractere "P", se  for positivo, e "N", se  for zero ou negativo.
print("---------POSITIVO OU NEGATIVO---------")

def par_impar(n):
    if n > 0:
        return "P"
    else:
        return "N"

n = float(input("\nDigite um valor: "))
if par_impar(n) == "P":
    print(f"{n} é positivo!\n")
else:
    print(f"{n} é negativo!\n")


# 5. Função que informe a quantidade de dígitos de um determinado número inteiro informado. 
print("---------QUANTIDADE DE DÍGITOS---------")

numero = input("\nDigite um número inteiro: ")
def quant_digitos(numero):
    quant = len(numero)
    return quant

print(f"A quantidade de dígitos do número {numero} é {quant_digitos(numero)}!")


# 6. Função deve receber a % do aumento, salário atual e retornar o novo salário. 
print("-----------AUMENTO DE SALÁRIO DOS FUNCIONÁRIOS-----------")

def aumento_sal():
    salario = float(input("\nQual o seu salário atual? "))
    porcentagem = float(input("Qual a sua porcentagem de aumento (P.S.: digite em decimal)?  "))
    aumento = salario*porcentagem
    return salario, aumento

salario, aumento = aumento_sal()
print(f"O aumento é {aumento}, logo o seu novo salário é {salario + aumento} !\n")


# 7. Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (volume = (4/3)*pi*raio3).
print("--------------------VOLUME DE UMA ESFERA----------------------")

def volume_esfera():
    raio = float(input("\nDigite o valor do raio do círculo (em cm): "))
    volume = (4/3)*math.pi*raio
    return raio, volume

raio, volume = volume_esfera()
print(f"O volume da esfera com raio {raio} é {round(volume,4)} cm^3.\n")


#8. Função que recebe 3 notas de um aluno por parâmetro e uma letra. Se a letra for A, calcule a média aritmética,
#se for P, a sua média ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. 
print("--------------------MÉDIA DOS ALUNOS----------------------")
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
opcao = input("Opções do cálculo da média:\n\t'A' - Média Aritmética;\n\t'P' - Média Ponderada;\n\t'H' - Média Harmônica.\nEscolha uma opção: ")

def media(nota1,nota2,nota3,opcao):
    if opcao == "A":
        media = (nota1 + nota2 + nota3)/3
    elif opcao == "P":
        media = ((nota1*5) + (nota2*3) + (nota3*2))/10
    elif opcao == "H":
        media = (3 / ((1/nota1) + (1/nota2) + (1/nota3)))
    return media

print(f"A média é {media(nota1,nota2,nota3,opcao)}!\n")


# 9. Função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro (True) 
# caso o valor seja primo e Falso (False) em caso contrário.
print("--------------------NÚMERO PRIMO----------------------")

n = int(input("Digite um número inteiro e positivo: "))
def primo(n):
    mult = 0
    for count in range(2,n):
        if (n % count == 0):
            mult += 1 # isso quer dizer que ele é multiplo desse número
    if(mult == 0):
        return True
    else:
        return False

if primo(n) == True:
    print(f"O número {n} é primo!\n")
else:
    print(f"O número {n} não é primo!\n")


# 10. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
print("--------------------IDADE EM DIAS----------------------")

def idade_dias():
    anos = int(input("Digite quantos anos de vida vocês tem: "))
    meses = int(input("Digite quantos anos de vida vocês tem: "))
    dias = int(input("Digite quantos dias de vida vocês tem: "))
    idade_em_dias = anos*365 + meses*30 + dias
    return idade_em_dias

print(f"Sua idade média em dias é {idade_dias()}!\n")


# 11. Faça um procedimento que recebe a idade de um nadador por parâmetro e retorna , também por parâmetro, a categoria desse nadador
print("--------------------CATEGORIA NADADOR----------------------")

def categoria_nad():
    age = int(input("\nQual a idade do nadador? "))
    if 5 <= age <= 7:
        categoria = "Infantil A"
    elif 8 <= age <= 10:
        categoria = "Infantil B"
    elif 11 <= age <= 13:
        categoria = "Juvenil A"
    elif 14 <= age <= 17:
        categoria = "Juvenil B"
    elif age >= 18:
        categoria = "Adulto"
    return age, categoria

age, categoria = categoria_nad()
print(f"O nadador com {age} anos está na categoria {categoria}!\n")


# 12. Função que recebe a média final de um aluno por parâmetro e retorna o seu conceito
print("--------------------CONCEITO ALUNO----------------------")

med = float(input("\nQual a média final do aluno? "))
def conceito_aluno(med):
    if 0 <= med <= 4.9:
        conceito = "D"
    elif 5 <= med <= 6.9:
        conceito = "C"
    elif 7 <= med <= 8.9:
        conceito = "B"
    elif 9 <= med <= 10:
        conceito = "A"
    return med, conceito

media, conceito = conceito_aluno(med)
print(f"O aluno com média final {media} deve receber o conceito {conceito}!\n")


# 13. Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e retorna o seu peso ideal
print("--------------------PESO IDEAL BASEADO EM GÊNERO----------------------")
altura = float(input("\nDigite o valor da sua altura: "))
sexo = input("Digite o sexo, 'M' - para masculino e 'F' - para feminino: ")

def peso_ideal(altura,sexo):
    if sexo == "M":
        melhor_peso = (72.7*altura) - 58 #para o caso de ser homem
    else: 
        melhor_peso = (62.1*altura) - 44.7 #para o caso de ser mulher
    return melhor_peso

print(f"O peso idade para o sexo {sexo} é {round(peso_ideal(altura,sexo),2)}!\n")




