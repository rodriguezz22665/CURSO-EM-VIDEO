#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
count = 0 

for c in range (1,7):
    num = int(input("Digite o {}° número inteiro: ".format(c)))
    if num % 2 == 0:
        soma += num
        count += 1
print("Você informou {} números pares, a soma foi {}.".format(count,soma))    