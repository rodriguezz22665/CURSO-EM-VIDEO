

algo = input('Digite algo: ')


print("O tipo primitivo deste valor é: {}".format(type(algo)))

print("Essa variável tem valor? {}".format(bool(algo)))

print("É um número? {}".format(algo.isnumeric()))

print("É composto apenas por letra? {}".format(algo.isalpha()))

print("É composto por letra e número? {}".format(algo.isalnum()))

print("Está capitalizado? {}".format(algo.isupper()))

print("Está em minúsculas? {}".format(algo.islower()))
