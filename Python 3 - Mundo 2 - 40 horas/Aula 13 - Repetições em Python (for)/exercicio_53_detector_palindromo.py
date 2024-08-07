#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input("Digite uma frase: ")).strip().upper().split()

junto = ''.join(frase)

#solucao alternativa ao for para inverter a frase:
#inverso = frase[::-1]

inverso = ''

for c in range (len(junto)-1,-1,-1):
   inverso += junto[c]
    
print("O inverso de {} é {}.".format(junto,inverso, end = ' '))

if inverso == junto:
    print("Temos um palíndromo!")
elif inverso != junto: 
    print("A frase digitada NÃO É um palíndromo!")    


