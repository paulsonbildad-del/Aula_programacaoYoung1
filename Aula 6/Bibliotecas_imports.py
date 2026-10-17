#importando bibliotecas:
#import "nome da bibliotecas"
#ou
#from "nome biblioteca" import "funcao especifica"
import matplotlib.pyplot as plt 
"""


dados_x = ["Personagem 1", "Personagem 2", "Personagem 3"]

dados_y = [100, 150, 10_00]



plt.title("Titulo do Gráfico")

plt.xlabel("Dados X")

plt.ylabel("Dados Y")

plt.bar(dados_x, dados_y)# bar = tipo do gráfico (gráfico de barras)

plt.show()
"""
"""
linguagens = ["python", "java", "c++", "javascript"]
alunos = [15,10,12,8]

plt.bar(linguagens, alunos)
plt.title("Alunos por linguagen")
plt.xlabel("Linguagen")
plt.xlabel("Quantidade de alunos")

plt.show()
"""

"""
dias_da_semana = ["segunda", "terça", "quarta", "quinta", "sexta"]
vendas = [410,360,120,300,900]

plt.bar(dias_da_semana, vendas)
plt.title("vendas por dias")
plt.xlabel("Dias da semana")
plt.xlabel("Quantidade de vendas")

plt.show()
"""

"""
import qrcode

texto = "Estou apprendendo python na melhor turma"

imagem = qrcode.make(texto)

imagem.save("qrcode.png")
"""

import cv2

image = cv2.imread("image.jpg")

image_cinza = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("image_cinza",image_cinza)

cv2.waitKey(0)

cv2.destroyAllWindows()