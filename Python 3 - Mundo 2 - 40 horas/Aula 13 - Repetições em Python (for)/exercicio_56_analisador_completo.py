#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
idade_homem_velho = 0 
tot_mulher_20 = 0
homem_velho = ''

for pessoa in range (1, 5):

    print("-----Digite os dados da {}° pessoa-----".format(pessoa))

    nome = str(input("Nome: ")).strip()

    idade = int(input("Idade: "))

    sexo = str(input("Sexo F(Feminino) ou M(Masculino): ")).strip()

    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

    elif sexo in 'Mm' and idade > idade_homem_velho:
        idade_homem_velho = idade
        homem_velho = nome

    media += idade 

media = media/4    

print("-="*18)
print("\nA média de idade do grupo é {:.2f}".format(media))  
print("O homem mais velho desse grupo se chama {} e tem {} anos.".format(homem_velho,idade_homem_velho))  
print("Nesse grupo temos {} mulher(es) abaixo dos 20 anos.".format(tot_mulher_20))

    

    
