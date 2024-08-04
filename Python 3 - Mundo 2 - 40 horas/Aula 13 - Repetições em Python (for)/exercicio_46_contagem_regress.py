#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print("-*"*30)
print("CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFÍCIO")
print("-*"*30)

for c in range (10,-1,-1):
    print(c)
    sleep(1)
print("-*"*30)    
print("BuUum, BuUuUm, pOoW!!!")   
print("-*"*30)   