#Marcelo Guerra Dubó
#Brayan Maldonado Carrasco

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def diagnosticoExamen(diag,tEx,mes,rut): #Funcion que nos ayudara a calcular el diagnostico de un paciente cualquiera recibiendo 3 parametros
                                         #diag = "prediagnostico del examen";tEx = "el tipo de examen";mes = "El mes en que se lo realizó" ; rut= "rut de la persona".   
    arch2=open("examenes.txt","r",encoding='utf-8') #Abrimos el archivo de texto llamado "examenes.txt".
    linea2=arch2.readline().strip() #Leemos
    valores=["",""] #Esta lista nos servira para poder dividir la presion sistólica y presion diastólica.
    exa=[] #Esta lista nos servira para dividir el valor del prediagnostico de la "Presion Arterial".
    while linea2 != "":
        partes=linea2.split(",")
        tipoEx=partes[0]         
        valorNormal=partes[1]
        valorAlterado=partes[2]
        diagnostico=partes[3]
        if tipoEx == "P": #Presion Arterial.
            valores[0]=valorNormal.split("/")   #En valorNormal independizamos la presion sistólica de la presion diastólica.
            valores[1]=valorAlterado.split("/") #En valorAlterado independizamos la presion sistólica de la presion diastólica.
            if tEx=="P":
                exa.append(diag.split("/")) #independizamos la presion sistólica de la presion diastólica del Diagnostico de una persona.
                x="" #Esta variable va a contener una lista con el diagnostico,el tipo de examen, mes y el rut de una persona.
                if int(exa[0][0]) >= int(valores[1][0]) or int(exa[0][1])>= int(valores[1][1]): #Comparamos para saber si el Diagnostico de la persona es Alterado
                    x=[diagnostico,tEx,mes,rut]
                elif int(exa[0][0]) <= int(valores[0][0]) or int(exa[0][1]) <= int(valores[0][1]): #Comparamos para saber si el Diagnostico de la persona esta Normal
                    x=["NORMAL",tEx,mes,rut]   
                else:
                    x=["PRECAUCIÓN",tEx,mes,rut]    #Diagnostico Precaución si el resultado no es Normal ni Alterado.

        if tipoEx=="C" and tEx=="C":    #Colesterol.
            x=""    #Esta variable va a contener una lista con el diagnostico,el tipo de examen, mes y el rut de una persona.
            if int(diag) >= int(valorAlterado): ##Comparamos para saber si el Diagnostico de la persona es Alterado.
                x=[diagnostico,tEx,mes,rut]
            if int(diag) < int(valorAlterado) and int(diag) > int(valorNormal): ##Comparamos para saber si el Diagnostico de la persona esta en Precaución.
                x=["PRECAUCIÓN",tEx,mes,rut]
            if int(diag) <= int(valorNormal):   ##Comparamos para saber si el Diagnostico de la persona es Normal.
                x=["NORMAL",tEx,mes,rut]    

        if tipoEx=="G" and tEx=="G":    #Curva de tolerancia a la glucosa.
            x=""    #Esta variable va a contener una lista con el diagnostico,el tipo de examen, mes y el rut de una persona.
            if int(diag)>= int(valorAlterado): #Comparamos para saber si el Diagnostico de la persona es Alterado.
                x=[diagnostico,tEx,mes,rut]
            if int(diag) < int(valorAlterado) and int(diag) > int(valorNormal): #Comparamos para saber si el Diagnostico de la persona esta en Precaición.
                x=["PRECAUCIÓN",tEx,mes,rut]
            if int(diag) <= int(valorNormal):   #Comparamos para saber si el Diagnostico de la persona es Normal.
                x=["NORMAL",tEx,mes,rut]
              
        linea2=arch2.readline().strip() 
    return x   



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
def porcentajeNormal(resultados,tEx):   #función que nos ayuda a calcular porcentaje de personas que 
                                        #en su último chequeo del año lograron niveles normales.
    listaA=[]   #rut de las personas que se hicieron el examen
    listaB=[]   #Ultimo resultado del año en cuanto al examen
    porcentaje=0
    for i in range(len(meses)): 
        for j in range(len(resultados)):    
            if resultados[j][2] == meses[i]:    #Separamos por meses. 
                if resultados[j][1] == tEx: #Separamos por tipo de Examen.
                    if resultados[j][3] not in listaA:
                        listaA.append(resultados[j][3]) #Agregamos los rut dependiendo del tipo de Examen.  
                        listaB.append(resultados[j][3]) 
                    for a in range(len(listaA)):
                        if resultados[j][3] == listaA[a]:   #Comparamos los rut.
                            listaB[a] = resultados[j][0] #Guardamos el diagnostico en la posicion del rut.
    cont=0
    for b in range(len(listaA)): #Recorremos la lista para saber cuantos diagnosticos nos dan Normal. 
        if listaB[b] == "NORMAL":
            cont+=1
    porcentaje=(round((cont/len(listaA))*100)) #Sacamos porcentaje de los diagnosticos con resultado Normal.
    
    return porcentaje
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                
arch=open("pacientes.txt","r")  #Abrimos el archivo de texto llamado "pacientes.txt".
linea=arch.readline().strip()   #leemos
rutPaciente=[]  
nombrePaciente=[]
edadPaciente=[]
sexoPaciente=[]
#Definimos 4 listas que contendran los datos de los pacientes.
while linea!= "":
    partes=linea.split(",")
    rut=partes[0]    #rut paciente.
    nombre=partes[1] #nombre paciente.
    sexo=partes[2]   #sexo paciente.
    edad=int(partes[3]) #edad paciente.
    
    rutPaciente.append(rut)
    nombrePaciente.append(nombre)
    edadPaciente.append(edad)
    sexoPaciente.append(sexo)
    #Agregamos a las listas previamente creadas los datos de lectura.
    linea=arch.readline().strip()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
