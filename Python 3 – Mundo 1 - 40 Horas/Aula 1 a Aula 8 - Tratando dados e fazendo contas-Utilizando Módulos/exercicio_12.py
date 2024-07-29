#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("\033[1;32;46mDigite o valor do produto desejado:\033[m "))

desc = preco - (preco * 0.05) 

print("\033[36mCom 5% de desconto o preço vai de R$ {:.2f} para R$ {:.2f}\033[m\n\033[32mAproveite esta promoção!!!\033[m".format(preco,desc))