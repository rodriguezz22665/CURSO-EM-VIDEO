#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”.
#Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase aleatória: ")).upper().strip()

print(f"A letra 'A' apareceu {frase.count('A')} vezes nesta frase")


print(f"A primeira letra 'A' apareceu na posição {frase.find('A')+1}")
print(f"A segunda letra 'A' apareceu na posição {frase.rfind('A')+1}")
