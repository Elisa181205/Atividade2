#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
preco1 = float(input('Digite o primeiro valor: '))  #
preco2 = float(input('Digite o segundo valor: '))
preco3 = float(input('Digite o terceiro valor: '))

lista = [preco1,preco2,preco3]

print("O mais barato é:",min(lista))