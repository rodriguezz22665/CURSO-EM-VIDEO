#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))

opcao = int(input('''Qual será a base de conversão? Escolha uma das opções a seguir: 
              - 1 para binário
              - 2 para octal
              - 3 para hexadecimal
              '''))

if opcao == 1:
    print("{} convertido para binário é igual a {}".format(num,bin(num)[2:]))
elif opcao == 2:        
    print("{} convertido para octal é igual a {}".format(num,oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para hexadecimal é igual a {}".format(num,hex(num)[2:]))    

else:
    print("Número inválido!")