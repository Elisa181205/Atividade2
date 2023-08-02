#Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("insira o segundo número:"))

if num1>num2:
    print("{} é maior que {}".format(num1,num2))
else:
    if num1<num2:
        print("{} é maior que {}".format(num2,num1))
    else:
        print("Os números são iguais")