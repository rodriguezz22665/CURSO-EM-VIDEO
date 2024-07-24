#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = float(input("Digite um número qualquer: "))

if num % 2 == 0:
    print("O número {} é um número par.".format(num))
else:
    print("O número {} é um número ímpar.".format(num))    
