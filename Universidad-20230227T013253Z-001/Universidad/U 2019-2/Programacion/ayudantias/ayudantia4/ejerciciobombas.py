#
arch=open("dispositivos.txt")
linea=arch.readline().strip()
c=0
seg=0
while linea!="":
    partes=linea.split(",")
    c+=1
    num=int(partes[0])
    r=0
    a=0
    n=0
    if num==3:
        print("El dispositivo",str(c),"tiene 3 cables")
        partes=linea.split(",")
        color1=partes[1]
        color2=partes[2]
        color3=partes[3]
        if color1!="Rojo" and color2!="Rojo" and color3!="Rojo":
            seg+=1
            print("Cortar el segundo cable:",color2)
        elif color3=="Blanco":
            print("Cortar el tercer cable:",color3)
        elif color1=="Azul" and color2=="Azul":
            seg+=1
            print("Cortar el segundo cable: azul")
        else:
            print("Cortar el tercer cable:",color3)
    elif num==4:
        print("El dispositivo",str(c),"tiene 4 cables")
        partes=linea.split(",")
        color1=partes[1]
        color2=partes[2]
        color3=partes[3]
        color4=partes[4]
        if color1=="Rojo":
            r+=1
        if color2=="Rojo":
            r+=1
        if color3=="Rojo":
            r+=1
        if color4=="Rojo":
            r+=1
        if r>1:
            print("Cortar el cable 4:",color4)
        elif color4=="Amarillo" and r==0:
            print("Cortar el cable 4:",color4)
        elif r==1:
            print("Cortar el segundo cable:",color2)
            seg+=1
        elif color2=="Amarillo" and color3=="Amarillo":
            print("Cortar el cable 4:",color4)
        else:
            print("Cortar el tercer cable:",color3)
    elif num==5:
         print("El dispositivo",str(c),"tiene 5 cables")
         partes=linea.split(",")
         color1=partes[1]
         color2=partes[2]
         color3=partes[3]
         color4=partes[4]
         color5=partes[5]
         if color1=="Amarillo":
             a+=1
         if color2=="Amarillo":
             a+=1
         if color3=="Amarillo":
             a+=1
         if color4=="Amarillo":
             a+=1
         if color5=="Amarillo":
             a+=1
         if color1=="Negro":
             n+=1
         if color2=="Negro":
             n+=1
         if color3=="Negro":
             n+=1
         if color4=="Negro":
             n+=1
         if color5=="Negro":
             n+=1
         if color5=="Negro":
             print("Cortar el cuatro cable",color4)
         elif color3=="Rojo" and a>1:
             print("Cortar el tercer cable",color3)
         elif n==0:
             seg+=1
             print("cortar el segundo cable",color2)
         else:
             print("Cortar el primer cable",color1)
            
    linea=arch.readline().strip()
porc=(100*(seg/c))
print("Fueron encontrados",c,"dispositivos")
print("El cable 2 se corto",seg,"veces")
print(porc,"% del total")                