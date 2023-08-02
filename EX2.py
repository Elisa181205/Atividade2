#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Por favor, insira um número: "))
print() # pula linha para melhorar a apresentação do resultado.
if valor < 0 :
    print ("O número é negativo.")
else:
    if valor == 0 :
        print("o número é igual a 0")
    else:
        print("O número é positivo")