arch3=open("registro.txt","r")  #Abrimos el archivo de texto llamado "registro.txt".
linea3=arch3.readline().strip() #Leemos.
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
#Creamos una lista con los meses.
resultados=[]   #Creamos una lista que contendra los diagnosticos, tipo de examen, mes y rut. 
while linea3 != "":
    partes=linea3.split(",")
    orden=(partes[0])       
    if orden != "O": #Discriminamos con la letra "O" ya que no nos entrega los resultados especificos de cada orden.
        rutP=partes[0]
        mes=partes[1]
        examen=partes[2]
        result=partes[3]
        resultados.append(diagnosticoExamen(result,examen,mes,rutP))    #Agregamos a la lista "resultados" los examenes hechos, evaluados por la funcion antes creada. 
        
    linea3=arch3.readline().strip()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Diagnostico.txt ; este codigo nos dara el archivo de salida como se observa en el archivo ejemplo entregado

#/////////////////////////////////////////<>\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                
                
diagnostico=open("diagnostico.txt","w") #Creamos el archivo "txt" de salida.

diagnostico.write("Presión Arterial"+"\n")  #Agregamos al archivo de salida.
for i in range(len(meses)):
    diagnostico.write(meses[i]+"\n")    #Agregamos al archivo de salida separando por meses.
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:    #Separamos por meses.
            if resultados[j][1] == "P": #Separamos por Presion Arterial.
                diagnostico.write(str(resultados[j][3])+","+str(nombrePaciente[rutPaciente.index(resultados[j][3])])+","+str(resultados[j][0])+"\n")
                #Agregamos al archivo de salida separado por rut, nombre de paciente y su diagnostico.

diagnostico.write("Colesterol"+"\n")
for i in range(len(meses)):
    diagnostico.write(meses[i]+"\n")    #Agregamos al archivo de salida separando por meses.
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "C": #Separamos por Colesterol.
                diagnostico.write(str(resultados[j][3])+","+str(nombrePaciente[rutPaciente.index(resultados[j][3])])+","+str(resultados[j][0])+"\n")
                #Agregamos al archivo de salida separado por rut, nombre de paciente y su diagnostico.

diagnostico.write("Curva de Tolerancia a la Glucosa"+"\n")
for i in range(len(meses)):
    diagnostico.write(meses[i]+"\n")    #Agregamos al archivo de salida separando por meses.
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "G": #Separamos por Curva de Tolerancia a la Glucosa.
                diagnostico.write(str(resultados[j][3])+","+str(nombrePaciente[rutPaciente.index(resultados[j][3])])+","+str(resultados[j][0])+"\n")
                #Agregamos al archivo de salida separado por rut, nombre de paciente y su diagnostico.

diagnostico.close() #Cerrramos el archivo "txt".

