#>>>>>>>>>>>>>>>>   Con respecto a partidos politicos   <<<<<<<<<<<<<<<<<<<<<
#Creamos una lista llamada "partidos" donde se llenara con los partidos sin repetir.
#CABE DESTACAR QUE LEEREMOS TODOS LOS ARCHIVOS CON "encoding="utf-8"
partidos=[]
arch2=open("partidos_politicos.txt","r")
linea=arch2.readline().strip()
while linea!="":
    nombre_partido_politico=linea
    if nombre_partido_politico not in partidos:
        partidos.append(nombre_partido_politico)
    linea=arch2.readline().strip()

#>>>>>>>>>>>>>>  Con respecto a las zonas   <<<<<<<<<<<<<<<<<<<<<<
#Creamos dos listas, una para las zonas sin repetir y otra para las regiones sin repetir.
zonas=[]
regiones=[]
arch1=open("zonas.txt","r")
linea=arch1.readline().strip()
while linea!="":
    partes=linea.split(",")
    nombre_zona=partes[0]
    nombre_region=partes[1]
    if nombre_zona not in zonas:
        zonas.append(nombre_zona)
    if nombre_region not in regiones:
        regiones.append(nombre_region)    
    linea=arch1.readline().strip()

#Ahora creamos una lista llamada "parte" para poner la zona y la region a la que pertenece.
parte=[]
arch1=open("zonas.txt","r")
linea=arch1.readline().strip()
while linea!="":
    partes=linea.split(",")
    parte.append(partes)
    linea=arch1.readline().strip()

#Ahora creamos una lista llamada "region2" para ordenar la lista "parte" por su respectiva region.
#ej: [["I","Iquique","Tamarugal]]
region2=[]
for i in range(len(regiones)):
    #Para ello definiremos otra lista para agregar las regiones unicas existentes a la lista.
    region_ciudad=[]
    region_ciudad.append(regiones[i])
    #De esta forma si parte[a][1] (Osea, la region) es igual a regiones[i] entonces que se agregue a "region_ciudad".
    for a in range(len(parte)):
        if parte[a][1]==regiones[i]:
            region_ciudad.append(parte[a][0])
    #Finalizando con añadir "region_ciudad" a la lista "region2" y seguir con el ciclo "for".
    region2.append(region_ciudad)

#>>>>>>>>>>>  CON RESPECTO A LOS CANDIDATOS <<<<<<<<<<<<<
#Para este archivo vamos crear varias listas
arch=open("candidatos.txt","r")
linea=arch.readline().strip()
presidentes=[]
senadores=[]
zonas_candidatos=[]
zonasx=[]
afiliaciones_senadores=[]
afiliaciones_candidatas=[]
afilia=[]
while linea!="":
    partes=linea.split(",")
    nombre_completo=partes[0].strip()
    zona=partes[1]
    afiliacion_politica=partes[2]
    tipo=partes[3].lower()
    #Ahora dividiremos los tipos de candidatos por su tipo (P o S) y los agregaremos a las listas correspondientes
    if tipo=="p":
        if afiliacion_politica in partidos:
            presidentes.append(nombre_completo)
    elif tipo=="s":
        if afiliacion_politica in partidos:
            senadores.append(nombre_completo)
        #Si el candidatos es senador, entonces agregaremos su zona a la lista "zonasx"
            zonasx.append(zona)
        #Ahora rellenamos la lista "afiliaciones_senadores" con las afiliaciones politicas >>>UNICAS<<< de los SENADORES
            if afiliacion_politica in partidos:
                if afiliacion_politica not in afiliaciones_senadores:
                    afiliaciones_senadores.append(afiliacion_politica)
        #Luego añadimos a la lista "afilia" las afiliaciones politicas de cada candidato
            afilia.append(afiliacion_politica)
    #Rellenamos la lista "zonas_candidatos" con la zonan de cada candidato
    if zona not in zonas_candidatos:
        zonas_candidatos.append(zona)
    #Por ultimo, rellenamos la lista "afiliaciones_candidatas" con las afiliaciones politicas >>>UNICAS<<<
    if afiliacion_politica not in afiliaciones_candidatas:
        afiliaciones_candidatas.append(afiliacion_politica)        
    linea=arch.readline().strip()
