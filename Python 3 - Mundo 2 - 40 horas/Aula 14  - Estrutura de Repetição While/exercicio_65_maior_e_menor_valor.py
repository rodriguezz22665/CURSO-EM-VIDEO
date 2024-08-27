#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = n = soma = cont = media = 0
opcao = ''

while opcao != 'N':
    n = int(input("Digite um número inteiro: "))
    opcao = str(input("Você deseja continuar digitando valores? [S/N] ")).strip().upper()
    soma += n
    cont += 1
    if cont == 1:
        maior = n
        menor = n 
    else:
        if maior < n:
            maior = n 
        if menor > n:
            menor = n     
    

media = soma/cont   
print("Você digitou {} números e a média foi {:.2f}".format(cont,media))
print("O maior valor foi {} e o menor valor foi {}".format(maior,menor))