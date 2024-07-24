#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#A multa vai custar R$7,00 por cada Km acima do limite.

velo_atual = float(input("Qual a velocidade atual do carro? "))

if velo_atual > 80:
    valor_multa = (velo_atual - 80) * 7
    print("MULTADO! Você excedeu o limite de velocidade permitido que é de 80 Km/h.\nVocê deve pagar uma multa de R$ {:.2f}!".format(valor_multa))
print("Tenha um bom dia! Dirija com segurança!")