#print(senadores)
    
#>>>>>>>>>>>>   Con respecto a las votaciones   <<<<<<<<<<<<
#Como siempre creamos listas para rellenarlas con los datos despues
votos_presi=[]
votos_sena1=[]
votos_sena2=[]
zonas_votadas1=[]
zonas_votadas=[]
votos_sena11=[]
votos_sena22=[]
arch3=open("votacion.txt","r")
linea=arch3.readline().strip()
while linea!="":
    partes=linea.split(",")
    nombre_votante=partes[0]
    apellido_votante=partes[1]
    nombre_zona=partes[2]
    voto_presidente=partes[3].strip()
    voto_senador1=partes[4].strip()
    voto_senador2=partes[5].strip()
    #Ahora empezaremos a rellenar las listas anteriormente definidas con su respectivo dato
    votos_presi.append(voto_presidente)
    votos_sena1.append(voto_senador1)
    votos_sena11.append(voto_senador1)
    votos_sena22.append(voto_senador2)
    votos_sena2.append(voto_senador2)
    zonas_votadas1.append(nombre_zona)
    zonas_votadas.append(nombre_zona)
    linea=arch3.readline().strip()
#>>>>>>>> PARA CREAR EL PRIMER TXT  <<<<<<<<<<<
#Definimos una lista llamada "votos" y una variable llamada "s" que sera nuestro sumador de votos totales
votos=[]
s=0
for i in range(len(presidentes)):
    #Dentro del ciclo for, definiremos otra variable llamada "c" que sera nuestro contador de votos a cada presidente
    c=0
    for b in range(len(votos_presi)):
        if votos_presi[b]==presidentes[i]:
            c+=1
            s+=1
    votos.append(c)
#Ahora crearemos una variable de votos de presidentes >>NULOS<< 
votos_presi_nulos=len(votos_presi)-s

#Finalmente, creamos el archivo de texto que se nos pide
out_presidente=open("out_presidente.txt","w")
for i in range(len(presidentes)):
    out_presidente.write(presidentes[i]+","+str(round((votos[i]/len(votos_presi))*100,2))+","+str(round((votos[i]/s)*100,2))+"\n")
out_presidente.close()

#>>>>  PARA CREAR EL TERCER TXT  <<<<<
#Primero crearemos el tercer archivo y luego iremos a por el segundo, ya que nos resulto mas facil
#Creamos una lista llamada "presi_region"
presi_region=[]
cantidadVotoX=[]
#Ahora haremos ciclos for para recorrer los valores
for a in range(len(votos)):
    s=0
    #Definimos una nueva lista como "zonita"
    zonita=[]
#    print(votos[a])
    for i in range(len(votos_presi)):
        if votos_presi[i]==presidentes[a]:
#            print(votos_presi[i])
            #Ahora rellenaremos la lista "zonita con las zonas de los votos para respectivos presidentes
            zonita.append(zonas_votadas[i])
    #creamos una lista llamada "votos_por_region y dentro del for, un contador "c"
    votos_por_region=[]
    cantidad_region=[]
    for a in range(len(region2)):
        c=0
        for i in range(1,len(region2[a])):
            for b in range(len(zonita)):
                if zonita[b]==region2[a][i]:
                    c+=1
#        print(c)
        #Ahora rellenaremos la lista "votos_por_region" con el contador
        votos_por_region.append(c)
        cantidad_region.append(0)
    #y al finalizar el ciclo for añadimos esta lista con los votos a la lista "presi_region"
    presi_region.append(votos_por_region)
    cantidadVotoX.append(cantidad_region)
