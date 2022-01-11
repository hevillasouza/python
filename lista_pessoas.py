"""
lista_pessoas = [
    ["Mario", "Carvalho", "Campo Grande", 1997, 85],
    ["Pedro", "Campos", "Campo Grande", 1994, 78],
    ["Elisa", "Vitória", "Campo Grande", 2000, 45],
]

print(lista_pessoas[0])
"""
# Crie um programa para cadastrar N pessoas.
# Adicione em uma lista e imprima npo final.
n = int(input("Quantas pessoas deseja cadastrar: "))
lista_pessoas = []
for indice in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    endereco = input("Digite a cidade que você mora: ")
    peso = float(input("Digite o seu peso em kg: "))
    nova_pessoa = [nome, idade,endereco,peso]
    lista_pessoas.append(nova_pessoa)
else:
    print("O cadastro de pessoas foi finalizado!")


for pessoa in lista_pessoas:
    print(f"Bem-vin@ {pessoa[0]}, você tem {pessoa[1]} anos, mora na cidade {pessoa[2]} e o seu peso é {pessoa[3]}!")
    if pessoa[1] >= 18:
        print("Você é maior de idade!")
    else:
        print("Você é menor de idade!")
else:
    print("A listagem de pessoas foi finalizado!")

print("Quantidade de pessoas cadastradas: ", len(lista_pessoas))