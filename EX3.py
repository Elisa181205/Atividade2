#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe seu genero com F ou M : ")
if sexo =="F":
    print("F - Feminino")
else:
    if sexo=="M":
        print ("M - Masculino" )
    else:
        print("Sexo invalido, tente novamente.")