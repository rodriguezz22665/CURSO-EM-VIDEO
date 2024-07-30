#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input("\033[32;40mDigite o valor do salário do colaborador:\033[m R$ "))

novo_sal = salario + (salario * 0.15)

print("\033[1;42mCom aumento de 15% o salário deste colaborador foi de R$ {} para R$ {:.2f}\033[m".format(salario,novo_sal))