#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”.
#Em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("\033[1;47mDigite uma frase aleatória:\033[m ")).upper().strip()

print(f"\033[1;32;47mA letra 'A' apareceu {frase.count('A')} vezes nesta frase\033[m")


print(f"\033[1;35;47mA primeira letra 'A' apareceu na posição {frase.find('A')+1}\033[m")
print(f"\033[1;34;47mA segunda letra 'A' apareceu na posição {frase.rfind('A')+1}\033[m")
