# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:37:50 2020

@author: BRAYAN Alexis Maldonado Carrasco C2
"""

cont_ocio = 0
cont_lit = 0
cont_est = 0
autores = []
lista = [0,0,0,0,0,0,0,0,0,0]
arch = open("libros.txt","r",encoding = 'utf-8')
line = arch.readline().strip()
while line != "":
    partes = line.split(",")
    aux = len(partes)
    nombre_libro = partes[0]
    stock = int(partes[1])
    categoria = partes[2]    
    if aux == 4:       
        autor_1 = partes[3]
        if autor_1 not in autores:
            autores.append(autor_1)
            
    
    if aux == 5:
        autor_1 = partes[3]
        autor_2 = partes[4]
        if autor_1 not in autores:
            autores.append(autor_1)
        if autor_2 not in autores:
            autores.append(autor_2)
        
    if aux == 6:
        autor_1 = partes[3]
        autor_2 = partes[4]
        autor_3 = partes[5]
        if autor_1 not in autores:
            autores.append(autor_1)
        if autor_2 not in autores:
            autores.append(autor_2)
        if autor_3 not in autores:
            autores.append(autor_3)
        
    
    if categoria == "OCIO":
        cont_ocio += stock
    if categoria == "LITERATURA":
        cont_lit += stock
    if categoria == "ESTUDIO":
        cont_est += stock
    
    for i in range(len(partes)):
       for j in range(len(autores)):
           if partes[i] == autores[j]:
               lista[j] += 1
               
               
         
        
        

    line = arch.readline().strip()
print("LIBROS POR CATEGORIA: ")
print("-  ocio:",cont_ocio)
print("-  literatura:",cont_lit)
print("-  estudio:",cont_est)
print("CANTIDAD DE LIBROS POR AUTOR: ")
for i in autores:
    print("   -",i+":",lista[autores.index(i)])   
    
    
    
                    