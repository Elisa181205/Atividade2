#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario = float(input("Informe o valor do salário"))
if salario <= 280 and salario >= 0:
    porcentagem = 20
    aumento= salario*0.2
    novo_salario = salario+aumento
    print("Antigo salário {}, percentual de aumento {}, Valor do Aumento {}, Novo salário {}".format(salario,porcentagem,aumento,novo_salario))
else:
    if salario > 280 and salario <=700:
        porcentagem = 15
        aumento= salario*0.15
        novo_salario = salario+aumento
        print("Antigo salário {}, percentual de aumento {}, Valor do Aumento {}, Novo salário {}".format(salario,porcentagem,aumento,novo_salario))
    else:
        if salario>700 and salario<=1500:
            porcentagem = 10
            aumento= salario * .10
            novo_salario = salario + aumento
            print("Antigo salário {}, percentual de aumento {}, Valor do Aumento {}, Novo salário {}".format(salario,porcentagem,aumento,novo_salario))

        elif salario>=1500:
            porcentagem = 5
            aumento= salario*.05
            novo_salario = salario + aumento
            print("Antigo salário {}, percentual de aumento {}, Valor do Aumento {}, Novo salário {}".format(salario,porcentagem,aumento,novo_salario))
