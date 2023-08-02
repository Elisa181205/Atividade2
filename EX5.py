#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2
#Calcula-se a media aritmetica das notas e armazena na variavel 'media'
if media >=7 and media <=9 :
    print ("Aprovado") #Se o valor da media estiver entre 7 e 9, imprime Aprovado
else:
    if media <7:
        print("Reprovado")
    else:
        if media == 10:
            print("Aprovado com distincão!")