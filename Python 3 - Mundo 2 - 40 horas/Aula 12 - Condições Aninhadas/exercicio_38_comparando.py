    #Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print("O primeiro número é maior!")

elif num2 > num1:
    print("O segundo número é maior!")

else:
    print("Não existe valor maior, os dois são iguais!")       