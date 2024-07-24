#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o valor do seu salário: "))

quinze = salario * 1.15
dez = salario * 1.10

if salario <= 1250:
    salario2 = quinze 
else:
    salario2 = dez     

print("Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.".format(salario, salario2))