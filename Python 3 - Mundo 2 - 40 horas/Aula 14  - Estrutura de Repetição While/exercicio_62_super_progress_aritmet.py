#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input("PRIMEIRO TERMO: "))
razao = int(input("RAZÃO: "))

cont = 1
termo = primeiro 
opcao2 = 0

print('{}'.format(primeiro), end ='')

while cont < 10:
    cont += 1
    termo = termo + razao
    '''print('{}'.format(primeiro) if cont == 2 else '', end='')'''
    print('' if cont == 1 else ' -> ',termo, end='')
    print(' -> FIM' if cont == 10 else '', end ='') 

    if cont == 10:
        opcao = int(input(('\nVocê deseja vizualizar mais termos? Digite [1] para sim ou [0] para sair do programa>: ')))
        if opcao == 1: 
            cont = 0
            while cont < 10: 
             cont += 1
             termo = termo + razao
             print('' if cont == 0 else ' -> ',termo, end='')
             print(' -> FIM' if cont == 10 else '', end='')
        elif opcao == 0:
           print('\033[32mSaindo do programa...\033[m')
        else:
           print('\033[31mOPÇÃO INVÁLIDA! Tente novamente!\033[m')
           opcao2 = int(input(('\nVocê deseja vizualizar mais termos? Digite [1] para sim ou [0] para sair do programa>: ')))
           if opcao2 == 1: 
            cont = 0
            while cont < 10: 
             cont += 1
             termo = termo + razao
             print('' if cont == 0 else ' -> ',termo, end='')
             print(' -> FIM' if cont == 10 else '', end='')
           elif opcao2 == 0:
            print('\033[32mSaindo do programa...\033[m')
           else:  
                print('\033[31mOPÇÃO INVÁLIDA! Tente novamente!\033[m')
                opcao2 = int(input(('\nVocê deseja vizualizar mais termos? Digite [1] para sim ou [0] para sair do programa>: ')))
                if opcao2 == 1: 
                    cont = 0
                while cont < 10: 
                    cont += 1
                    termo = termo + razao
                    print('' if cont == 0 else ' -> ',termo, end='')
                    print(' -> FIM' if cont == 10 else '', end='')

          #AO DIGITAR A OPCAO INVÁLIDA MAIS DE 2 VEZES, ELE ENCERRA O PROGRAMA SEM OFERECER OUTRA OPCAO
          #PROGRAMA ESTA ENCERRANDO SEM O 0 SER DIGITADO PELO USUÁRIO
                   
    

   


