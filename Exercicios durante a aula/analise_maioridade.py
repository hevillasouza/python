# Análise de maioridade

ano = int(input("Digite o ano que você nasceu: "))

idade = 2022 - ano

print("\nA sua idade é",idade,"anos.")
if idade >= 18:
    print("VOCÊ É MAIOR DE IDADE!")
else:
    print("VOCÊ É MENOR DE IDADE!")
