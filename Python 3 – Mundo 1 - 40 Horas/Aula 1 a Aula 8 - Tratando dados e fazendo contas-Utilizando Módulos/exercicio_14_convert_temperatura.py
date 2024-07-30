#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("\033[1;31;43mDigite a temperatura em graus Celsius:\033[m "))

f = (c * 1.8) + 32

print("\033[33m{} graus Celsius corresponde a {:.2f} graus Fahrenheit\033[m".format(c,f))