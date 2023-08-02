#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input('Digite aqui o numero do DIA: '))
if dia==1:
    print("Domingo")
else:
    if dia == 2: 
            print("{}-Segunda".format(dia))

    else:
        if dia ==3:
                print("{}-Terça".format(dia))

        else:
            if dia ==4:
                     print("{}-Quarta".format(dia))

            else:
                if dia ==5:
                        print("{}-Quinta".format(dia))

                else:
                    if dia ==6:
                              print("{}-Sexta".format(dia))

                    else:
                        if dia ==7:
                                  print("{}-Sábado".format(dia))

                        else:
                            print("Valor inválido")