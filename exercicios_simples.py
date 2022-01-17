"""
# seria para setar as respostas em português
import locale
locale.setlocale(locale.LC_ALL, "pt_br")
"""



"""
# Exercícios frutas
salada_frutas = ["Maça","Laranja","Uva","Mamão","Melão"]
print("A lista inicial é",salada_frutas)
salada_frutas.append("Morango")
salada_frutas.remove("Maça")
salada_frutas[1] = "Banana"
print("A lista final é", salada_frutas,"\n")

# Exercícios nomes
dados = [["Carla",23,"Feminino",1998],["Maria",18,"Feminino",2003],["José",25,"Masculino",1996],["Paula",14,"Feminino",2007]]
print("Os dados são:\n",dados[0],"\n",dados[1],"\n",dados[2],"\n",dados[3])

#1 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.
nome = input("Qual o seu nome? ")

while True:
    senha = input("Qual a sua senha? ")
    if senha == nome:
        print("Senha inválida, por favor corrija a informação! ")
    else:
        print("Senha válida!")
        break

# 2. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
print("----------------ÍMPARES DE 1 A 50---------------------")
b = 1
while b <= 50:
    if b % 2 != 0:
        print(b)
    b = b + 1

# Teste função
num1 = float(input("Digite o valor do primeiro número: "))
num2 = float(input("Digite o valor do segundo número: "))
num3 = float(input("Digite o valor do terceiro número: "))

def somatorio(n1,n2,n3):
    soma = n1 + n2 + n3
    return soma

print("A soma é",somatorio(num1,num2,num3))


# Quantidade de números pares
lista = [1,2,3,2,1,2,3,4,5,6,5,4,3,2,1,8,10,12]

def quant_pares(lista):
    cont = 0
    for i in lista:
        if i % 2 == 0:
            cont += 1
    return cont

print("A lista é",lista)
print("A quantidade de números pares é",quant_pares(lista),"!")


# dizer o dia da semana que nasceu
import datetime

dia = int(input("Qual o dia que você nasceu? "))
mes = int(input("Qual o mês que você nasceu? "))
ano = int(input("Qual o ano que você nasceu? "))

data_nasc = datetime.datetime(ano,mes,dia)

print("\nVocê nasceu no dia da semana:",data_nasc.strftime("%A"))
"""

