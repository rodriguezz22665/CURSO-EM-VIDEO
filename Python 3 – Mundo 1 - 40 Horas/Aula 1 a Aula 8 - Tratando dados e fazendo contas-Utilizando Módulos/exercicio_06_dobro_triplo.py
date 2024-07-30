#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = float(input("Digite um número: "))

from math import sqrt

dobro = num * 2
triplo = num * 3
raiz = sqrt(num)

print("O dobro de {} é {}".format(num,dobro))
print("O triplo de {} é {}".format(num,triplo))
print("A raiz quadrada de {} é {}".format(num,raiz))