from collections import Counter
#import numpy as np
import matplotlib.pyplot as plt

def word_count(fname): #Creamos una función la cual contará las palabras que se repitan
  with open(fname) as f:
    return Counter(f.read().split()) #Nos regresa las palabras que se repiten y la cantidad
    
L = word_count("GEH.txt") #Creamos una variable para que podamos usarla más fácil después

#print("Number of words in the file :", L)  

#print (L)
#print(type(L))
LD = dict(L)#convertimos el counter a diccionario
palabras = list(LD.keys())#Agregamos las palabras a una lista
frecuencia = list(LD.values())#Agregamos las cantidades a una lista

#print (palabras)
#print(frecuencia)

x = palabras #En el gráfico "x" serán todas las palabras
y = frecuencia #En el gráfico "y" será cuantas veces se repite

plt.bar(x,y,align='center') #Para que se encuentre centrado el histograma
plt.xlabel('Palabras') #El titulo del eje x
plt.ylabel('Frecuencia') #El titulo del eje y
for i in range(len(y)):
    plt.hlines(y[i],0,x[i]) # Dibujamos la linea horizontal
plt.show() #Mostramos el gráfico