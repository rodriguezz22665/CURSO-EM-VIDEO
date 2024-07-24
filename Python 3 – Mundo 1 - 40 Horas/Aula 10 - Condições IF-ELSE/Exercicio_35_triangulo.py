#Desenvolva um programa que leia o comprimento de três retas, 
#e diga ao usuário se elas podem ou não formar um triângulo.

print("-="*20)
print("ANALISANDO TRIÂNGULOS")
print("-="*20)

reta1 = float(input("Digite o valor da reta 1: "))
reta2 = float(input("Digite o valor da reta 2: "))
reta3 = float(input("Digite o valor da reta 3: "))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta2 > reta1:
    print("É possível criar um triângulo com os três seguimentos acima!")
else:
    print("Não é possível criar um triângulo com os três seguimentos acima!")

    