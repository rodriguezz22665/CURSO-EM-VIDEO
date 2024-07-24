#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint 
from time import sleep

num = randint(0,5)
print("-----"*20)
num_usuario = int(input("Eu escolhi um número inteiro entre 0 e 5, tente adivinhar qual e digite: "))
print("-----"*20)     

print("PROCESSANDO....")
sleep(2)
print("-----"*20)

if num_usuario == num: 
 print("Parabéns! Você escolheu o número {}. Você acertou!".format(num_usuario))
else: 
 print("Não foi desta vez, eu escolhi o número {}.\nTente novamente!".format(num)) 
