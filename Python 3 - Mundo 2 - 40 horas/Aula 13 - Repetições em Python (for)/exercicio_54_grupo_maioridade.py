#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0

for pessoa in range (1,5):
    nasc = int(input("Digite o ano de nascimento da {}° pessoa: ".format(pessoa)))
    idade = ano_atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1 
   
    
print("Nessa lista tem {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade.".format(maior,menor))
  