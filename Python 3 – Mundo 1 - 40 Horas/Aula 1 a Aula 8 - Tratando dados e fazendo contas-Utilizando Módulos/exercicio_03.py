#Crie um programa que leia dois números e mostre a soma entre eles.

num1 = float(input('\033[47mDigite um valor:\033[m '))
num2 = float(input('\033[42mDigite outro valor:\033[m '))

soma = num1 + num2

print("\033[35;41mA soma entre {} e {} é {}\033[m".format(num1,num2,soma))