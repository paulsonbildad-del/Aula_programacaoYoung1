#Requisitos funcionais

# Monstrar o numero de tentativas restantes
# Monstrar letras acertadas
#permitir vencer
#permitir perde
#apenas aceitar una letra por tentativa
#impedir que a mesma letra seja digitada novamente

#requisitos funcionais opcionais


palavra_secreta = "python"
letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0 :
    
    palavra_formada = ""

for letra in palavra_secreta: 

    if letra in letras_certas: 
        palavra_formada += letra

    else:palavra_formada += "-"

 
