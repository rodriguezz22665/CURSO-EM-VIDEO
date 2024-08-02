#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.


from datetime import date

ano_nasc = int(input("Em que ano você nasceu? "))
sexo = str(input("Qual seu sexo?"))
atual = date.today().year
idade = atual - ano_nasc

print("Quem nasceu no ano de {} tem {} anos em {}.".format(ano_nasc,idade,date.today().year))

if atual - ano_nasc == 18:
   print("Você tem que se alistar imediatamente!")
elif atual - ano_nasc < 18:
   saldo = 18 - idade 
   ano_alist = atual + saldo 
   print("Ainda faltam {} anos para o seu alistamento!".format(saldo))
   print("Seu alistamento será em {}!".format(ano_alist))
else:
   saldo = idade - 18
   ano_alist = atual - saldo
   print("Você já deveria ter se alistado há {} anos!".format(saldo))
   print("Seu alistamento foi em {}!".format(ano_alist))         