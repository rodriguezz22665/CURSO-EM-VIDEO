#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
'''a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Cruzeiro'''

print('{:=^80}'.format(" TABELA DO CAMPEONATO BRASILEIRO "))

tabela = ('Botafogo','Palmeiras','Fortaleza','Flamengo',
          'São Paulo','Bahia','Cruzeiro','Internacional','Atlético-MG','Vasco','Bragantino','Juventude','Criciúma','Grêmio','Athletico-PR','Vitória','Corinthians','Fluminense','Cuiabá','Atlético-GO')

print('='*80)
print(f'Lista dos times do Brasileirão: {tabela}')
print('='*80)
print(f'Os 5 primeiros colocados são: {tabela[:5]}')
print('='*80)
print(f'Os 4 últimos colocados são: {tabela[16:]}')
print('='*80)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('='*80)
print(f'O Cruzeiro está na {tabela.index("Cruzeiro")+1}º posição.')
print('='*80)
