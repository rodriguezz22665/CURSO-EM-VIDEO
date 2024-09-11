#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("  /"*27)
print('{:¤^80}'.format(" CAIXA ELETRÔNICO "))
print("  /"*27)

saque = int(input("Qual o valor você deseja sacar? "))

cinquenta = saque/50 
vinte = saque/20
dez = saque/10
um = saque/1

print(f'{cinquenta}')
print(f'{vinte}')
print(f'{dez}')
print(f'{um}')