#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input("Digite a temperatura em graus Celsius: "))

f = (c * 1.8) + 32

print("{} graus Celsius corresponde a {:.2f} graus Fahrenheit".format(c,f))