#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Digite o seu sexo: [M/F] ")).strip().upper()[0]

while sexo not in 'FfMm':
    sexo = str(input("\033[31mDado inválido! Tente novamente.\033[m\nDigite o seu sexo: [M/F] ")).strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))    



#Minha solucao 
'''sexo =''

while sexo != 'F' and sexo != 'M':
    sexo = str(input("Qual o seu sexo M/F? ")).strip().upper()[0]
    if sexo != 'F' and sexo != 'M':
        print("\033[31mDado inválido, digite novamente!\033[m")
        
print("Você digitou o sexo {}.".format(sexo))'''        