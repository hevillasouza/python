from tkinter import *
import funcao_delta as d
import math 

class Application:
    def __init__(self, master=None):
        
        #criação dos containes
        self.container1 = Frame(master)
        self.container1["pady"] = 12
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 10
        self.container2["padx"] = 30 # para ter um espaço maior para a largura
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["pady"] = 15
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["pady"] = 10
        self.container4.pack()

        #texto para printar o título
        self.titulo = Label(self.container1, text="Calculadora de equação de 2° grau")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #texto para printar a destrição
        self.titulo = Label(self.container2, text="entre com os valores dos coeficinetes da equação")
        self.titulo["font"] = ("Arial", "8", "bold")
        self.titulo.pack()

        # para printar as variáveis
        self.lbl_a = Label(self.container2, text="a:")
        self.lbl_a["font"] = ("Arial", "10")
        self.lbl_a.pack(side=LEFT)

        # colocando o espaço onde o usuário vai colocar o coeficiente a
        self.txt_a = Entry(self.container2)
        self.txt_a["width"] = 10
        self.txt_a["font"] = ("Arial", "10")
        self.txt_a.pack(side=LEFT)

        # para printar as variáveis
        self.lbl_b = Label(self.container2, text="b:")
        self.lbl_b["font"] = ("Arial", "10")
        self.lbl_b.pack(side=LEFT)

        # colocando o espaço onde o usuário vai colocar o coeficiente a
        self.txt_b = Entry(self.container2)
        self.txt_b["width"] = 10
        self.txt_b["font"] = ("Arial", "10")
        self.txt_b.pack(side=LEFT)

        # para printar as variáveis
        self.lbl_c = Label(self.container2, text="c:")
        self.lbl_c["font"] = ("Arial", "10")
        self.lbl_c.pack(side=LEFT)

        # colocando o espaço onde o usuário vai colocar o coeficiente a
        self.txt_c = Entry(self.container2)
        self.txt_c["width"] = 10
        self.txt_c["font"] = ("Arial", "10")
        self.txt_c.pack(side=LEFT)

        # criando o botao de calcular
        self.bnt_calc = Button(self.container3)
        self.bnt_calc["text"] = "Calcular"
        self.bnt_calc["font"] = ("Calibri", "12","bold")
        self.bnt_calc["width"] = 10
        self.bnt_calc["command"] = self.calc
        self.bnt_calc.pack(side=LEFT)

        # criando o texto para o resultado
        self.lbl_resultado = Label(self.container4, text="")
        self.lbl_resultado["font"] = ("Arial", "10")
        self.lbl_resultado.pack()
   
    def calc(self):
        a = float(self.txt_a.get())
        b = float(self.txt_b.get())
        c = float(self.txt_c.get())

        delta = d.del_ta(a,b,c)

        if delta == 0:
            x = b/(2*a)
            self.lbl_resultado["text"] = f"A equação só tem uma raíz: {x}!"
        elif delta > 0:
            x1 = (b + math.sqrt(delta))/(2*a)
            x2 = (b - math.sqrt(delta))/(2*a)
            self.lbl_resultado["text"] = f"A equação tem duas raízes: {x1} e {x2}!"
        else:
            self.lbl_resultado["text"] = "Esse problema não tem raízes reais, visto que delta é menor que zero!"


root = Tk()
Application(root)
root.mainloop()