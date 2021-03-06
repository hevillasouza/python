# Importa as bibliotecas
from PyQt6 import uic, QtWidgets


def receber_num():
    num1 = float(formulario.txt_num1.text()) #para receber pelos usuarios o numero
    num2 = float(formulario.txt_num2.text())
    return num1, num2

def soma():
    num1, num2 = receber_num()
    soma = num1 + num2 
    formulario.lbl_saida.setText(f" = {soma}") # para aparecer o resultado na tela

def sub():
    num1, num2 = receber_num()
    sub = num1 - num2 
    formulario.lbl_saida.setText(f" = {sub}") # para aparecer o resultado na tela

def mult():
    num1, num2 = receber_num()
    mult = num1 * num2 
    formulario.lbl_saida.setText(f" = {mult}") # para aparecer o resultado na tela

def div():
    num1, num2 = receber_num()
    if num2 != 0:
        div = num1 / num2 
        formulario.lbl_saida.setText(f" = {round(div,4)}") # para aparecer o resultado na tela
    else:
        formulario.lbl_saida.setText("É impossível \nrealizar \na divisão!") # para aparecer o resultado na tela

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: formulário com os componentes, wuindow é a janela com form
Form, Window  = uic.loadUiType("tela.ui")

# Criar a Window() - Janela
window = Window()
#Criando o formulárop para ter acesso aos componentes
formulario = Form()
# Link janela e formulário
formulario.setupUi(window) 

formulario.btn_som.clicked.connect(soma) #chamando a função caso seja clicada
formulario.btn_sub.clicked.connect(sub)
formulario.btn_mult.clicked.connect(mult)
formulario.btn_div.clicked.connect(div)

window.show()
app.exec()
