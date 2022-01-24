# Importação da lib tkinter
from tkinter import *
class Application:
    def __init__(self, master=None):
        
        #criação dos containes
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        #texto para printar calculadora
        self.titulo = Label(self.container1, text="CALCULADORA")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # para printar o texto na lateral "num 1"
        self.lbl_num1 = Label(self.container1, text="Número 1: ")
        self.lbl_num1["font"] = ("Arial", "10", "bold")
        self.lbl_num1.pack(side=LEFT)

        # colocando o espaço onde o usuário vai colocar o numero 1
        self.txt_num1 = Entry(self.container1)
        self.txt_num1["width"] = 30
        self.txt_num1["font"] = ("Arial", "10", "bold")
        self.txt_num1.pack(side=LEFT)

        # para printar o texto na lateral "num 2"
        self.lbl_num2 = Label(self.container2, text="Número 2: ")
        self.lbl_num2["font"] = ("Arial", "10", "bold")
        self.lbl_num2.pack(side=LEFT)

        # # colocando o espaço onde o usuário vai colocar o numero 2
        self.txt_num2 = Entry(self.container2)
        self.txt_num2["width"] = 30
        self.txt_num2["font"] = ("Arial", "10", "bold")
        self.txt_num2.pack(side=LEFT)

        # criando o botao soma
        self.bnt_soma = Button(self.container3)
        self.bnt_soma["text"] = "+"
        self.bnt_soma["font"] = ("Calibri", "10","bold")
        self.bnt_soma["width"] = 5
        self.bnt_soma["command"] = self.soma
        self.bnt_soma.pack(side=LEFT)

        # criando o botao de subtração
        self.bnt_sub = Button(self.container3)
        self.bnt_sub["text"] = "-"
        self.bnt_sub["font"] = ("Calibri", "10","bold")
        self.bnt_sub["width"] = 5
        self.bnt_sub["command"] = self.sub
        self.bnt_sub.pack(side=LEFT)

        # criando o botao de multiplicação
        self.bnt_mult = Button(self.container3)
        self.bnt_mult["text"] = "*"
        self.bnt_mult["font"] = ("Calibri", "10","bold")
        self.bnt_mult["width"] = 5
        self.bnt_mult["command"] = self.mult
        self.bnt_mult.pack(side=LEFT)

        # criando o botao de divisão
        self.bnt_div = Button(self.container3)
        self.bnt_div["text"] = "/"
        self.bnt_div["font"] = ("Calibri", "10","bold")
        self.bnt_div["width"] = 5
        self.bnt_div["command"] = self.div
        self.bnt_div.pack(side=LEFT)

        # criando o texto para o resultado
        self.lbl_resultado = Label(self.container4, text="")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()

    def soma(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        soma = num1 + num2
        self.lbl_resultado["text"] = f"{num1} + {num2} = {soma}"

    def sub(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        sub = num1 - num2
        self.lbl_resultado["text"] = f"{num1} - {num2} = {sub}"

    def mult(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        mult = num1 * num2
        self.lbl_resultado["text"] = f"{num1} * {num2} = {mult}"

    
    def div(self):
        num1 = float(self.txt_num1.get())
        num2 = float(self.txt_num2.get())
        if num2 != 0:
            div = num1 / num2
            self.lbl_resultado["text"] = f"{num1} / {num2} = {div}"
        else:
            self.lbl_resultado["text"] = f"Como o segundo número é 0, é impossível realizar a divisão!"

root = Tk()
Application(root)
root.mainloop()