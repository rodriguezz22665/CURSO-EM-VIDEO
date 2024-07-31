#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Digite o valor da casa: R$ "))

salario = float(input("Digite o valor do seu salario: R$ "))

anos = int(input("Em quantos anos deseja pagar esta casa? "))

prestacao = casa/(anos*12)

if prestacao >= salario * 0.3:
    print("Valor da casa: {:.2f}\nTempo para quitar: {} anos\nValor das parcelas: R$ {:.2f}".format(casa,anos,prestacao))
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado!")
    print("Valor da casa: {:.2f}\nTempo para quitar: {} anos\nValor das parcelas: R$ {:.2f}".format(casa,anos,prestacao)) 