for a in range(len(presi_region)):
    for b in range(len(presi_region[a])):
        cantidadVotoX[0][b]+=presi_region[a][b]
cantidad_votos_por_region=cantidadVotoX[0]
#Ahora creamos una lista llamada "lista2"
lista2=[]
for a in range(len(votos)):
    #Al recorrer el largo de la lista, vamos añadiendo los valores correspondientes al indice de las listas "presidentes" y "presi_region"
    lista=[]
    lista.append(presidentes[a])
    lista.append(presi_region[a])
    #Por ultimo añadimos esta lista a "lista2"
    lista2.append(lista)

#Y finalmente creamos el tercer archivo
out_presidencia_region=open("out_presidencia_region.txt","w")
for i in range(len(regiones)):
    #¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ IMPORTANTE LEER !!!!!!!!!!!!!!!!!!!!!!!
    #Tuve que discriminar esto porque sino, se hacia division por cero... asi que no imprimira las regiones donde no hayan votos en la region para ningun candidato
    #Tambien tenia una duda con respecto a si la frase "Porcentaje de votos obtenido por el candidato en la región, respecto al total de votos"
    #correspondia a si el porcentaje era por el TOTAL de votos por CADA REGION o en TOTAL por CANDIDATO o por VOTOS TOTALES
    if cantidad_votos_por_region[i]!=0:
        for a in range(len(presidentes)):
            out_presidencia_region.write(regiones[i]+","+str(presidentes[a])+","+str(round((presi_region[a][i]/cantidad_votos_por_region[i])*100,2))+"\n")
    else:
        for a in range(len(presidentes)):
            out_presidencia_region.write(regiones[i]+","+str(presidentes[a])+","+str(round(0.0,2))+"\n")        
out_presidencia_region.close()
#arch3=open("out_presidencia_region.txt","w")
#for i in range(len(regiones)):
#    for a in range(len(presidentes)):
#        arch3.write(regiones[i]+","+str(presidentes[a])+","+str(round((presi_region[a][i]/votos[a])*100,2))+"\n")
#arch3.close()  






#>>>>>>>>>>>>> PARA CREAR EL SEGUNDO TXT  <<<<<<<<<


#Primero definiremos 3 listas:
cantidad_por_partidos=[]
senadores_por_partidos=[]
lugar_por_partidos=[]
for i in range(len(afiliaciones_senadores)):
    #Y dentro de este for otras 2 mas junto a un contador
    senadores_en_partidos=[]
    lugar_de_senadores=[]
    contador=0
    #Volveremos a leer el archivo candidatos.txt para sacar otras variables
    arch=open("candidatos.txt","r")
    linea=arch.readline().strip()
    while linea!="":
        partes=linea.split(",")
        nombre_completo=partes[0].strip()
        zona=partes[1]
        afiliacion_politica=partes[2]
        tipo=partes[3].lower()
        if tipo=="s":
            if afiliacion_politica==afiliaciones_senadores[i]:
                senadores_en_partidos.append(nombre_completo)
                contador+=1
                lugar_de_senadores.append(zona)
        linea=arch.readline().strip()
    lugar_por_partidos.append(lugar_de_senadores)
    senadores_por_partidos.append(senadores_en_partidos)
    cantidad_por_partidos.append(contador)
#Aqui pondremos los nombres repetidos en el voto como "repetido" para luego anular un voto 
    linea=arch3.readline().strip()
    
for a in range(len(votos_sena1)):
    for b in range(len(zonasx)):
        if senadores[b]==votos_sena1[a]:
            if zonasx[b]!=zonas_votadas[a]:
                votos_sena1[a]="repetido"
        if votos_sena1[a] not in senadores:
            votos_sena1[a]="repetido"

