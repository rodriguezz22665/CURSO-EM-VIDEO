#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#Um número natural é primo se ele possui apenas dois divisores positivos e distintos. Ou seja, um número natural é primo se ele é maior que 1 e é divisível apenas por si próprio e por 1.

num = int(input("Digite um número inteiro: "))

count = 0

#cores = {'amarelo' : '\033[33m', 'limpa' : '\033[m'}
#print("\033[33m{}{}{}\033[m".format(cores['amarelo'],c,cores['limpa']))


for c in range (1,num+1):
    if num % c == 0 and num % 1 == 0:
        count += 1 
        print('\033[33m', end = ' ')
    else:
        print("\033[31m", end = ' ')    
    print("{}".format(c), end = ' ')

if count != 2:
    print("\n\033[mO número {} foi divisível por {} vezes.\nE por isso ele NÃO É PRIMO!".format(num,count))
else: 
    print("\n\033[mO número {} foi divisível por {} vezes.\nE por isso ele É PRIMO!".format(num,count))        
        
