#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input("\033[7;33;47mDigite um número:\033[m "))

cores = {'vermelho': '\033[31m','azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'roxo':'\033[35m', 'cinza': '\033[37m', 'lilas': '\033[36m', 'limpa': '\033[m'}

from math import sqrt

dobro = num * 2
triplo = num * 3
raiz = sqrt(num)

print("O dobro de {}{}{} é {}".format(cores['amarelo'],num,cores['limpa'],dobro))
print("O triplo de {}{}{} é {}".format(cores['amarelo'],num,cores['limpa'],triplo))
print("A raiz quadrada de {}{}{} é {:2f}".format(cores['amarelo'],num,cores['limpa'],raiz))