#  Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input("\033[1;47mDigite um número de 0 a 9999:\033[m "))

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

fundo = {'limpa':'\033[m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m','cinza':'\033[47m','branco':'\033[7;40m'}

estilo = {'negrito':'\033[1m','sublinhado':'\033[4m'}

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10 

print("{}Analisando o número... {}{}".format(fundo['branco'], num, cores['limpa']))

print("{}Unidade: {}{}".format(fundo['verde'],u,fundo['limpa']))
print("{}Dezena: {}{}".format(fundo['vermelho'],d,fundo['limpa']))
print("{}Centena: {}{}".format(fundo['amarelo'],c,fundo['limpa']))
print("{}Milhar: {}{}".format(fundo['azul'],m,fundo['limpa']))


