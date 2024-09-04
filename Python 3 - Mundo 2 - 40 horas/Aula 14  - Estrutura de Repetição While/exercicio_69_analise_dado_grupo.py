#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

cont = 0
A = 0
B = 0
C = 0
print("{:=^80}".format(" CADASTRO DE PESSOAS "))

while True:
    cont+= 1
    idade = int(input(f"\nDigite a idade da {cont}º pessoa: "))
    if idade > 18:
        A += 1
    sexo = ' '
    opcao = ' '
    while sexo not in 'FM':
        sexo = str(input(f"Sexo da {cont}ª pessoa [F/M]: ")).strip().upper()[0]
        if sexo == 'M':
            B += 1
        elif sexo == 'F' and idade < 20:
            C += 1
    while opcao not in 'SN':    
        opcao = str(input("Você deseja adicionar mais uma pessoa? [S/N]? ")).strip().upper()[0]
        if opcao in 'SN':
            print("~="*40 )
        
    if opcao == 'N':
            break
    
print(f"\nForam cadastradas {A} pessoa(s) acima dos 18 anos.")
print(f"Foram cadastrados {B} homens.")
print(f"Foram cadastradas {C} mulher(es) com menos de 20 anos.\n")
print("~="*40)