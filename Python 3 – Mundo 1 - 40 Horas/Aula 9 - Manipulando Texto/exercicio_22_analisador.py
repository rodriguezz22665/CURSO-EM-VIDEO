#Crie um programa que leia o nome completo de uma pessoa e mostre:

  #O nome com todas as letras maiúsculas e minúsculas.
  #Quantas letras ao todo (sem considerar espaços).
  #Quantas letras tem o primeiro nome.

nome = str(input("Digite o seu nome completo: ")).strip()

print("\nAnalisando o seu nome...\n")

print(f"O seu nome em maúsculas é : {nome.upper()}")
print(f"O seu nome em minúsculas é: {nome.lower()}")

print(f"O seu nome tem ao todo tem {(len(nome) - nome.count(' '))} caractéres.")

#print("O seu prieiro tem {} letas".format(nome.find(' ')))

nome_dividido = nome.split()
print(f"O seu primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras")








