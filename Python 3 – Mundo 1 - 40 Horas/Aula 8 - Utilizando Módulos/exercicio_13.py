#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input("Digite o valor do salário do colaborador: R$ "))

novo_sal = salario + (salario * 0.15)

print("Com aumento de 15% o salário deste colaborador foi de R$ {} para R$ {:.2f}".format(salario,novo_sal))