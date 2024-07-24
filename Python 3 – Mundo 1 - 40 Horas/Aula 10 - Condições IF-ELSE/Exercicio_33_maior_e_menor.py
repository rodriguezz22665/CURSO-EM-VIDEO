#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Digite o primeiro número: "))#5
num2 = int(input("Digite o segundo número: "))#4
num3 = int(input("Digite o terceiro número: "))#7

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

print("O maior número digitado foi {}!".format(maior))
print("O menor número digitado foi {}!".format(menor))

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