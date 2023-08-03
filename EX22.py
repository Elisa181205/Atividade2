#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

n = int(input('Digite um numero: '))

if n % 2:
    print('{} é impar'.format(n))
else:
    print('{} é par'.format(n))