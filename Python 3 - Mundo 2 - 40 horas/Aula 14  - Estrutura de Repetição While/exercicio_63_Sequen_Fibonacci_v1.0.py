#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
#0 – 1 – 1 – 2 – 3 – 5 – 8
#"A sequência de Fibonacci é uma sequência numérica infinita em que cada termo a partir do terceiro é a soma dos dois termos anteriores.
#Portanto, a sequência de Fibonacci é (1,1,2,3,5,8,13,21,34,55…)"

print("SEQUÊNCIA DE FIBONACCI")
print('~='*19)

quant_termos = int(input("Quantos termos você deseja vizualizar? "))
cont = 0
cont2 = 3
anterior = 1

while cont < quant_termos:
        cont += 1
        cont2 += 1
        if cont == 3:
                anterior += anterior
        elif cont == 4:
                anterior += 1     
 
        
        #cada termo a partir do terceiro é a soma dos dois termos anteriores
        print(anterior, end= '')
        print(cont)
        print(cont2, end='')


        





