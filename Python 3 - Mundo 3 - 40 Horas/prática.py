lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#tuplas são imutáveis 
print(lanche[1])
print(lanche[:2])
print(lanche[1:])
print("="*40)

for comida in lanche:
    print(f'- Eu vou comer {comida}')
print("="*40)    

for posicao, comida in enumerate(lanche):
    print(f'-- Eu vou vou comer {comida} na posição {posicao}')    
print("="*40)

for cont in range (0, len(lanche)):
    print(f'--- Eu vou comer {lanche[cont]} na posição {cont}')    
print("="*40)

#Mostrar organizado por ordem alfabética
print(sorted(lanche))    
