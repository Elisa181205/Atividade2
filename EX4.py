#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Insira uma letra: ")

if letra =="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U" or letra =="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print(f"{letra} é vogal")  # A, E ou I
else:
    print("É consoante")