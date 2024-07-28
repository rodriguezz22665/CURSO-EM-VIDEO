#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("\033[7;47;32mDigite o valor do seu salário:\033[m "))

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

quinze = salario * 1.15
dez = salario * 1.10

if salario <= 1250:
    salario2 = quinze 
else:
    salario2 = dez     

print("Quem ganhava {}R$ {:.2f}{} passa a ganhar {}R$ {:.2f}{} agora.".format(cores['azul'],salario,cores['limpa'], cores['verde'],salario2,cores['limpa']))