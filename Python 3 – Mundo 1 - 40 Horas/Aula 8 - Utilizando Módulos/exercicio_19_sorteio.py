# Um professor quer sortear um de seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

cores = {'verde':'\033[32m', 'vermelho':'\033[31m', 'lilas':'\033[36m]', 'limpa':'\033[m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'roxo':'\033[35m'}


aluno1 = input("{}Digite o nome do aluno: {}".format(cores['verde'], cores['limpa']))
aluno2 = input("{}Digite o nome do aluno: {}".format(cores['lilas'], cores['limpa']))
aluno3 = input("{}Digite o nome do aluno: {}".format(cores['amarelo'],cores['limpa']))
aluno4 = input("{}Digite o nome do aluno: {}".format(cores['azul'], cores['limpa']))

lista_alunos = [aluno1,aluno2,aluno3,aluno4]
lista_alunos = random.choice(lista_alunos)

print("{}{}{} foi escolhido para apagar o quadro hoje!".format(cores['roxo'],lista_alunos,cores['limpa']))

