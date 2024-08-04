#Crie um programa que faça o computador jogar Jokenpô com você.
# pedra 'quebra' a tesoura; tesoura 'corta' o papel e papel 'embrulha' a pedra.

from random import choice
from time import sleep


opcoes = ('PEDRA','PAPEL','TESOURA')

print("-="*24)

usuario = str(input("PEDRA, PAPEL ou TESOURA? ")).upper()

pc = choice(opcoes)

print("\nVocê escolheu {} e o computador escolheu {}\n".format(usuario, pc))
print("-="*24)

if usuario == 'PEDRA':
    if pc == 'PEDRA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("EMPATE!")
    elif pc == 'PAPEL':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Computador ganhou!")
    elif pc == 'TESOURA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Você ganhou!") 
elif usuario == 'PAPEL':
    if pc == 'PAPEL':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Empate!")
    elif pc == 'PEDRA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Você ganhou!")
    elif pc == 'TESOURA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Computador ganhou!")
elif usuario == 'TESOURA':
    if pc == 'TESOURA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("EMPATE!")
    elif pc == 'PEDRA':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Computador ganhou!")
    elif pc == 'PAPEL':
        sleep(1)
        print("JO")
        sleep(1)  
        print("KEN")
        sleep(1)
        print("PO!!!\n")
        sleep(0.5)
        print("Você ganhou!")
else: 
    print("PROCESSANDO...\n")
    sleep(2)
    print("OPÇÃO INVÁLIDA! Você deve escolher entre Pedra, papel ou tesoura. Tente novamente!")

