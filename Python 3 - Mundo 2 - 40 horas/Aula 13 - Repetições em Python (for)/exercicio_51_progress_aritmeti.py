#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('{:-^82}'.format(' 10 TERMOS DE UM PA '))
print("-="*41)
print("-="*41)

termo = int(input("\nPRIMEIRO TERMO: "))
razao = int(input("RAZÃO: "))
decimo = termo + (10 -1) * razao

for c in range (termo,decimo+razao,razao):
    print(c, end ='  ->  ')
print(" ACABOU")    
 