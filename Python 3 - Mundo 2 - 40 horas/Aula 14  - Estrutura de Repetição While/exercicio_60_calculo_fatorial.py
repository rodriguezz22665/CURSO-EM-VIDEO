#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
#5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input("Digite um número para vizualizar o seu fatorial: "))   
count = num + 1
fat = []


while count >= 2:
    count -= 1
    fat.append (int(count))
   
  
    print(count)

print('fim')
print(fat)  
fator = fat[0] * fat[1] * fat[2] * fat[3] * fat[4] 
print(fator)