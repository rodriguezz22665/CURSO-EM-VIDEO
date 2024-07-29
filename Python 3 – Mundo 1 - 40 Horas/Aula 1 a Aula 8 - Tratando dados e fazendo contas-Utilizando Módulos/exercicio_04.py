#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')

cores = {'vermelho': '\033[31m','azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'roxo':'\033[35m', 'cinza': '\033[37m', 'lilas': '\033[36m', 'limpa': '\033[m'}

print("{}O tipo primitivo deste valor é:{} {}".format(cores['vermelho'],cores['limpa'],type(algo)))

print("{}Essa variável tem valor?{} {}".format(cores['azul'],cores['limpa'],bool(algo)))

print("{}É um número?{} {}".format(cores['verde'],cores['limpa'],algo.isnumeric()))

print("{}É composto apenas por letra?{} {}".format(cores['amarelo'],cores['limpa'],algo.isalpha()))

print("{}É composto por letra e número?{} {}".format(cores['roxo'],cores['limpa'],algo.isalnum()))

print("{}Está capitalizado?{} {}".format(cores['cinza'],cores['limpa'],algo.isupper()))

print("{}Está em minúsculas?{} {}".format(cores['lilas'],cores['limpa'],algo.islower()))
