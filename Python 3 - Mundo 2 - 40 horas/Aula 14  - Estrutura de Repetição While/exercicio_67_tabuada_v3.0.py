#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo
'''print("="*80)
print('{:_^80}'.format(' TABOADA V3.0 '))
print("="*80)

cont = 0
núm = int(input("\nDigite um número para vizualizar a sua taboada: "))

while cont <= 10:
    cont += 1
    print(f"{núm} x {cont} = {núm*cont}")    

    if cont == 10:
        núm = int(input("\nDigite um número para vizualizar a sua taboada: "))
        cont = 0
        if núm < 0:
            break

print('{:=^80}'.format(" Obrigado por utilizar o TABOADA V3.0!!! "))'''

#SOLUCAO DO PROFESSOR GUANABARA:

print("="*80)
print('{:_^80}'.format(' TABOADA V3.0 '))
print("="*80)

while True:
    n = int(input("Digite um número para vizualizar a sua taboada: "))

    if n < 0:
        break

    for c in range (1, 11):
        print(f'{n} x {c} = {n*c}')
        
    print("-"*50)    
        
print('\n')
print('{:=^80}'.format(" Obrigado por utilizar o TABOADA V3.0!!! "))
print('\n')  

