# Importando a biblioteca TK
from tkinter import *

# Criando a tela
class Tela:
    # definindo o construtor padrão
    #  receber a master root do TK
    def __init__(self, master=None):
        #criando o conteiner 1
        self.container1 = Frame(master)
        # registrando o conteiner 
        self.container1.pack()

        # criar um widget e adicionar ao container
        self.msg = Label(self.container1, text = "Bem vind@!") #o primeiro termo é para associar a mensagem a esse conteiner1 e label é para escrever texto na tela
        self.msg["font"] = ("Verdana", "10", "italic", "bold") # aqui é para formatar o texto
        # registrando o widget
        self.msg.pack ()

        # criando o botão (widget) de sair
        self.sair = Button(self.container1) # ese comando é para criar um botão
        self.sair["text"] = "Sair" # o texto que vai aparecer
        self.sair["font"] = ("Calibri", "10") # formatando
        self.sair["width"] = 5 # largura do botão
        self.sair["command"] = self.container1.quit # o comando que o widget vai executar
        self.sair.pack () # registrando

        # criando o botão (widget) de cadastrar
        self.cadastrar = Button(self.container1, text = "Cadastrar") # ese comando é para criar um botão
        self.cadastrar["font"] = ("Calibri", "10") # formatando
        self.cadastrar["width"] = 10 # largura do botão
        # chamando a função
        self.cadastrar["command"] = self.cadastrar # o comando que o widget vai executar
        self.cadastrar.pack () # registrando

        # criar uma nova label
        self.resultado = Label(self.container1, text = "") #o primeiro termo é para associar a mensagem a esse conteiner1 e label é para escrever texto na tela
        self.resultado["font"] = ("Verdana", "10", "italic", "bold") # aqui é para formatar o texto
        # registrando o widget
        self.resultado.pack ()

    def cadastrar(self):
        print("Clicou em cadastrar!")

# Criar um objetivo do tipo TK para construir a tela
root = Tk()

# Passando o root (obejtivo do tipo TK) para a minha classe
Tela(root)

# Criando o evento loop para ficar verificando se o evento foi acionado
root.mainloop()