#/////////////////////////////////////////<>\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#Estadisticas.txt ;  este codigo nos dara el archivo de salida como se observa en el archivo ejemplo entregado

#/////////////////////////////////////////<>\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

estadisticas=open("estadisticas.txt","w")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# "A"
#Calculamos la cantidad de exámenes hechos por mes y por tipo.

estadisticas.write("*A*"+"\n") #Creamos el archivo "txt" de salida.

estadisticas.write("Presión Arterial"+"\n")
for i in range(len(meses)):
    cont=0 #cantidad examenes hechos, separados por mes y por tipo  
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "P": #Separamos por Presion Arterial
                cont+=1 #Agregamos al contador.
    estadisticas.write(str(meses[i]+","+str(cont))+"\n")    #Agregamos al archivo de salida separados por meses la cantidad examenes totales de Presion Arterial.
      
estadisticas.write("Colesterol"+"\n")
for i in range(len(meses)):
    cont=0 #cantidad examenes hechos, separados por mes y por tipo  
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "C": #Separamos por Colesterol
                cont+=1 #Agregamos al contador.
    estadisticas.write(str(meses[i]+","+str(cont))+"\n")    #Agregamos al archivo de salida separados por meses la cantidad examenes totales de Colesterol.

estadisticas.write("Curva de Tolerancia a la Glucosa"+"\n")
for i in range(len(meses)):
    cont=0 #cantidad examenes hechos, separados por mes y por tipo  
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "G": #Separamos por Curva de Tolerancia a la Glucosa
                cont+=1 #Agregamos al contador.
    estadisticas.write(str(meses[i]+","+str(cont))+"\n")    #Agregamos al archivo de salida separados por meses la cantidad examenes totales de Curva de Tolerancia a la Glucosa.    

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# "B"
#Calculamos porcentaje de pacientes con resultado normal, con resultado precaución y con resultado alterado.

estadisticas.write("*B*"+"\n")
estadisticas.write("Presión Arterial"+"\n")
for i in range(len(meses)):
    cont=0  #cantidad total de examenes tipo Presion Arterial hechos 
    norm=0  # contador de casos con Presion Arterial  en condicion "Normal"
    prec=0  # contador de casos con Presion Arterial  en condicion "Precaucion"
    alt=0   # contador de casos con Presion Arterial  en condicion "Alterado" 
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "P":
                cont+=1
                if resultados[j][0]=="NORMAL":  #Separamos los casos de Presion Arterial en condicion Normal y lo agregamos al contador.
                    norm+=1
                elif resultados[j][0]=="PRECAUCIÓN":    #Separamos los casos de Presion Arterial en condicion Precaución y lo agregamos al contador.
                    prec+=1
                else:
                    alt+=1  #Agregamos al contador los casos de Presion Arterial en condicion Alterado.
    if cont==0: #Discriminamos para evitar error de division por cero.
        estadisticas.write(str(meses[i])+","+str(0)+"%,"+str(0)+"%,"+str(0)+"%"+"\n")   #Agregamos al archivo de salida los porcentajes separados por Presion Arterial y ordenado por Normal, Precaución y Alterado.
    else:
        estadisticas.write(str(meses[i])+","+str(round(((norm/cont)*100),))+"%,"+str(round(((prec/cont)*100),))+"%,"+str(round(((alt/cont)*100),))+"%"+"\n")    #Agregamos al archivo de salida los porcentajes separados por Presion Arterial y ordenado por Normal, Precaución y Alterado.
      
estadisticas.write("Colesterol"+"\n")
for i in range(len(meses)):
    cont=0  #cantidad total de examenes tipo Colesterol hechos   
    norm=0  # contador de casos con Colesterol  en condicion "Normal"
    prec=0  # contador de casos con Colesterol  en condicion "Precaucion"
    alt=0   # contador de casos con Colesterol  en condicion "Alterado" 
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "C":
                cont+=1
                if resultados[j][0]=="NORMAL":  #Separamos los casos de Colesterol en condicion Normal y lo agregamos al contador.
                    norm+=1
                elif resultados[j][0]=="PRECAUCIÓN":    #Separamos los casos de Colesterol en condicion Precaución y lo agregamos al contador.
                    prec+=1
                else:
                    alt+=1  #Agregamos al contador los casos de Colesterol en condicion Alterado.
    if cont==0: #Discriminamos para evitar error de division por cero.
        estadisticas.write(str(meses[i])+","+str(0)+"%,"+str(0)+"%,"+str(0)+"%"+"\n")   #Agregamos al archivo de salida los porcentajes separados por Colesterol y ordenado por Normal, Precaución y Alterado.   
    else:
        estadisticas.write(str(meses[i])+","+str(round(((norm/cont)*100),))+"%,"+str(round(((prec/cont)*100),))+"%,"+str(round(((alt/cont)*100),))+"%"+"\n")    #Agregamos al archivo de salida los porcentajes separados por Colesterol y ordenado por Normal, Precaución y Alterado.

