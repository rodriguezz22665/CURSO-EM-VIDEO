#Desenvolva um programa que leia o comprimento de três retas, 
#e diga ao usuário se elas podem ou não formar um triângulo.
cores = {'limpa':'\033[m','vermelho':'\033[31m','verde':'\033[32m','amarelo':'\033[33m','azul':'\033[34m','cinza':'\033[37m'}

print("\033[7;47;35m-=\033[m"*15)
print("\033[2;45;7;32mANALISANDO TRIÂNGULOS\033[m")
print("\033[7;47;35m-=\033[m"*15)

reta1 = float(input("\033[1;7;47mDigite o valor da reta 1:\033[m "))
reta2 = float(input("\033[1;7;47mDigite o valor da reta 2:\033[m "))
reta3 = float(input("\033[1;7;47mDigite o valor da reta 3:\033[m "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta2 > reta1:
    print("{}É possível criar um triângulo com os três seguimentos acima!{}".format(cores['verde'],cores['limpa']))
else:
    print("{}Não é possível criar um triângulo com os três seguimentos acima!{}".format(cores['vermelho'],cores['limpa']))

    