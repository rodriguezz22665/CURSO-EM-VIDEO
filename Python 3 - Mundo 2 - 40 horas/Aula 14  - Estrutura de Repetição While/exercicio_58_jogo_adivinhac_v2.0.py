#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

palpite = 1

computador = randint(0,10)

jogador = int(input("Eu pensei em um número entre 0 e 10.\nTente adivinhar...\nQual o seu palpite? "))

while jogador != computador:
    print("\033[32mProcessando...\033[m")
    sleep(0.5)

    if computador > jogador:
        print("\033[31mMais... Tente outra vez!\033[m")
        jogador = int(input("Qual o seu palpite? "))
    elif computador < jogador:
        print("\033[31mMenos... Tente outra vez!\033[m")
        jogador = int(input("Qual o seu palpite? "))

    palpite += 1

sleep(1)    
print("\n\033[32mACERTOU!!\033[m\nVocê digitou o número {}.\nForam {} tentativas até acertar!\n".format(jogador,palpite))    
