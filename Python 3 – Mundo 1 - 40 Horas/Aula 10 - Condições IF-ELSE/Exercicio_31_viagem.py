#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

distancia = float(input("\033[33;44mQual a distância da sua viagem?\033[m "))
print("Você está prestes a iniciar uma viagem de {}{:.0f}{} KM.".format(cores['verde'],distancia,cores['limpa']))

preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print("O preço desta viagem é: {}R$ {:.2f}{}".format(cores['vermelho'],preco,cores['limpa']))

'''if distancia <= 200:
    preco = distancia * 0.5
    print("O preço desta viagem é: R$ {:.2f}".format(preco))
else:
    preco = distancia * 0.45
    print("O preço desta viagem é: R$ {:.2f}".format(preco))'''    
