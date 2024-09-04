#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

'''from random import randint
cont = 0

print('{:=^80}'.format("JOGO DO PAR OU ÍMPAR"))
print("-="*40)

while True:
    pc = randint(1,10)
    usuario = int(input("Digite um valor: "))
    escolha = str(input("Par[P] ou Ímpar[I]? ")).strip().upper()[0]
    soma = usuario + pc 
    
    if escolha == 'P':
        if soma % 2 == 0:
            print(f"Você jogou {usuario} e o PC jogou {pc}. Total de {soma} DEU PAR.")
            print("-"*80)
            print("Você venceu! \nVamos jogar novamente...")
            print("="*80)
            cont +=1
        elif soma % 2 != 0:
            print("-"*80)
            print(f"Você jogou {usuario} e o PC jogou {pc}. Total de {soma} DEU ÍMPAR.")
            print("O PC venceu!")
            print("-"*80)
            print(f"GAME OVER!!! Você venceu {cont} vez(es)")
            print("-"*80)
            break          
    elif escolha == 'I':
        if soma % 2 != 0:
            print("-"*80)
            print(f"Você jogou {usuario} e o PC jogou {pc}. Total de {soma} DEU ÍMPAR.")
            print("-"*80)
            print("Você venceu! \nVamos jogar novamente...")
            print("-"*80)
            cont += 1
        elif soma % 2 == 0:
            print("-"*80)
            print(f"Você jogou {usuario} e o PC jogou {pc}. Total de {soma} DEU PAR.") 
            print("-"*80)
            print("O PC venceu!")
            print("-"*80)
            print(f"GAME OVER!!! Você venceu {cont} vezes")
            print("-"*80)
            break'''

#SOLUCAO PROFESSOR GUANABARA:

from random import randint
v = 0
print('{:=^80}'.format("JOGO DO PAR OU ÍMPAR"))
print("-="*40)
while True:
    jogador = int(input("Digite um valor: "))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o PC jogou {computador}. Total de {total} ", end='')     
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")

    if tipo == 'P':
        if total % 2 == 0:
            print("VOCÊ VENCEU!")
            v += 1
        else:
            print("VOCÊ PERDEU!")
            break

    elif tipo == 'I':
        if total % 2 != 1:
            print("VOCÊ VENCEU!")
            v += 1
        else:
            print("VOCÊ PERDEU!")
            break    
    print("Vamos jogar novamente...")  
print(f"GAME OVER!!! Você venceu {v} vez(es).")          