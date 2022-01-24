import matplotlib.pyplot as plt
import numpy as np

#1. Crie um gráfico pizza em Python para mostrar por dia da semana o número de frutas que uma pessoa comprou

y = np.array([12, 19, 21, 7, 14, 5, 8])
mylabels = ["Segunda", "Terça","Quarta","Quinta","Sexta","Sábado","Domingo"]

plt.pie(y, labels = mylabels)
plt.title("Quant. de frutas por dia da semana")
#plt.legend(title = "Legenda:")
plt.show() 


# 2. Crie um gráfico linha em Python para mostrar a relação da quantidade de litros de agua ingerido por calorias.

litros = np.array([4,2,5,1,3,6])
cal = np.array([140,120,122,150,130,175])

plt.plot(litros,cal)
plt.title("Relação quant. de litro x consumo de calorias")
plt.show() 