
#operador maior ou menor e igual ou maior e maior e maior ou igual
# > operador maior
# <operador maior
# >= operador maior ou igual
# <operador menor ou igual


print(10 > 10) #Falso, 10 nao e maior que 10
print(10 >= 10) #True, 10 e maior ou igual a 10
print(1.1 > 10) #True, 1.1 e maior que 1

print(10 < 10) #Falso, 10 nao e maior que 10
print(10 <= 10) #True, 10 e maior ou igual a 10
print(1.1 <= 10) #True, 1.1 nao e maior ou igual a 1



#operador de comparacao ==

#o moperador == server para comparacao do primeiro VALOR com o segundo  
#VALOR diferente do = que serve para atribuicao

print(10.0 == 10)                           #True
print("nome@gmail.com" == "nome@cna.com")   #False
print(9.1 == 9)                             #False

#Operador de Diferença !=

#Ele e utilizado para verificar se o primeiro valor e DIFERENTE
#do segundo valor, retornando sempre TRUE ou FALSE

print(10.0 != 10)                   #True
print("professor" != "professor")   #False
print(09.1 != 9)                    #False   


#Estruturas Condicionais

#if que significa SE
# eslse que significa SE NAO
# eslse if que significa SE NAO SE

if  True:
    print("teste")#Como retornou VERDADEIRO o bloco de código executa


if  False:
    print("teste")#Como retornou FALSO o bloco de código NAO executa

#Exemplo 1

teste = True

if teste:
    print("É Verdadeiro")

teste = False

if teste:
    print("È Verdadeiro")


#Exemplo 2

teste = input("Você ja bricou com fogo?") # Input sempre retornar um string

if teste == "sim":
    print("Entao já se queimou : ()")

else:
    print("Então não brinque se não vai se queimar.")

#Exemplo 3  
#IF aninhado quando a primeira condicao do primeiro if
#precisa ser VERDADEIRO para que os demais IF dentro dele
#sejam executados

idade = 17
tem_documento = True
pagou_ingresso = True

if idade  >=18 :
    print("é maior de idade.")

    if tem_documento:
        print("apresentou um documento.")

        if pagou_ingresso:
            print("Entrada permitida.")

print()
print("Exemplo if independentes:")
print()


#IF INDEPENDENTES, quando um if não depende dos outros ser verdadeiro
#para ser executado


if idade  >=18 :
    print("é maior de idade.")

if tem_documento:
    print("apresentou um documento.")
        
if pagou_ingresso:
    print("Entrada permitida.")

#Estrutura de condicional ELIF

teste = input("Você ja bricou com fogo?") # Input sempre retornar um string

if teste == "sim":
    print("Entao já se queimou : ()")

elif teste == "talves":
    print("Então não brinque se não vai se queimar.")

else:
    print("Então não brinque se não vai se queimar.")


#Operadores Logicos not"Não" , or"OU", and"E"

# not = not
# or = ||ou|
# and = && ou &

estudante = True
print(not estudante)          		#Não é estudante? Não (False)

proplayer = True
print(not proplayer)         		 #Não é pro player? Não (False)

maior_de_idade = False
print(not maior_de_idade)     		#Não é maior de idade? Sim (True)

goku_venceria_madoka = False
print(not goku_venceria_madoka)  	#Goku não venceria a Madoka? Sim (True)


#Operador OR

True or False		# -> True

True or True		# -> True

False or False		# -> False

10 >= 10 or 1 > 2	# -> True, a primeira condição é verdadeira

10 < 10 or 1 > 2	# -> False, ambas condições são falsas

#Operador And

True and False	# -> False

True and True		# -> True

False and False	# -> False

10 >= 10 and 1>2	# -> False, a segunda condição é falsa

10 < 11 and 1 < 2	# -> True, ambas condições são verdadeiras

#Exemplo 4 - Atividade Pratica

coral = True

print("treinamento Iniciado")

Resposta = input("A cobra Registrada no sistema é uma coral verdadeira")

if coral == True and Resposta == "s" or Resposta == "S" or Resposta == "yes" or Resposta == "sim":
    print("Identificacao correta")

else:
    print("Indetificacao! Incorreta!")


Coral = False

print("treinamento Iniciado")

Resposta = input("A cobra Registrada no sistema é uma coral Falso? s/n")

if Coral == False and Resposta == "s" or Resposta == "S" or Resposta == "yes" or Resposta == "sim":
    print("Indetificacao! Incorreta!")

else:
    print("Identificacao correta")

    
