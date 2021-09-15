
import random

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']#indica que todas los miembros del juego se encuentran en el lado A inicial.
Lado_B = []#indica que el lado B "destino final" se encuentra vacio. 
Path = []#inidca que el "Path" igualmente se encuentra vacio. 

def seleccion(L):#Esta es una función para dar numero aleatorios de 0 a el tamaño de la muestra -1. 
    op = random.randint(0,len(L)-1)
    return (L[op])

def Viaje(F, D):#Esta función indica los cambios que hará cuando el granjero realice cada viaje entre la fuente y el destino. 
    p1 = seleccion(F) #El granjero es el que va a acompañar a cada miembro del juego, por lo que va a estar en constante cambio entre la fuente y el destino.
    #print ('Selección -> ', p1)
    if p1 != 'Granjero': #Si la fuente es diferente al granjero, significa que el granjero ya no se encuentra en la fuente sino en el destino. 
        F.remove(p1) #ya no está en la fuente.
        D.append(p1) #se encuentra ahora en el destino. 
    #elimina el texto.
    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1)

def valida_estado(L):
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False
    return True

def reiniciar_sistema():
    global Lado_A, Lado_B, Path
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
    Lado_B = []
    Path = []
    

def HCR():
    F = Lado_A
    D = Lado_B
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        if valida_estado (F) and valida_estado (D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:#Caso contrario
                Path.append('B->A :')#si no se cumple el if anterior se agrega de la siguiente manera
            Path.append(p1)#se agrega a la solucion personaje 1
            Path.append(p2)#se agrega a la solucion personaje 2
            
            Temp = F#Se hace un cambio de fuente destino a una variable temporal
            F = D#F es igual al destino 
            D = Temp#Destino es igual al temporal      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()#si el estado no es valido se reincia con la funcion reiniciar_sistema
            F = Lado_A#vuelve a 0
            D = Lado_B#vuelve a 0
    return (Path)


def main():#funcion principal para llama a las demas funciones
    P = HCR()#La funcion se guarda en una variable
    while len(P) > 22:#Nos permite comprobar infinitas veces hasta llegar al resultado optimo
        reiniciar_sistema()#reinicia el sistema
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))#se imprime las soluciones hasta encontrar la mas optima
        P = HCR()#La funcion se guarda en una variable
    print (P)#imprime la variable con la funcion
    print (len(P))#Imprime el tamaño de la lista para saber el si el numero es optimo(En este caso se busca 21)
            
main()#se llama a la funcion principal

  
