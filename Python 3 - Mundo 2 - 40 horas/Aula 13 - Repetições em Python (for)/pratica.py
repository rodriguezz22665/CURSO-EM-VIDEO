from time import sleep

for c in range(0,6):
    print(c)
print("FIM")

for c in range (6,0,-1):
    print(c)
print('FIM')    

for c in range(0,10,2):
    print(c)
print("FIM")    

n = int(input("Digite um número inteiro: "))

for c in range (0,n+1):
    print(c)
    sleep(0.5)
print("FIM")    


i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for c in range (i, f+1, p):
    print(c)
    sleep(0.5)
print("FIM")    

soma = 0

for c in range (0,5+1):
    n = int(input("Digite um número inteiro: "))
    soma += n
print("A soma de todos os valores foi {}".format(soma))    