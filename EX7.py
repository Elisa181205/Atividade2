#Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = int (input('digite um número:'))
num2 = int (input('digite o segundo número:'))
num3 = int (input('digite o terceiro número:'))

lista = [num1, num2, num3]
print("o maior número é",max(lista),"e O menor número é",min(lista))
