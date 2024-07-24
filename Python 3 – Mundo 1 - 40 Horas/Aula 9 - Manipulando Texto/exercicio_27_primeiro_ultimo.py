#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite o seu nome completo: ")).strip()

nome = n.split()

print("O seu primeiro nome é {}.".format(nome[0]))

print("O seu último nome é {}.".format(nome[0-1]))