for a in range(len(votos_sena1)):
    for b in range(len(zonasx)):
        if senadores[b]==votos_sena2[a]:
            if zonasx[b]!=zonas_votadas[a]:
                votos_sena22[a]="repetido"
        if votos_sena2[a] not in senadores:
            votos_sena2[a]="repetido"
for i in range(len(votos_sena1)):
    if votos_sena1[i]==votos_sena2[i]:
        votos_sena22[i]="repetido"
for a in range(len(votos_sena22)):
    votos_sena2[a]=votos_sena22[a]
for a in range(len(votos_presi)):
    if votos_presi[a] not in presidentes:
        votos_presi[a]="repetido"
    
listx=[]
liscantidad_votos=[]
for b in range(len(zonas)):
    nulos=0
    cantidad_votos=0
    for a in range(len(votos_sena1)):
        if zonas[b]==zonas_votadas[a]:
            cantidad_votos+=3
            if votos_sena1[a]=="repetido":
                nulos+=1
            if votos_sena2[a]=="repetido":
                nulos+=1
            if votos_presi[a]=="repetido":
                if votos_presi[a] not in presidentes:
                   nulos+=1
    listx.append(nulos)
    liscantidad_votos.append(cantidad_votos)

cantidad_votos_no_nulos=[]
for a in range(len(listx)):
    cantidad_votos_no_nulos.append(liscantidad_votos[a]-listx[a])

out_resumen_zona=open("out_resumen_zona.txt","w")
for a in range(len(zonas)):
    if liscantidad_votos[a]!=0:
        out_resumen_zona.write(zonas[a]+","+str(listx[a])+","+str(round(listx[a]/liscantidad_votos[a]*100,2))+","+str(cantidad_votos_no_nulos[a])+","+str(round(cantidad_votos_no_nulos[a]/liscantidad_votos[a]*100,2))+"\n")
    else:
        out_resumen_zona.write(zonas[a]+","+str(listx[a])+","+str(round(0.0,2))+","+str(cantidad_votos_no_nulos[a])+","+str(round(0.0,2))+"\n")
out_resumen_zona.close()


      
#Aqui definimos una matriz de zonas por afiliaciones donde se rellenaran con la cantidad de votos por partido
import numpy as np
matriz=np.zeros([len(zonas),len(afiliaciones_senadores)])
for d in range(len(zonas)):
    for i in range(len(afiliaciones_senadores)):
        c=0
        for a in range(cantidad_por_partidos[i]):
            for b in range(len(votos_sena1)):
                if votos_sena1[b]!="repetido":
                    if zonas[d]==lugar_por_partidos[i][a]:
                        if votos_sena1[b]==senadores_por_partidos[i][a]:
                            if lugar_por_partidos[i][a]==zonas_votadas[b]:
                                c+=1
            for b in range(len(votos_sena2)):
                if votos_sena2[b]!="repetido":
                    if zonas[d]==lugar_por_partidos[i][a]:
                        if votos_sena2[b]==senadores_por_partidos[i][a]:
                            if lugar_por_partidos[i][a]==zonas_votadas[b]:
                                c+=1
        matriz[d][i]=c



##Se sacaran los partidos de mayoria 1 y 2
mayores=[]
mayorafiliacion=[]
for i in range(len(zonas)):
    mayor=0
    listadematriz=[]
    mayorafiliacion=[]
    afiliacionxd=[]
    for a in range(len(afiliaciones_senadores)):
        listadematriz.append(int(matriz[i][a]))
        afiliacionxd.append(afiliaciones_senadores[a])
    for a in range(len(listadematriz)):
        if listadematriz[a]>mayor:
            mayor=listadematriz[a]
    mayorindice=listadematriz.index(mayor)
    mayorafiliacion.append(afiliacionxd[mayorindice])
    listadematriz.pop(mayorindice)
    afiliacionxd.pop(mayorindice)
    mayor=0
    for a in range(len(listadematriz)):
        if listadematriz[a]>mayor:
            mayor=listadematriz[a]
    mayorindice=listadematriz.index(mayor)
    mayorafiliacion.append(afiliacionxd[mayorindice])
    mayores.append(mayorafiliacion)


