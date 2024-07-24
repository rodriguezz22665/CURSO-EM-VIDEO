# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite o nome ce uma cidade: ")).strip()

print('SANTO' in cidade[:5].upper())    
