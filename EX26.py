"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""
print("\n Digite 1 para Gasolina e 2 para Álcool")
litro = float(input("Informe a quantidade de litros: "))
tipo = int(input("Gasolina ou Álcool ?"))
total = 0
if tipo ==1:
    if litro <=20:
        desc = 4/100
        total1= (litro*2.5)
        total = total1-(total1*desc)
        print("O valor a ser é de: R${}".format(total))
    else :
        desc = 6/100
        total1= (litro*2.5)
        total = total1-(total1*desc)
        print("O valor a ser é de: R${}".format(total))
else:
    if litro<=20:
        desc =  3 /100
        total=(litro * 1.90 )-((litro)*desc)
        print ("O valor a ser pago será de {}".format(total ))
    elif litro >20:
        desc =   5/100
        total =(litro * 1.9)- ((litro )*desc)
        print ("O valor a ser pago será de {} ". format(total))