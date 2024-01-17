# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""



def diagnosticoExamen(examen,tEx,mes):
    arch2=open("examenes.txt","r",encoding='utf-8')
    linea2=arch2.readline().strip()
    valores=["",""]
    exa=[]
    while linea2 != "":
        partes=linea2.split(",")
        tipoEx=partes[0]
        valorNormal=partes[1]
        valorAlterado=partes[2]
        diagnostico=partes[3]

        if tipoEx=="P":
            valores[0]=valorNormal.split("/")
            valores[1]=valorAlterado.split("/")  
            if tEx=="P":
                exa.append(examen.split("/"))
                x=""
                if int(exa[0][0]) >= int(valores[1][0]) or int(exa[0][1])>= int(valores[1][1]):
                    x=[diagnostico,tEx,mes]
                elif int(exa[0][0]) <= int(valores[0][0]) or int(exa[0][1]) <= int(valores[0][1]) :
                    x=["NORMAL",tEx,mes]
                else:
                    x=["PRECAUCIÓN",tEx,mes]   

        if tipoEx=="C" and tEx=="C":
            x=""
            if examen>=valorAlterado:
                x=[diagnostico,tEx,mes]
            if examen<valorAlterado and examen>valorNormal:
                x=["PRECAUCIÓN",tEx,mes]
            if examen<=valorNormal:
                x=["NORMAL",tEx,mes]    

        if tipoEx=="G" and tEx=="G":
            x=""
            if examen>=valorAlterado:
                x=[diagnostico,tEx,mes]
            if examen<valorAlterado and examen>valorNormal:
                x=["PRECAUCIÓN",tEx,mes]
            if examen<=valorNormal:
                x=["NORMAL",tEx,mes]
              
        linea2=arch2.readline().strip() 
    return x  
    
arch=open("pacientes.txt","r")
linea=arch.readline().strip()
rutPaciente=[]
nombrePaciente=[]
edadPaciente=[]
sexoPaciente=[]
while linea!= "":
    partes=linea.split(",")
    rut=partes[0]
    nombre=partes[1]
    sexo=partes[2]
    edad=int(partes[3])
    
    rutPaciente.append(rut)
    nombrePaciente.append(nombre)
    edadPaciente.append(edad)
    sexoPaciente.append(sexo)

    linea=arch.readline().strip()
    
arch3=open("registro.txt","r")
linea3=arch3.readline().strip()
rutRegistro=[]
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
resultados=[]
while linea3 != "":
    partes=linea3.split(",")
    orden=(partes[0])
    
    if orden != "O":
        rutP=partes[0]
        mes=partes[1]
        examen=partes[2]
        result=partes[3]
        rutRegistro.append(rutP)
        resultados.append(diagnosticoExamen(result,examen,mes))
        
        

    linea3=arch3.readline().strip()

"""
for j in range(len(resultados)):
    print("Presion Arterial")
    if resultados[j][1] == "P": #primer filtro de reultado de examen para presion alteriar
        if resultados[j][2] == "Enero": #segundo filtro para meses  
            print("Enero")
            print(rutRegistro[j],resultados[j][0])
        



"""

lista  = []
rut = []
for i in range(len(resultados)):    
    if resultados[i][1] == "P" and resultados[i][2] == "Enero":
        lista.append(resultados[i])
        rut.append(rutRegistro[i])
        
        
print(lista)        
print(rut)   
print("Presion Alterial")
print("Enero")
for a in range(len(lista)):
    print(rut[a],nombrePaciente[a],lista[a][0]) 
     
        
    
    
           
