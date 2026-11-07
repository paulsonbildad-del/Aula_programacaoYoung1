
#codigo utilizado para crir e escrever un arquivo txt

""" with open("dados.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Escrevendo um arquivo em Python!!!")
 """

#codigo utilizado para ler o arquivo


""" with open("dados.txt", "r") as arquivo:
    texto = arquivo.read();
    print(texto) """

#Codigo para adicionar texto ao arquivo

with open("dados.txt", "a", encoding= "utf-8") as arquivo:
    arquivo.write("\n") # Adicionando uma quebra linha
    arquivo.write("Adicionaado mais Texto")