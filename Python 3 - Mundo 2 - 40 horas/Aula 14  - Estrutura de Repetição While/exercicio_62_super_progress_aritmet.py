#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print("----GERADOR DE PA----\n")
primeiro = int(input("PRIMEIRO TERMO: "))
razao = int(input("RAZÃO: "))

cont = 1
termo = primeiro 
cont2 = 0
total_termos = 10

print('{}'.format(primeiro), end ='')

while cont < 10:
    cont += 1
    termo = termo + razao
    print('' if cont == 1 else ' -> ',termo, end='')
    print(' -> PAUSA' if cont == 10 else '', end ='')

    if cont == 10:
        cont2 = int(input(('\nQuantos termos você quer mostrar a mais? ')))
        while cont2 > 0:
            cont2 -= 1
            termo = termo + razao
            total_termos += 1
            print(termo, end=' -> ')
            print('PAUSA' if cont2 == 0 else '', end= '')
            if cont2 == 0:
                cont2 = int(input(('\nQuantos termos você quer mostrar a mais? ')))
print('\nProgressão finalizada com {} termos mostrados.\n'.format(total_termos))

#SOLUCAO PROFESSOR GUANABARA:

'''print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input("RAZÃO: "))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
     print("{} -> ".format(termo), end='')
     cont += 1
     termo += razao
    print('PAUSA')
    mais = int(input(('Quantos termos você quer mostrar a mais? ')))
print('\nProgressão finalizada com {} termos mostrados.\n'.format(total))'''
           

        
                   
    

   


