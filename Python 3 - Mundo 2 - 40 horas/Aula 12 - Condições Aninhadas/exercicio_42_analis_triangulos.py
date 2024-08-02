#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos diferentes

#Desafio 35 
#Desenvolva um programa que leia o comprimento de três retas, 
#e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

if reta1 == reta2 and reta1 == reta3 and reta3 == reta2 == 1:
    tipo = 'Equilátero'
elif reta1 != reta2 and reta1 != reta3 and reta3 != reta2 != 1: 
    tipo = 'Escaleno'
else:
    tipo = 'Isóceles'    

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta3 + reta2 > reta1:
    print("Os seguimentos {}, {} e {} formam um triângulo {}.".format(reta1,reta2,reta3,tipo))
else:
    print("Os seguimentos {}, {}, e {} não formam um triângulo!".format(reta1,reta2,reta3))    


