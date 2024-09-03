#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

while True:
    pc = randint(1,10)

    escolha = str(input("Par[P] ou Ímpar[I]? ")).strip().upper()

    usuario = int(input("Digite um número inteiro: "))

    if escolha == 'P' and usuario % 2 == 0:
        if pc % 2 == 0:
            print(f"O pc escolheu {pc} e Você escolheu {usuario}. Empate! ")
        elif pc % 2 != 0:
            print(f"O pc escolheu {pc} e Você escolheu {usuario}. Você ganhou! ")    
    elif escolha == 'I' and usuario % 2 != 0:
        if pc % 2 != 0:
            print(f"O pc escolheu {pc} e você escolheu {usuario}. Empate! ")
        elif pc % 2 == 0:
            print(f"O pc escolheu {pc} e você escolheu {usuario}. Você ganhou! ") 

print(usuário)
print(pc)

