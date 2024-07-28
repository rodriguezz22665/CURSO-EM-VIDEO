# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("\033[1;7;30;40mDigite o nome de uma cidade:\033[m ")).strip()

print('SANTO' in cidade[:5].upper())    
