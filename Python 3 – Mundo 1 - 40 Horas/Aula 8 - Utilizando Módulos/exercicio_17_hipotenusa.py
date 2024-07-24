# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.

# Importar biblioteca
from math import hypot, sqrt 

# Ler o comprimento do cateto oposto
cateto_oposto = float(input("Digite o comprimento do cateto oposto do triângulo retângulo: "))

# Ler o comprimento do cateto adjacente
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente do triângulo retângulo: "))

# Criar uma fórmula para calcular o comprimento da hipotenusa
# O cálculo da hipotenusa é enunciado pelo Teorema de Pitágoras, 
# que diz: “A hipotenusa é igual à raiz quadrada da soma dos catetos ao quadrado”.

#resulucao original:
#cateto_soma = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
#hipotenusa = math.sqrt(cateto_soma) 

#resolucao guanabara:

hipot = hypot(cateto_oposto, cateto_adjacente)

# Exibir o comprimento da hipotenusa 
print(f"O comprimento da hipotenusa é: {hipot:.2f}")
