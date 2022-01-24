# Importa as bibliotecas
from PyQt6 import uic, QtWidgets
import pandas as pd
import numpy as np

banco = read.csv


def enviar():
    titulo = formulario.txt_titulo.text() #para receber pelos usuarios o numero
    email = formulario.txt_email.text()
    reclamacao = formulario.txt_recl.text()
    
    # Motando a linha
    linha = {'Titulo': titulo,
            'Email': email,
            'Reclamacao': reclamacao}

    # Adicionando no banco
    banco.append(linha, ignore_idex = True)

    # Listar banco

def listar():
    pass
    
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

formulario.btn_enviar.clicked.connect(soma) #chamando a função caso seja clicada
formulario.btn_listar.clicked.connect(sub)


window.show()
app.exec()