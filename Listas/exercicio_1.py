# 1. Programa que peça dois números e imprima a soma.
print("------------------SOMA DE DOIS NÚMEROS----------------------")
num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))

soma = num1 + num2

print("A soma dos dois números é ",soma,"\n")

# 2. Programa que peça as 4 notas bimestrais e mostre a média.
print("--------------------MÉDIA DO ANO----------------------")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4)/4

print("A média do aluno é",media,"\n")

# 3. Programa que converta metros para centímetros
print("------------------METROS EM CENTÍMETROS----------------------")
med_met = float(input("Digite a medida em metros: "))

med_cent = med_met * 100

print("A medida convertida para centímetros é ",med_cent," cm.\n")

# 4. Programa que peça o raio de um círculo, calcule e mostre sua área
print("--------------------ÁREA DO CÍRCULO----------------------")
raio = float(input("Digite o valor do raio do círculo: "))

pi = 3.14
area = pi*(raio**2)

print(f"A área do círculo é {area}. \n") #aqui é para escrever na variável no canto que eu quero sem usar virgulas

# 5. Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
print("---------------------DOBRO ÁREA QUADRADO----------------------")
lado = float(input("Digite o valor do lado do quadrado: "))

area_quad =  lado ** 2

print("A área do quadrado é ",area_quad," e o dobro disso é ", area_quad*2,".\n")

# 6. Programa que calcule e mostre o total do seu salário no referido mês.
print("--------------------SALÁRIO MENSAL----------------------")
salario_hora = float(input("Digite o seu salário por hora: "))
horas =  float(input("Quantas horas que você trabalhou no mês: "))

salario_mensal = salario_hora * horas

print("O seu salário mensal será ",salario_mensal,".\n")

# 7. Programa que peça a temperatura em Fahrenheit, transforme em Celsius.
print("-------------------CONVERSÃO DE TEMPERATURA--------------------")
fahrenheit = float(input("Informe a temperatura em graus Fahrenheit: "))

celsius = 5 * ((fahrenheit-32)/9)

print("A temperatura em graus Fahrenheit convertida em graus Celsius é ",celsius,".\n")

# 9. Faça um Programa que peça 2 números inteiros e um número real, calcule
print("------------------OPERAÇÕES COM NÚMEROS----------------------")
int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite o número real: "))

first = (2*int1) * (int2/2)
second = (3*int1) + real
third = real ** 3

print("O produto do dobro do primeiro número com metade do segundo é ",first)
print("A soma do triplo do primeiro com o terceiro é ",second)
print("O terceiro número elevado ao cubo é ",third,"\n")

#10.  algoritmo que calcule seu peso ideal
print("--------------------PESO IDEAL----------------------")
altura_pessoa = float(input("Digite o valor da sua altura: "))

peso_ideal = (72.7*altura_pessoa) - 58

print("O seu peso ideal é ",peso_ideal,".\n")

# 11. Algoritmo que calcule seu peso ideal considerando o gênero
print("--------------------PESO IDEAL BASEADO EM GÊNERO----------------------")
altura_p = float(input("Digite o valor da sua altura: "))

melhor_peso_mulher = (62.1*altura_p) - 44.7 #para o caso de ser mulher
melhor_peso_homem = (72.7*altura_p) - 58 #para o caso de ser homem

print("Se você for mulher, o seu peso ideal é ",melhor_peso_mulher,".\nCaso você seja homem, seu peso ideal é ",melhor_peso_homem,". \n")


