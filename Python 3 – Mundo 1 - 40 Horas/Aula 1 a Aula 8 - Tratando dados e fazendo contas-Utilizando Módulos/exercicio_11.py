#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("\033[7;31;40mQual a largura da parede em metros?\033[m "))

altura = float(input("\033[7;32;40mQual a altura da parede em metros?\033[m "))

area = altura * largura 

tinta = area/2

print("\033[1;31mSua parede tem a dimensão de {} x {} e sua área é de {} metros quadrados.\033[m".format(largura,altura,area))

print("\033[32mPara pintar essa parede, você precisará de {}L de tinta.\033[m".format(tinta))