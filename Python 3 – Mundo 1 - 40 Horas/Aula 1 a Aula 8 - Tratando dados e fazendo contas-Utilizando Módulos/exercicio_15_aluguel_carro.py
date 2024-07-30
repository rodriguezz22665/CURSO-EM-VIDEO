# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input("\033[4;35mQuantos Km foram percorridos com o carro?\033[m  "))

dias = int(input("\033[4;36mPor quantos dias o carro foi alugado? \033[m"))

prec_total = (dias * 60) + (km * 0.15)

print("\033[1;42mO valor total do aluguel deste veículo foi de R$ {:.2f}\033[m".format(prec_total))