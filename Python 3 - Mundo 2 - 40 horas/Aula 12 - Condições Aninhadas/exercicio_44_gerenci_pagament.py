#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros


print('{:/^80}'.format(' LOJAS RODRIGUEZ '))

valor = float(input("\nQual o valor total das compras? R$ "))

print('''FORMAS DE PAGAMENTO:
      \033[1;31m(digite o número correspondente a opção de pagamento desejada)\033[m\n 
      [1] á vista dinheiro/cheque: 10% de desconto
      [2] á vista no cartão: 5% de desconto
      [3] em até 2x no cartão: preço formal
      [4] 3x ou mais no cartão: 20% de juros\n''')

opcao = int(input("Qual a opção de pagamento você deseja? "))

if opcao == 1:
    total = valor - (valor * 0.1) 
    print("Você optou pela forma de pagamento 1\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.\n".format(valor, total))
elif opcao == 2:
    total = valor - (valor * 0.05)
    print("Você optou pela forma de pagamento 2\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.\n".format(valor, total))
elif opcao == 3:
    opcao2 = int(input("Quantas parcelas? \033[31m\nDigite 1 para uma parcela OU 2 para duas parcelas\033[m\n"))
    if opcao2 == 1:
      print("Você optou pela forma de pagamento 3 em 1x\n Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.\n".format(valor,valor))
    elif opcao2 == 2:
      prest = valor / 2
      print("Você optou pela forma de pagamento 3 em 2x.\nSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.".format(valor,valor))    
      print("Sua compra será parcelada em 2x de R$ {} SEM JUROS.\n".format(prest))
elif opcao == 4:
    opcao2 = int(input("Quantas parcelas? "))
    total = (valor * 1.2) 
    prest = total / opcao2 
    print("\nVocê optou pela forma de pagamento 4 em {}x.\nSua compra no valor de R$ {:.2f} vai custar R$ {:.2f} no final.".format(opcao2,valor, total))
    print("Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS.\n".format(opcao2,prest))
else: 
    print("\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE.\033[m ")            
