# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
import delta as d
import math

def baskara():
    a = float(formulario.txt_a.text()) #para receber pelos usuarios o numero
    b = float(formulario.txt_b.text())
    c = float(formulario.txt_c.text())
    delta = d.del_ta(a,b,c)
    if delta == 0:
        x = -b/(2*a)
        formulario.lbl_saida.setText(f"\nEsse problema só tem uma raíz e ela é {x}!") # para aparecer o resultado na tela
    elif delta > 0:
        x1 = (b + math.sqrt(delta))/(2*a)
        x2 = (b - math.sqrt(delta))/(2*a)
        formulario.lbl_saida.setText(f"\nEssa equação tem duas raízes e elas são {x1} e {x2}!")
    else:
        formulario.lbl_saida.setText("\n Esse problema não tem raízes reais, visto que delta é menor que zero!")

# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: formulário com os componentes, wuindow é a janela com form
Form, Window  = uic.loadUiType("Baskara_pyqt/tela.ui")

# Criar a Window() - Janela
window = Window()
#Criando o formulárop para ter acesso aos componentes
formulario = Form()
# Link janela e formulário
formulario.setupUi(window) 

formulario.bnt_res.clicked.connect(baskara) #chamando a função caso seja clicada, deve ser sem os "()"

window.show()
app.exec()
