#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = float(input("\033[1;41mDigite um número qualquer:\033[m "))

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

fundo = {'limpa':'\033[m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m','cinza':'\033[47m','branco':'\033[7;40m'}

if num % 2 == 0:
    print("O número {}{}{} é um número par.".format(cores['verde'],num,cores['limpa']))
else:
    print("O número {}{}{} é um número ímpar.".format(cores['vermelho'],num,cores['limpa']))    
