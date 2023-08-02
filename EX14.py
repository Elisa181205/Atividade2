#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

nota1 = float(input("Insira a primeira nota : "))
nota2 = float(input("Insira a segunda nota : "))
media= (nota1+nota2)/ 2.0 #arredondamento para baixo
print ("A média é", media)
if media >9 :
    print ("Suas notas foram:\n {} e {}\n sua média foi de {}\n e você foi APROVADO".format(nota1,nota2,media))
else:
    if media >7.5 and media<=9:
        print ("Suas notas foram:\n {} e {}\n sua média foi de {}\n e você foi APROVADO".format(nota1,nota2,media))
    else:
        if media> 6 and media<=7.5:
            print ("Suas notas foram:\n {} e {}\n sua média foi de {}\n e você foi APROVADO".format(nota1,nota2,media))
        else:
            if media >4 and media <6:
                    print ("Suas notas foram:\n {} e {}\n sua média foi de {}\n e você foi REPROVADO".format(nota1,nota2,media))

            else:
                    print ("Suas notas foram:\n {} e {}\n sua média foi de {}\n e você foi REPROVADO".format(nota1,nota2,media))
