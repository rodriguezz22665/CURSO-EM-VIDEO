# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input("Ditige um número real: "))

print("A porção inteira de {} é {}".format(num, math.trunc(num)))

