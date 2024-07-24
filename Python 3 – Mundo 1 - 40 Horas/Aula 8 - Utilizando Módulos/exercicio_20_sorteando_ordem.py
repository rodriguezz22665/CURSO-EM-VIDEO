# Um professor quer sortear a ordem de apresentação de trabalhos dos alunos
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

aluno1 = input("Digite o nome do aluno: ")
aluno2 = input("Digite o nome do aluno: ")
aluno3 = input("Digite o nome do aluno: ")
aluno4 = input("Digite o nome do aluno: ")

lista_alunos = [aluno1,aluno2,aluno3,aluno4]

random.shuffle(lista_alunos)

print(f"A orde de apresentação do trabalho é: {lista_alunos}")