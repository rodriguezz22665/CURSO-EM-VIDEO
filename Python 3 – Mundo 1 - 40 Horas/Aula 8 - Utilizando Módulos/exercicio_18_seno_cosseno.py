# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 

angulo = float(input("\033[1;7;41mDigite o valor de um ângulo qualquer: \033[m"))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"\033[1;47mO seno de\033[m {angulo:.1f}º\033[1;47m é\033[m {seno:.2f}\033[1;47m, o cosseno é\033[m {cosseno:.2f} \033[1;47me a tangente é\033[m {tangente:.2f}\033[1;47m.\033[m")