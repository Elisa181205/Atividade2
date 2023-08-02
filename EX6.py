#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Digite primeiro número: "))
n2 = int(input("Digite segundo número: "))
n3 = int(input("Digite terceiro número: "))
if (n1 > n2) and (n1 > n3):
    print("{} é o Maior".format(n1))  # Verificando qual dos dois foram os maiores, para imprimir na tela.
else:
    if(n2 > n1) and (n2 > n3):
        print("{} é o Maior.".format(n2))
    else :
        if (n3>n1 )and (n3>n2 ):
            print ("{} é o Maior ". format(n3 ))   #Verifica se    apenas o último valor digitado foi o maior    ou não.
            print ("{} É O MAIORES ". format(n3 ))
            