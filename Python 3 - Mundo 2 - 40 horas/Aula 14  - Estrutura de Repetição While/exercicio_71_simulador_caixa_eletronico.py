#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("  /"*27)
print('{:¤^80}'.format(" CAIXA ELETRÔNICO "))
print("  /"*27)

tot_50 = tot_20 = tot_10 = tot_1 = resto = resto2 = 0
saque = int(input("Qual o valor você deseja sacar? "))

   
cinquenta = int(saque/50) 
vinte = int(saque/20)
dez = int(saque/10)
um = int(saque/1)

if saque > 50:
    tot_50 = cinquenta * 50
    resto = saque - tot_50
    print(f"{cinquenta} notas de 50")
elif saque < 50 and saque >= 20:
    tot_20 = vinte * 20 
    resto = saque - tot_20 
    print(f'{vinte} notas de 20')
elif saque < 20 and saque >= 10:
    tot_10 = dez * 10
    resto = saque - tot_10
    print(f"{dez} notas de 10")
elif saque < 10 and saque >= 1:
    tot_1 = um * 1
    resto = saque - tot_1     
    print(f"{um} notas de 1")  

if resto != 0:
    if resto >= 20:
        resto2 = resto/20
        print("notas de 20")
    elif resto < 20 and resto >= 10:
        resto2 = resto/10
        print("notas de 10")
    elif resto < 10 and resto >= 1:
        resto2 = resto/1        

print(resto)
print(resto2)
print(f'{cinquenta}')
print(f'{vinte}')
print(f'{dez}')
print(f'{um}')