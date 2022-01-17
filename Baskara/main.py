import math

#Crie um programa em Python que calcule as raizes reais de uma equação do segundo grau.
import delta

a = float(input("Digite o coeficiente da a: "))
b = float(input("Digite o coeficiente da b: "))
c = float(input("Digite o coeficiente da c: "))

print(f"\nA equação é {a}x^2 + {b}x + {c}")


if delta.del_ta(a,b,c) == 0:
        x = b/(2*a)
        print(f"\nEsse problema só tem uma raíz e ela é {x}!")
elif delta.del_ta(a,b,c) > 0:
    x1 = (b + math.sqrt(delta.del_ta(a,b,c)))/(2*a)
    x2 = (b - math.sqrt(delta.del_ta(a,b,c)))/(2*a)
    print(f"\nEssa equação tem duas raízes e elas são {x1} e {x2}!")
else:
    print("\n Esse problema não tem raízes reais, visto que delta é menor que zero!")
