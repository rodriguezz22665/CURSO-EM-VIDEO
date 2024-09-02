#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
#O programa será interrompido quando o número solicitado for negativo
print("="*80)
print('{:_^80}'.format(' TABOADA V3.0 '))
print("="*80)

cont = 0

núm = int(input("\nDigite um número inteiro para vizualizar a sua taboada: \n[PARA ENCERRAR O PROGRAMA DIGITE UM NÚMERO NEGATIVO] "))

while cont <= 10:
    cont += 1
    print(f"{núm} x {cont} = {núm*cont}")

    if cont == 10:
        núm = int(input("\nDigite um número inteiro para vizualizar a sua taboada: \n[PARA ENCERRAR O PROGRAMA DIGITE UM NÚMERO NEGATIVO] "))
        cont = 0
        if núm < 0:
            break
print('{:=^80}'.format(" Obrigado por utilizar o TABOADA V3.0!!! "))        