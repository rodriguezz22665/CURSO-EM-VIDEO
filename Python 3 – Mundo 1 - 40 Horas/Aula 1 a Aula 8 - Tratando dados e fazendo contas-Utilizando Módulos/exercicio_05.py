#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

num = int(input("\033[1;35;47mDigite número inteiro:\033[m "))

ante = num - 1 
suce = num + 1 

print("\033[7;36;47mAnalisando o valor {}, o seu antecessor é {} e o seu sucessor é {}\033[m".format(num,ante,suce))


