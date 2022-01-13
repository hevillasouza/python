import geometria

print("-----------CALCULADORA DE ÁREA DE FORMAS GEOMÉTRICAS--------\n")
print("1 - área do círculo, 2 - área do quadrado")
opcao = int(input("Escolha uma das opções acima: "))

if opcao == 1:
    raio = float(input("\nQual o tamanho do raio em cm? "))
    print(f"A área do círculo é {geometria.area_circulo(raio)} cm")
elif opcao == 2:
    lado = float(input("\nQual o tamanho do lado em cm? "))
    print(f"A área do quadrado é {geometria.area_quadrado(lado)} cm")
else:
    print("Opções inválidas!")
