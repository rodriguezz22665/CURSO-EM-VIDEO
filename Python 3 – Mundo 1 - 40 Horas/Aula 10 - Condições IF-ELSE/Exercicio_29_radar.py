#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

velo_atual = float(input("Qual a velocidade atual do carro? "))

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

fundo = {'limpa':'\033[m','vermelho':'\033[41m','verde':'\033[42m','amarelo':'\033[43m','azul':'\033[44m','cinza':'\033[47m','branco':'\033[7;40m'}


if velo_atual > 80:
    valor_multa = (velo_atual - 80) * 7
    print("{}MULTADO!{} Você excedeu o limite de velocidade permitido que é de 80 Km/h.\nVocê deve pagar uma multa de R$ {:.2f}!".format(fundo['vermelho'], fundo['limpa'],valor_multa))
print("{}Tenha um bom dia! Dirija com segurança!{}".format(fundo['cinza'], fundo['limpa']))