listavotos=[]
partidozona=[]
senadorzona=[]
for a in range(len(zonas)):
#    print(zonas[a])
    senadorporregion=[]
    partidoporregion=[]
    for b in range(len(afilia)):
        if zonas[a]==zonasx[b]:
            senadorporregion.append(senadores[b])
            partidoporregion.append(afilia[b])
    votosporregion=[]
    contador=0
    for c in range(len(senadorporregion)):
        contador=0
        for d in range(len(votos_sena1)):
            if votos_sena1[d]==senadorporregion[c]:
                    contador+=1

        for d in range(len(votos_sena2)):
                if votos_sena2[d]==senadorporregion[c]:
                        if votos_sena2[d]!="repetido":
                            contador+=1
        votosporregion.append(contador)
    if votosporregion:
        listavotos.append(votosporregion)
    if partidoporregion:
        partidozona.append(partidoporregion)
    if senadorporregion:
        senadorzona.append(senadorporregion)

#---------------------------------------------
out_senadores=open("out_senadores.txt","w")

sumadevotossenadores=[]
for a in range(len(listavotos)):
    suma=0
    for b in range(len(listavotos[a])):
        suma+=listavotos[a][b]
    sumadevotossenadores.append(suma)
#print(sumadevotossenadores)
for a in range(len(listavotos)):
    votosmayoresx=[]
    mayorsenador=[]
    mayor=0
    partidoeliminado=[]
    for b in range(len(listavotos[a])):
        if partidozona[a][b]==mayores[a][0]:
            if listavotos[a][b]>mayor:
                mayor=listavotos[a][b]
    indice=listavotos[a].index(mayor)
    mayorsenador.append(senadorzona[a][indice])
    mayores[a].pop(indice)
    partidoeliminado.append(partidozona[a][indice])
    indicex=[]
    votosmayoresx.append(listavotos[a][indice])
    for y in range(len(partidoeliminado)):
        for x in range(len(partidozona[a])):
            if partidoeliminado[y]==partidozona[a][x]:
                ind=partidozona[a].index(partidoeliminado[y])
                indicex.append(ind)
    for p in range(len(indicex)):
        partidozona[a].pop(indicex[p])
        listavotos[a].pop(indicex[p])
        senadorzona[a].pop(indicex[p])
    mayor=0
    for b in range(len(listavotos[a])):
        if partidozona[a][b]==mayores[a][0]:
            if listavotos[a][b]>mayor:
                mayor=listavotos[a][b]
                indice=listavotos[a].index(mayor)
    votosmayoresx.append(listavotos[a][indice])
    mayorsenador.append(senadorzona[a][indice])
    votosmayoresx.append(listavotos[a][indice])       
    out_senadores.write(zonas[a]+","+mayorsenador[0]+","+str(round(((votosmayoresx[0]/sumadevotossenadores[a])*100),2))+","+mayorsenador[1]+","+str(round(((votosmayoresx[1]/sumadevotossenadores[a])*100),2))+"\n")

out_senadores.close()




#>>>>>>>>>>>>> PARA EL CUARTO TXT  <<<<<<<<<<<<<<<
out_partido_region=open("out_partido_region.txt","w")
#print(matriz)
listaMatReg=[]
liscerosReg=[]
c=0
for a in range(len(zonas)):
    listaMat=[]
    lisceros=[]
    for b in range(len(afiliaciones_senadores)):
        c=matriz[a][b]
        listaMat.append(int(c))
        lisceros.append(0)
    listaMatReg.append(listaMat)
    liscerosReg.append(lisceros)
#print(listaMatReg)
#print(liscerosReg)
#print(len(zonas))
#print(len(listaMatReg))
cantidadCiudadesXRegion=[]
for a in range(len(region2)):
    cantidadCiudadesX=[]
    for b in range(len(region2[a])):
