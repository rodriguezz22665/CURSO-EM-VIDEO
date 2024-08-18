##Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120 
#Só que dessa vez utilize o FOR

num = int(input('Digite um número para vizualizar o seu fatorial: '))
fatorial = 0

print("\n{} ! = ".format(num), end='')

for c in range (num,0,-1):
    
    print(c,  end=' ')
    print(' x ' if c > 1 and c <= num else ' = ', end='')
    if c == num:
        fatorial = num
    else:
        fatorial = c * fatorial
    
print(fatorial)            