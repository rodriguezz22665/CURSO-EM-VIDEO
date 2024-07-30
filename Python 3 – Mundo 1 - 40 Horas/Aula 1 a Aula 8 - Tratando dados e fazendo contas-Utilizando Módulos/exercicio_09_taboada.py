#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

cores = {'vermelho': '\033[31m','azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'roxo':'\033[35m', 'cinza': '\033[37m', 'lilas': '\033[36m', 'limpa': '\033[m'}

num = int(input("\033[1;45mDigite um número para ver a sua taboada:\033[m "))

print("\033[1;47;33m-\033[m"*43)
print("{}{} x  1 = {}{}".format(cores['vermelho'],num,num*1,cores['limpa']))
print("{}{} x  2 = {}{}".format(cores['verde'],num,num*2,cores['limpa']))
print("{}{} x  3 = {}{}".format(cores['vermelho'],num,num*3,cores['limpa']))
print("{}{} x  4 = {}{}".format(cores['verde'],num,num*4,cores['limpa']))
print("{}{} x  5 = {}{}".format(cores['vermelho'],num,num*5,cores['limpa']))
print("{}{} x  6 = {}{}".format(cores['verde'],num,num*6,cores['limpa']))
print("{}{} x  7 = {}{}".format(cores['vermelho'],num,num*7,cores['limpa']))
print("{}{} x  8 = {}{}".format(cores['verde'],num,num*8,cores['limpa']))
print("{}{} x  9 = {}{}".format(cores['vermelho'],num,num*9,cores['limpa']))
print("{}{} x 10 = {}{}".format(cores['verde'],num,num*10,cores['limpa']))
print("\033[1;47;33m-\033[m"*43)