# Calculadora:
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

def soma(num1,num2):
    soma = num1 + num2
    return soma

def sub(num1,num2):
    sub = num1 - num2
    return sub

def mult(num1,num2):
    mult = num1 * num2
    return mult

def div(num1,num2):
    div = num1 / num2
    return div

print("---------OPÇÕES DE OPERAÇÕES----------")
print("+:Adição; -:Subtração; *:Multiplicação; /:Divisão")
operacao = input("De acordo com as opções acima, qual você deseja? ")

if operacao == "+":
    print(f"{num1} + {num2} == {soma(num1,num2)}")
elif operacao == "-":
    print(f"{num1} - {num2} == {sub(num1,num2)}")
elif operacao == "*":
    print(f"{num1} * {num2} == {mult(num1,num2)}")
elif operacao == "/":
    print(f"{num1} / {num2} == {div(num1,num2)}")
else:
    print("Operação inválida!")