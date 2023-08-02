#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print("1 - M - Matutino")
print("2 - V - Vespertino")
print("3 - N - Noturno")

turno = input("Escolha uma das opções acima:")

if turno=="1":
    print ("Bom dia!")
else:
    if turno=="2":
        print('Boa tarde!')
    else:
        if turno=="3":
            print ('Boa noite')
        else:
            print (f'Opção inválida! Digite novamente.')