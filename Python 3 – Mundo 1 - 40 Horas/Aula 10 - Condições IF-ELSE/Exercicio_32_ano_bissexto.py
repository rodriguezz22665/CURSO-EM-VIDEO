#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#from datetime import date 

from datetime import date 
from time import sleep 

cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

ano = int(input("\033[1;47;32mQue ano deseja analisar? Digite 0 caso queira analisar o ano atual:\033[m "))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("\033[31mPROCESSANDO....\033[m")
    sleep(1)
    print("O ano de {}{}{} é bissexto!".format(cores['verde'],ano,cores['limpa']))
else:
    print("\033[31mPROCESSANDO....\033[m")
    sleep(1)
    print("O ano de {}{}{} não é um ano bissexto!".format(cores['vermelho'],ano,cores['limpa']))


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




