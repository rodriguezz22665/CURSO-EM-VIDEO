#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez','onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

'''while True:
    posicao = int(input('Digite um número entre 0 e 20: '))
    if posicao < 0 or posicao > 20:
        print("Número inválido! Tente novamente.")
    else:    
     print(f'Você digitou o número {extenso[posicao]}.')
     break'''

#Solucao professor Guanabara
while True:
    posicao = int(input('Digite um número entre 0 e 20: '))  
    if 0 <= posicao <= 20:
       break  
    print("Número inválido! Tente novamente.", end='')
print(f'Você digitou o número {extenso[posicao]}.')    