casa = float(input("Digite o valor da casa: R$ "))

salario = float(input("Digite o valor do seu salario: R$ "))

anos = int(input("Em quantos anos deseja pagar esta casa? "))


if casa/(anos*12) > salario * 0.3:
    print("Orçamento reprovado!")
else:
    print("Orçamento aprovado!")
    print("Valor da casa: {:2f}\nValor das parcelas: R$ {:2f}".format(casa,(casa/(anos*12))))    
