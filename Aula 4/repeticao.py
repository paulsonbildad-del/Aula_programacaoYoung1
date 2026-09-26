#listas

alunos = ["pietro", "paul", "davi", "professor matheus"]

print("Lista Original: ", alunos)

alunos.append("tiago") # adiciona um novo valor a variavel do tipo lista

print()#Serva para criar um espaço acima

print("Lista apos metodo append: ", alunos)

alunos.remove("professor matheus")

print("-"*150)#Serva para criar linhas pelo numero vezes multiplicado

print("Lista apos metodo remove: ", alunos)

print("-"*150)#Serva para criar linhas pelo numero vezes multiplicado

alunos.sort()  # Ordem Crescente
print("Lista apos metodo sort: ", alunos)

print("-"*150)#Serva para criar linhas pelo numero vezes multiplicado
print(len(alunos)) # funçao len funciona para ler a quantidade de dados dentro da lista ou outros metodos


print("-"*150)#Serva para criar linhas pelo numero vezes multiplicado

contador = 0

while  contador < 3: # repete enquanto a condicao for verdadeira exemplo o valor da variavel contador é menor que 3 se sim a repetição continuara até 
    print(contador)
    contador = contador + 1

print("-"*150)#Serva para criar linhas pelo numero vezes multiplicado
for alunos in ["pietro", "paul", "davi", "professor matheus"]:

    print(alunos)


for contador in range(10):

    if contador == 3:

        print("O passo 3 será pulado :P")

        continue



    print("Degrau:", contador)