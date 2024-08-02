#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

ano_nasc = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade = ano_atual - ano_nasc

if idade <= 9:
    print("Atletas com {} anos estão na categoria MIRIM!".format(idade))
elif idade <= 14:
    print("Atletas com {} anos estão na categoria INFANTIL!".format(idade))     
elif idade <= 19:
    print("Atletas com {} anos estão na categoria JÚNIOR!".format(idade))     
elif idade <= 25:
    print("Atletas com {} anos estão na categoria SÊNIOR!".format(idade)) 
elif idade > 25:
    print("Atletas com {} anos estão na categoria MASTER!".format(idade))                 