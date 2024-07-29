# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 

angulo = float(input("Digite o valor de um ângulo qualquer: "))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O seno de {angulo}º é {seno:.2f}, o cosseno é {cosseno:.2f} e a tangente é {tangente:.2f}.")