estadisticas.write("Curva de Tolerancia a la Glucosa"+"\n")
for i in range(len(meses)):
    cont=0  #cantidad total de examenes tipo Curva de Tolerancia a la Glucosa hechos   
    norm=0  # contador de casos con Curva de Tolerancia a la Glucosa  en condicion "Normal"
    prec=0  # contador de casos con Curva de Tolerancia a la Glucosa  en condicion "Precaucion"
    alt=0   # contador de casos con Curva de Tolerancia a la Glucosa  en condicion "Alterado" 
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:
            if resultados[j][1] == "G":
                cont+=1
                if resultados[j][0]=="NORMAL":  #Separamos los casos de Curva de Tolerancia a la Glucosa en condicion Normal y lo agregamos al contador.
                    norm+=1
                elif resultados[j][0]=="PRECAUCIÓN":    #Separamos los casos de Curva de Tolerancia a la Glucosa en condicion Precaución y lo agregamos al contador.
                    prec+=1
                else:
                    alt+=1  #Agregamos al contador los casos de Curva de Tolerancia a la Glucosa en condicion Alterado.
    if cont==0: #Discriminamos para evitar error de division por cero.
        estadisticas.write(str(meses[i])+","+str(0)+"%,"+str(0)+"%,"+str(0)+"%"+"\n")   #Agregamos al archivo de salida los porcentajes separados por Curva de Tolerancia a la Glucosa y ordenado por Normal, Precaución y Alterado.
    else:
        estadisticas.write(str(meses[i])+","+str(round(((norm/cont)*100),))+"%,"+str(round(((prec/cont)*100),))+"%,"+str(round(((alt/cont)*100),))+"%"+"\n")    #Agregamos al archivo de salida los porcentajes separados por Curva de Tolerancia a la Glucosa y ordenado por Normal, Precaución y Alterado.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# "C"
#Calculamos los porcentaje de personas que en su último resultado del año lograron niveles normales.

estadisticas.write("*C*"+"\n")
estadisticas.write("Presión Arterial"+"\n")
estadisticas.write(str(porcentajeNormal(resultados,"P"))+"%"+"\n")

estadisticas.write("Colesterol"+"\n")
estadisticas.write(str(porcentajeNormal(resultados,"C"))+"%"+"\n")

estadisticas.write("Curva de Tolerancia a la Glucosa"+"\n")
estadisticas.write(str(porcentajeNormal(resultados,"G"))+"%"+"\n")

#Agregamos al archivo de salida los porcentajes calculados en la funcion previamente creada, separados por el tipo de Examen.
 
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# "D"
#Calculamos los Porcentaje de personas mayores de 40 años que tienen más de un resultado alterado o con precaución al finalizar el año
 
rutPresion=[]   #rut de las personas que se hicieron el examen de Presión Arterial
resultP=[]   #Ultimo resultado del año en cuanto al examen de Presión Arterial 
rutColesterol=[]   #rut de las personas que se hicieron el examen de Colesterol
resultC=[]   #Ultimo resultado del año en cuanto al examen de Colesterol y que se intercambiaran con el diagnostico
rutGlucosa=[]   #rut de las personas que se hicieron el examen de Curva de Tolerancia a la Glucosa
resultG=[]   #Ultimo resultado del año en cuanto al examen de Curva de Tolerancia a la Glucosa y que se intercambiaran con el diagnostico
sexo=[] #En esta lista guardaremos los sexos de las personas con resultados Alterados o con precaución
edad=[] #En esta lista guardaremos los edad de las personas con resultados Alterados o con precaución

