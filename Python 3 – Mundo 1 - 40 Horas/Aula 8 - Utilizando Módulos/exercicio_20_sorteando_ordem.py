# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = input("\033[47;35mDigite o nome do aluno: \033[m")
aluno2 = input("\033[47;36mDigite o nome do aluno: \033[m")
aluno3 = input("\033[47;32mDigite o nome do aluno: \033[m")
aluno4 = input("\033[47;30mDigite o nome do aluno: \033[m")

lista_alunos = [aluno1,aluno2,aluno3,aluno4]

random.shuffle(lista_alunos)

print(f"\033[1;7;41;33mA ordem de apresentação do trabalho é:\033[m \033[7;37;40m{lista_alunos}\033[m")