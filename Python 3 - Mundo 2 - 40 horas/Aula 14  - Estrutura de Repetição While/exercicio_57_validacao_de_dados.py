#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo =''

while sexo != 'F' or sexo != 'M':
    sexo = str(input("Qual o seu sexo M/F? ")).upper()
    if sexo != 'F' or sexo != 'M':
        print("\033[31mDado inválido, digite novamente!\033[m")
print("Você digitou o sexo {}.".format(sexo))        