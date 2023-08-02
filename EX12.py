#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#Salário Bruto: (5 * 220)        : R$ 1100,00
#(-) IR (5%)                     : R$   55,00  
#(-) INSS ( 10%)                 : R$  110,00
#FGTS (11%)                      : R$  121,00
#Total de descontos              : R$  165,00
#Salário Liquido                 : R$  935,00
horas = float(input("Digite a qtd de horas trabalhadas: "))
valor = float(input("Digite o valor da sua hora: "))
salario = horas*valor

if salario <=900:
    print('\nO valor do seu salário é {} e você não recebe nenhum desconto.'.format(salario))
else:
    if salario <=1500:
        ir=(salario*0.05)
        inss =(salario*0.1)
        sindicato =(salario*0.03)
        fgts = (salario*0.11)
        descontos= ir+inss
        liquido = salario-descontos
        print('\n O Salario bruto: ({}*{}) : R$ {} \n (-) IR (5%) : R${} \n (-) INSS (10%) \n FGTS (11%) : R${}\n total de Descontos :{} \n Salário Liquido: R${}'.format(horas,valor,salario,ir,fgts,descontos,liquido))

    else:
        if salario <=2500:
            ir=(salario*0.2)
            inss =(salario*0.1)
            sindicato =(salario*0.03)
            fgts = (salario*0.11)
            descontos= ir+inss
            liquido = salario-descontos
            print('\n O Salario bruto: ({}*{}) : R$ {} \n (-) IR (5%) : R${} \n (-) INSS (10%) \n FGTS (11%) : R${}\n total de Descontos :{} \n Salário Liquido: R${}'.format(horas,valor,salario,ir,fgts,descontos,liquido))

            if salario >=2500:
                ir=(salario*0.2)
                inss =(salario*0.1)
                sindicato =(salario*0.03)
                fgts = (salario*0.11)
                descontos= ir+inss
                liquido = salario-descontos
                print('\n O Salario bruto: ({}*{}) : R$ {} \n (-) IR (5%) : R${} \n (-) INSS (10%) \n FGTS (11%) : R${}\n total de Descontos :{} \n Salário Liquido: R${}'.format(horas,valor,salario,ir,fgts,descontos,liquido))
