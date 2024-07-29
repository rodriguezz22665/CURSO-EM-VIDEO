#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o valor do produto desejado: "))

desc = preco - (preco * 0.05) 

print("Com 5% de desconto o preço vai de R$ {:.2f} para R$ {:.2f}\nAproveite esta promoção!!!".format(preco,desc))