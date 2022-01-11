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

"""




