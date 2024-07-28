# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math
num = float(input("\033[2;31mDitige um número real:\033[m "))

print("A porção inteira de {}{}{} é {}{}{}".format('\033[3;35;45m',num,'\033[m', '\033[2;34;44m',math.trunc(num),'\033[m'))