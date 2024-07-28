#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

num1 = int(input("\033[1;7;47;32mDigite o primeiro número:\033[m "))
num2 = int(input("\033[1;7;47;31mDigite o segundo número:\033[m "))
num3 = int(input("\033[1;7;47;35mDigite o terceiro número:\033[m "))

maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num2 and num3 > num1:
    maior = num3

menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num2 and num3 < num1:
    menor = num3    

print("{}O maior número digitado foi {}{}!".format(cores['azul'],maior,cores['limpa']))
print("{}O menor número digitado foi {}{}!".format(cores['verde'],menor,cores['limpa']))

'''if num1 > num2 and num1 > num3:
    print("O número {} é o maior número!".format(num1))
elif num2 > num1 and num2 > num3:
        print("O número {} é o maior número!".format(num2))
elif num3 > num1 and num3 > num2:
            print("O número {} é o maior número!".format(num3))    
            
if num1 < num2 and num1 < num3:
    print("O número {} é o menor número!".format(num1))
elif num2 < num1 and num2 < num3:
        print("O número {} é o menor número!".format(num2))
elif num3 < num1 and num3 < num2:
            print("O número {} é o menor número!".format(num3))'''    