#        print(region2[a][b])
        if region2[a][b] not in regiones:
            cantidadCiudadesX.append(region2[a][b])
    cantidadCiudadesXRegion.append(cantidadCiudadesX)
#print(cantidadCiudadesXRegion)
contador=1
f=0
cccantidad=[]
for a in range(len(cantidadCiudadesXRegion)):
    s=len(cantidadCiudadesXRegion[a])+f
#    print(s)
    ccantidad=[]
    for c in range(len(afiliaciones_senadores)):
        lita=[]
        ocupa=[]
        if contador==1:
            for b in range(s):
                lita.append(listaMatReg[b][c])
        else:
            for b in range(f,s):
                lita.append(listaMatReg[b][c])
#        print(lita)
        sumador=0
        for d in range(len(lita)):
            sumador+=lita[d]
        ccantidad.append(sumador)
    totalx=0
    for i in range(len(ccantidad)):
        totalx+=int(ccantidad[i])
#    print(totalx)
    for d in range(len(afiliaciones_senadores)):
        if totalx!=0:
            out_partido_region.write(regiones[a]+","+afiliaciones_senadores[d]+","+str(round(ccantidad[d]/totalx*100,2))+"\n")
        else:
            out_partido_region.write(regiones[a]+","+afiliaciones_senadores[d]+","+str(round(0.0,2))+"\n")
#    print(ccantidad)
    contador+=1
    f=s
    cccantidad.append(ccantidad)
out_partido_region.close()
#print(cccantidad)
#print(len(cccantidad))
#print(len(region2))












#Glosario:
#    listas importantes:
#    -partidos= partidos existentes para los senadores
#    -zonas= zonas Unicas presentes en zonas.txt
#    -regiones= regiones unicas presentes en zonas.txt
#    -parte= zona+region presentes en el archivo zonas.txt
#    -region2= zonas ordenadas por region en el archivo zonas.txt
#    -presidentes= presidentes en el archivo candidatos.txt
#    -senadores= senadores presentes en el archivo candidatos.txt
#    -zonas_candidatos= zonas de donde pertenecen los candidatos en candidatos.txt
#   -zonansx= zonas donde pertenecen los senadores en candidatos.txt
#   -afiliaciones_senadores= afiliacion politica >>>>UNICAS<<< para los senadores en candidatos.txt
#   -afiliaciones_candidatas= afiliaciones politicas totales para los candidatos en candidatos.txt
#   -afilia= afiliacion de cada uno de los senadores presentes en candidatos.txt
#   -votos_presi=los votos correspondientes a los presidentes (en votacion.txt)
#   -votos_sena1=primer voto para los senadores (en votacion.txt)
#   -votos_sena2=segundo voto para los senadores (en votacion.txt)
#   -zonas_votadas1=zonas de los candidatos votados (en votacion.txt)
#   -zonas_votadas=zonas de los candidatos votados (en votacion.txt)
#   -votos: votos recibidos por cada presidente (respecto al indice de presidentes)
#   -presi_region= lista de listas, contiene dentro una lista de votos por region por cada candidato de presidente
#   -lista2= lista de listas con una lista dentro, contiene dentro una lista con el nombre del candidato y una lista con sus votos por region
#   -cantidad_votos_por_region= contiene el numero de votos de presidente por cada region
#   -cantidad_por_partidos: cantidad de senadore en cada partido
#   -senadores_por_partidos: senadores ordenados por partidos
#   -lugar_por_partidos: lugar del senador ordenado por partidos
#   -matriz: Contiene los votos de los partidos por zonas
#   -mayores: lista de listas, contiene los dos mayores partidos por zona
#   -listavotos: lista de listas, contiene los votos de las personas por partido
#   -partidozona: lista de listas, contiene los partidos votados por zona
#   -senadorzona: lista de listas, contiene el senador del partido por zona