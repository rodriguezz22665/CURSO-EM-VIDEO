#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

cores = {'vermelho': '\033[31m','azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'roxo':'\033[35m', 'cinza': '\033[37m', 'lilas': '\033[36m', 'limpa': '\033[m'}

n1 = float(input("\033[45;32mDigite a primeira nota do aluno:\033[m "))
n2 = float(input("\033[44;32mDigite a segunda nota do aluno:\033[m "))

m = (n1 + n2) / 2

print("A média entre {}{}{} e {}{}{} é {:.1f}".format(cores['roxo'],n1,cores['limpa'],cores['azul'],n2,cores['limpa'],m))

