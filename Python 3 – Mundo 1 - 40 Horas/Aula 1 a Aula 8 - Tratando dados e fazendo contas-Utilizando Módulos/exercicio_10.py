#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("\033[44mQuanto dinheiro você tem na carteira?\033[m R$ "))

dolar = real/5.63

print("\033[34mCom R$ {} você pode comprar US$ {:.2f}\033[m".format(real, dolar))