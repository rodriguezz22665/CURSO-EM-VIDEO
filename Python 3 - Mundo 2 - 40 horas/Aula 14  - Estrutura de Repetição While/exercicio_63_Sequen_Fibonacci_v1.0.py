#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
#"A sequência de Fibonacci é uma sequência numérica infinita em que cada termo a partir do terceiro é a soma dos dois termos anteriores.
#Portanto, a sequência de Fibonacci é (1,1,2,3,5,8,13,21,34,55…)"

print("SEQUÊNCIA DE FIBONACCI")
print('~='*20)

quant_termos = int(input("Quantos termos você deseja vizualizar? "))
cont = 0
termo3 = 0
termo1 = 0
termo2 = 1

print('{} -> {}'.format(termo1,termo2),end='')

while cont < quant_termos:
        cont += 1
        termo3 = termo1 + termo2
        termo1 = termo2
        termo2 = termo3
        print('-> {}'.format(termo3),end='')
        
   

        
       

      
       


        





