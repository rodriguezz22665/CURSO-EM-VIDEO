#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

cores = {'vermelho': '\033[31m','azul': '\033[34m', 'verde': '\033[32m', 'amarelo': '\033[33m', 'roxo':'\033[35m', 'cinza': '\033[37m', 'lilas': '\033[36m', 'limpa': '\033[m'}

dist = float(input("\033[35;46mDigite alguma distância em metros:\033[m "))

dam = dist/10
hm = dist/100
km = dist/1000
dm = dist*10
cm = dist*100
mm = dist*1000  

print("A medida de {}{} m{} corresponde a: ".format(cores['lilas'],dist,cores['limpa']))

print("\033[36m{} dam\n {} hm\n {} km\n {} dm\n {:.0f} cm\n {:.0f} mm\033[m\n".format(dam,hm,km,dm,cm,mm))


