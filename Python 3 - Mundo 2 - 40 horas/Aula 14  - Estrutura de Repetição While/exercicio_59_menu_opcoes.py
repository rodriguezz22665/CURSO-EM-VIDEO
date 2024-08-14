#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num_user = 0
num_user2 = 0 
opcao = 0

print("-----CALCULADORA COM MENU-----\n")
num_user = int(input("Digite o primeiro número: "))
num_user2 = int(input("Digite o segundo número: "))

while opcao != 5:

        print("\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa")
        sleep(1)
        opcao = int(input("\n>>>> Qual operação você deseja realizar? "))

        if opcao == 1:
            somar = num_user + num_user2
            print("\nA soma entre {} e {} é {}".format(num_user, num_user2, somar))   
            print("-="*21)  
        elif opcao == 2:
            multiplicar = num_user * num_user2
            print("\nMultiplicando {} por {} fica {}".format(num_user, num_user2, multiplicar))  
            print("-="*21) 
        elif opcao == 3:
            if num_user > num_user2:
                maior = num_user
            else:
                maior = num_user2     
            print("\nO maior número digitado foi {}".format(maior)) 
            print("-="*21)    
        elif opcao == 4:
            print("-="*21) 
            print("\nDIGITE OS NOVOS NÚMEROS\n")  
            num_user = int(input("Digite o primeiro número: "))
            num_user2 = int(input("Digite o segundo número: "))
        elif opcao == 5:
            print("-="*21) 
            print("\033[32mSaindo do programa...\033[m")
            sleep(1)
            print("Obrigado por utilizar o programa!") 
            print("-="*21) 
        else:
            print("-="*21) 
            print("\033[31mOpção inválida! Tente novamente\033[m")
            print("-="*21)       
       



