#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("PRIMEIRO TERMO: "))
razao = int(input("RAZÃO: "))
pa = termo 
c = 1

while c <= 10:
    c += 1
    print('PA = ' if c == 2 else ' -> ', end='')
    print(pa, end='')
    pa = pa + razao 
    
print(' -> FIM', end='')

#SOLUCAO PROFESSOR GUANABARA:

'''print('Gerador de PA')
print('-=' * 10)

primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input("RAZÃO: "))
termo = primeiro
count = 1
while count <= 10:
    print("{} -> ".format(termo), end='')
    count += 1
    termo += razao
print('FIM')'''
    