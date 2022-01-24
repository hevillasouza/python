"""
1 - Faça uma função que verifique se um valor é perfeito ou não. Um valor é
dito perfeito quando ele é igual a soma dos seus divisores excetuando ele
próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve
retornar um valor booleano. (Use for pra ir de 1 até N,range…)
"""

print("--------------------NÚMERO PERFEITO----------------------")

n = int(input("Digite um número inteiro e positivo: "))

def num_perfeito(n):
    mult = 0
    soma = 0
    for count in range(1,n):
        if (n % count == 0):
            mult += 1 # isso quer dizer que ele é multiplo desse número
            soma = soma + count
    if soma == n:
        return True
    else:
        return False

print(num_perfeito(n))

"""
2 - Escreva um procedimento que recebes 3 valores reais X, Y e Z e que
verifique se esses valores podem ser os comprimentos dos lados de um
triângulo e, neste caso, retornar qual o tipo de triângulo formado. Para que X,
Y e Z formem um triângulo é necessário que a seguinte propriedade seja
satisfeita: o comprimento de cada lado de um triângulo é menor do que a
soma do comprimento dos outros dois lados. O procedimento deve identificar
o tipo de triângulo formado observando as seguintes definições:
Triângulo Equilátero: os comprimentos dos 3 lados são iguais.
Triângulo Isósceles: os comprimentos de 2 lados são iguais.
Triângulo Escaleno: os comprimentos dos 3 lados são diferentes.
"""

