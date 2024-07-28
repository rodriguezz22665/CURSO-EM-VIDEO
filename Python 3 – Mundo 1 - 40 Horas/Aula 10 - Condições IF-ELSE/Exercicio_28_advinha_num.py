#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar 
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint 
from time import sleep

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

fundo = {'limpa':'\033[m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m','cinza':'\033[47m','branco':'\033[7;40m'}

num = randint(0,5)
print("\033[1;35m-----\033[m"*15)    
num_usuario = int(input("\033[1;45mEu escolhi um número inteiro entre 0 e 5, tente adivinhar qual e digite:\033[m "))
print("\033[1;35m-----\033[m"*15)     

print("{}PROCESSANDO....{}".format(fundo['vermelho'], fundo['limpa']))
sleep(2)
print("\033[1;35m-----\033[m"*15)  

if num_usuario == num: 
 print("{}Parabéns!{} Você escolheu o número {}. {}Você acertou!{}".format(cores['verde'], cores['limpa'],num_usuario, cores['verde'], cores['limpa']))
else: 
 print("{}Não foi desta vez{}, eu escolhi o número {}.\n{}Tente novamente!{}\n".format(cores['vermelho'],cores['limpa'],num,cores['vermelho'],cores['limpa'])) 
