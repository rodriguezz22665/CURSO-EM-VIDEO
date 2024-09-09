#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000
#C) qual é o nome do produto mais barato.           


print('{:|^80}'.format(" LOJAS RODRIGUEZz "))

valor_prod = tot_valor = cont = tot_1000 = 0
mais_barato = ' '

while True:

    produto = str(input("\nNOME DO PRODUTO: ")).strip().upper()
    preco = float(input("PREÇO: "))
    cont += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
        if opcao in 'S':
            print("-="*40)
    tot_valor += preco

    if cont == 1:
        mais_barato = produto
        valor_prod = preco
    if valor_prod > preco:
        valor_prod = preco
        mais_barato = produto
        

    if preco > 1000:
        tot_1000 += 1 
    if opcao in 'Nn':
        break


print('{:=^80}'.format(" RESUMO DA COMPRA "))
print(f'\nVALOR TOTAL: R$ {tot_valor:.2f}')
print(f'VOCÊ COMPROU {tot_1000} PRODUTO(s) ACIMA DE R$ 1000,00.')
print(f'O PRODUTO MAIS BARATO QUE VOCÊ COMPROU FOI {mais_barato} que custa R$ {valor_prod:.2f}')
print("\n")
print('{:^80}'.format("OBRIGADO POR COMPRAR NAS LOJAS RODRIGUEZz! VOLTE SEMPRE!"))    
print("{:_^80}".format(" © Copyright 2024 "))




