
import random

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
Lado_B = []
Path = []

def seleccion(L):
    op = random.randint(0,len(L)-1)
    return (L[op])

def Viaje(F, D):
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)

    F.remove('Granjero')
    D.append('Granjero')

    #print (F)
    #print (D)
    return ('Granjero',p1)

def valida_estado(L): #Creamos una función que constantemente cheque si es una solución posible.
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2:
        return False #Nos arrojará un false, debido a que si el ganzo y maíz se quedan sólos la solución es incorrecta ya que el ganzo se come el maíz.
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
        return False #Nos arrojará un false, debido a que si el ganzo y zorro se quedan sólos la solución es incorrecta ya que el zorro se come al ganzo.
    return True# Si ninguna de estas dos situaciones sucede, podemos continuar con el programa, y nos arroja un True.

def reiniciar_sistema(): #Esta función hace un reinicio para que podamos intentar otra solución.
    global Lado_A, Lado_B, Path #Llamamos a las variables de los lados y el camino.
    
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz'] #El lado A siempre que reiniciemos contiene a todos los personajes.
    Lado_B = [] #El lado B no tiene ningun personaje ya que reiniciamos.
    Path = [] #Ningun personaje se encuentra moviendose ya que reinicamos.
    

def HCR(): #La función que va a crear el camino del acertijo.
    F = Lado_A #F es el lado donde iniciamos, así que hacemos igual a lado A.
    D = Lado_B #D es el lado al que queremos cruzar , así que hacemos igual a lado B.
    while len(Lado_B) != 4: #Siempre que nuestro destino no contenga a los cuatro personajes.
        p1, p2 = Viaje(F, D)
        if valida_estado (F) and valida_estado (D):
            #Esto permite que confirmemos que es una solución, por lo que seguimos
            if F == Lado_A:
                Path.append('A->B :') #Esta funcion hace que cuando en el camino queramos viajar de A hacia B sea permitido
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)
            
            Temp = F
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    return (Path)


def main():
    P = HCR()
    while len(P) > 22:
        reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print (P)
    print (len(P))
            
main()

  
