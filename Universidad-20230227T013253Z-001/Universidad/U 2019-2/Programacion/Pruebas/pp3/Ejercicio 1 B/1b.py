# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:05:13 2020

@author: BRAYAN Alexis Maldonado Carrasco paralelo C2
"""
import numpy as np



def alerta(mensajes): #contara los mensajes de alerta
    if mensajes == "<Visibilidad>" or mensajes == "<Trafico>" or mensajes == "<Combustible>" or mensajes == "<Ráfagas>" or mensajes == "<Altitud>":
        return 1        
    else:
        return 0
        
def insert(total_aviones,diass): #esta funcion nos ira agregandp un 1(como simbolo de que se envio un mensaje); filas seran aviones y columnas seran los dias
    m_prueba = np.zeros((8,10))
    aux = aviones.index(total_aviones)
    aux2 = dias.index(diass)
    m_prueba[aux][aux2] += 1
    return m_prueba

arch = open("comunicaciones.txt","r",encoding='utf-8')
line = arch.readline().strip()
cont = 0 #contador de mensajes totales
cont_2 = 0 #contador de mensajes de alerta
matriz_madre = np.zeros((8,10))
aviones = [] #fila
dias = [20,21,22,23,24,25,26,27,28,29] #columnas
while line != "":
    partes = line.split(";")
    fecha = partes[0]
    hora = partes[1]
    avion = partes[2] #entra en insert(1)
    mensaje = partes[3]                
    partes2 = fecha.split("/")
    dia = int(partes2[0]) #¸entra en insert(2)
    mes = partes2[1]
    año = partes2[2]
    if avion not in aviones:
        aviones.append(avion)    
    result = insert(avion,dia)
    matriz_madre += result    
    cont += 1
    cont_2 += alerta(mensaje)
    line = arch.readline().strip()
print("(1) La cantidad de mensajes enviados es de ",cont)    
print("(2) El porcentaje de contenido multimedia es de ",round((cont_2/cont)*100,2),"%")
print(matriz_madre)
mayor = -1
for i in range(len(aviones)): #sumamos las filas de la matriz
    suma = 0
    for j in range(len(dias)):
        suma += matriz_madre[i][j]
        if suma > mayor:
            mayor = suma            
print("(3) La(s) persona(s) con más mensajes enviados, con  ",mayor,"es/son")    
a = matriz_madre.sum()# sumamos todos los elementos de la matriz
b = a/10 # lo dividimos en el total de dias

print("(4) El promedio diario de mensajes es ",b,"y el los dias con mas mensajes fueron")
        