for i in range(len(meses)):
    for j in range(len(resultados)):
        if resultados[j][2] == meses[i]:    #Separamos por meses. 
            if resultados[j][1] == "P" :    #Separamos por tipo de Examen "Presión Arterial".
                if resultados[j][3] not in rutPresion:
                    rutPresion.append(resultados[j][3])
                    resultP.append(resultados[j][3])
                for a in range(len(rutPresion)):
                    if resultados[j][3] == rutPresion[a]:
                        resultP[a] = resultados[j][0]   #Guardamos el diagnostico en la posicion del rut.
            if resultados[j][1] == "C" :    #Separamos por tipo de Examen "Colesterol".
                if resultados[j][3] not in rutColesterol:
                    rutColesterol.append(resultados[j][3])
                    resultC.append(resultados[j][3])
                for a in range(len(rutColesterol)):
                    if resultados[j][3] == rutColesterol[a]:
                        resultC[a]=resultados[j][0] #Guardamos el diagnostico en la posicion del rut.
            if resultados[j][1] == "G" :    #Separamos por tipo de Examen "Curva de Tolerancia a la Glucosa".
                if resultados[j][3] not in rutGlucosa:
                    rutGlucosa.append(resultados[j][3])
                    resultG.append(resultados[j][3])
                for a in range(len(rutGlucosa)):
                    if resultados[j][3] == rutGlucosa[a]:
                        resultG[a]=resultados[j][0] #Guardamos el diagnostico en la posicion del rut.
                        
for a in range(len(rutPresion)):
    for b in range(len(rutColesterol)):
        for c in range(len(rutGlucosa)):
            #Recorremos las 3 listas que contenian rut de los examenes de Presion, Colesterol y de Glucosa
            if rutPresion[a]==rutColesterol[b] and rutPresion[a]==rutGlucosa[c]:    #Comparamos los rut de las 3 listas 
                if (resultP[a] != "NORMAL" and resultC[b] !="NORMAL") or (resultP[a] !="NORMAL" and resultG[c]!= "NORMAL") or (resultC[a]!="NORMAL" and resultG[c]!= "NORMAL"):
                #Separamos los diagnosticos que sean distintos al Normal, para saber cuantas personas tiene mas de un diagnostico Alterado o con Precaución.
                    sexo.append(sexoPaciente[rutPaciente.index(rutPresion[a])]) #Agregamos los sexos de las personas con mas de un diagnostico Alterado o con Precaución.
                    edad.append(edadPaciente[rutPaciente.index(rutPresion[a])]) #Agregamos la edad de las personas con mas de un diagnostico Alterado o con Precaución.
                    
contTotal_Masc=0    #Contador total de pacientes Masculinos
contTotal_Fem=0 #Contador total de pacientes Femeninos
for i in range(len(sexoPaciente)):  #Recorremos las lista que contiene el sexo de todos los pacientes
    if sexoPaciente[i]=="F":    #Separamos por sexo Femenino a los pacientes y lo agregamos al contador.
        contTotal_Fem+=1
    if sexoPaciente[i]=="M":    #Separamos por sexo Masculino a los pacientes y lo agregamos al contador.
        contTotal_Masc+=1
contFem=0   #Contador de pacientes Femeninos mayores a 40 años con mas de un resultado Alterado o con Precaución.
contMasc=0  #Contador de pacientes Masculinos mayores a 40 años con mas de un resultado Alterado o con Precaución.
for l in range(len(sexo)):  #Recorremos las lista que contiene el sexo de todos los pacientes mayores a 40 con mas de un resultado Alterado o con Precaución.
    if sexo[l]=="F":    #Separamos por sexo Femenino a los pacientes y lo agregamos al contador.
        if edad[l] >= 40:
            contFem+=1
    if sexo[l]=="M":    #Separamos por sexo Masculino a los pacientes y lo agregamos al contador.
        if edad[l] >= 40: 
            contMasc+=1

#Al final agregamos al archivo "txt" de salida los porcentajes de mujeres y hombres mayores a 40 años con mas de un resultado Alterado o con Precaución
estadisticas.write("*D*"+"\n")
estadisticas.write("Mujeres "+str(round((contFem/contTotal_Fem)*100))+"%"+"\n")
estadisticas.write("Hombres "+str(round((contMasc/contTotal_Masc)*100))+"%"+"\n") 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

estadisticas.close()    #Cerramos el archivo "txt" de salida

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 