#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input("Digite um número para vizualizar a sua taboada: "))

for c in range (1,11):
    print("{} x {} = {}".format(num,c,num*c))