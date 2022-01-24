import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

app = QApplication(sys.argv)

janela = QWidget()
janela.resize(500,500)
janela.setWindowTitle("Programa 123")

lbl_texto = QLabel("Bem-vind@!", janela)
lbl_texto.setGeometry(20, 10, 100, 16)

lbl_nome = QLabel("Nome: ", janela)
lbl_nome.setGeometry(20, 40, 100, 16)

janela.show()
app.exec()
