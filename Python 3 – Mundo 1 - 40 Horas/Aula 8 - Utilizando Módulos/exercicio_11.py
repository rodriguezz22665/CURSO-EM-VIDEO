#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Qual a largura da parede em metros? "))

altura = float(input("Qual a altura da parede em metros? "))

area = altura * largura 

tinta = area/2

print("Sua parede tem a dimensão de {} x {} e sua área é de {} metros quadrados.".format(largura,altura,area))

print("Para pintar essa parede, você precisará de {}L de tinta.".format(tinta))