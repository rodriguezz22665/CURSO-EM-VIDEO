#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#from datetime import date 

from datetime import date 
from time import sleep 

ano = int(input("Que ano deseja analisar? Digite 0 caso queira analisar o ano atual: "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("PROCESSANDO....")
    sleep(1)
    print("O ano de {} é bissexto!".format(ano))
else:
    print("PROCESSANDO....")
    sleep(1)
    print("O ano de {} não é um ano bissexto!".format(ano))


'''if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("PROCESSANDO....")
            sleep(2)
            print("O ano de {} é bissexto!".format(ano))
        else:
            print("PROCESSANDO....")
            sleep(2)
            print("O ano de {} não é um ano bissexto!".format(ano))
    else:
        print("PROCESSANDO....")
        sleep(2)
        print("O ano de {} é bissexto!".format(ano))'''




