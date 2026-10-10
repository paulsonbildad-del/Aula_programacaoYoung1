#Funcoes e parametros

def ola():
    print("olá")

ola()


def comprimentar(nome):
    print("olá", nome)

comprimentar("Matheus")


#return retornar o valor do algoritmo que é a soma dos valores no parametro
#porém NÂO imprimi por isso é nessario utilizar o print com a funcão como parametropara exibir o resultados
def somar_valores(valor1,valor2):
    soma=valor1 + valor2

    return soma


print(somar_valores(10,20))


#Apos o return a funcao se encerra ignorando qualquer codigo em baixo return dentro da funcao
def subitrair_valores(valor1,valor2):
    soma = valor1 - valor2

    print(soma)

    soma2 = valor1 + valor2

    print(soma2)

    return soma

    soma3 = valor1 + valor2

    print(soma3)

subitrair_valores(50,26)



