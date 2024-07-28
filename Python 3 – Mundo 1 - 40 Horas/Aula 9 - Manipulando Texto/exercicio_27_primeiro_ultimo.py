#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
cores = {'limpa': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'}

n = str(input("\033[1;7;40mDigite o seu nome completo:\033[m ")).strip()

nome = n.split()

print("{}O seu primeiro nome é {}{}.".format(cores['verde'],nome[0],cores['limpa']))

print("{}O seu último nome é {}{}.".format(cores['vermelho'],nome[0-1],cores['limpa']))