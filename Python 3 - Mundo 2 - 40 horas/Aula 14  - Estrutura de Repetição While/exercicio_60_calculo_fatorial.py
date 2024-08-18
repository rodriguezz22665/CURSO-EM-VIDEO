#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

#MINHA SOLUÇÃO NA QUAL DEMOREI 5415848485 ANOS:
num = int(input("Digite um número para vizualizar o seu fatorial: "))   
count = num + 1
lista = []
sep =  ' x '
fatorial = 0 

while count >= 2:
    count -= 1
    lista.append(str(count))
   
    if count == num:
        fatorial = count 
    else:    
        fatorial = fatorial * count    

print('\nO fatorial de {} é: \n'.format(num))
print('{}! = '.format(num) + sep.join(lista) + ' = {}\n'.format(fatorial))


#SOLUCAO PROFESSOR GUANABARA:
'''n = int(input("Digite um número para calcular o seu fatorial: ")) 
c = n
f = 1 
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
