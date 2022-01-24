# Importa as bibliotecas
from PyQt6 import uic, QtWidgets

def boas_vindas():
    nome = formulario.txt_nome.text()
    # para aparecer o resultado na tela
    formulario.lbl_result.setText(f"Bem-vind@ {nome}!")


# Criando a aplicação princial
app = QtWidgets.QApplication([])

# Carrego a ui - Link
# Retorna: formulário com os componentes, wuindow é a janela com form
Form, Window  = uic.loadUiType("Boas_vindas/tela.ui")

# Criar a Window() - Janela
window = Window()
#Criando o formulárop para ter acesso aos componentes
formulario = Form()
# Link janela e formulário
formulario.setupUi(window) 

formulario.btn_enviar.clicked.connect(boas_vindas)

window.show()
app.exec()