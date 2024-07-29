dist = float(input("Digite alguma distância em metros: "))

dam = dist/10
hm = dist/100
km = dist/1000
dm = dist*10
cm = dist*100
mm = dist*1000  

print("A medida de {} m corresponde a: ".format(dist))

print("{} dam\n {} hm\n {} km\n {} dm\n {:.0f} cm\n {:.0f} mm\n".format(dam,hm,km,dm,cm,mm))


