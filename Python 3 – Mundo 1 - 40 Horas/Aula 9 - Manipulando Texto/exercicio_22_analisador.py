#Crie um programa que leia o nome completo de uma pessoa e mostre:

  #O nome com todas as letras maiúsculas e minúsculas.
  #Quantas letras ao todo (sem considerar espaços).
  #Quantas letras tem o primeiro nome.

nome = str(input("\033[1;7;30;40mDigite o seu nome completo: \033[m")).strip()

print("\033[1;41m\nAnalisando o seu nome...\033[m\n")

print(f"\033[44mO seu nome em maúsculas é : {nome.upper()}\033[m")
print(f"\033[46mO seu nome em minúsculas é: {nome.lower()}\033[m")

print(f"\033[47mO seu nome tem ao todo tem {(len(nome) - nome.count(' '))} caractéres.\033[m")

#print("O seu prieiro tem {} letas".format(nome.find(' ')))

nome_dividido = nome.split()
print(f"\033[1;43;37mO seu primeiro nome é {nome_dividido[0]} e tem {len(nome_dividido[0])} letras\033[m")








