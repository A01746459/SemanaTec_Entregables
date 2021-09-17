import HCRfinal

import pygame

def redrawGameWindow(Dir, p1, p2):#funcion de los lados A y B de la animación
    global x, y, Side_A, Side_B #asigna variables globales a x, y, side a y b
            
    win.blit(bg,(0,0))#define posiciones iniciales
    ypos = 300#define posiciones iniciales
    for item in Side_A:#mientras el personajes se encuentre en el lado A
        win.blit(item,(5,ypos))#posicion
        ypos = ypos - 60#resta 60

    ypos = 300
    for item in Side_B:#mientras el personajes se encuentre en el lado B
        win.blit(item,(450,ypos))#posicion
        ypos = ypos - 60#se resta 60

    if p1 != 'Unknown':#mientras p1 sea diferente a desconocido
        if right:#si es derecha
            win.blit(BoatRight,(x,y))#moverá el barco a la derecha
            win.blit(farmer,(x,y-50))#mover el granjero junto con el barco
            if p2 != farmer:#si el granjero es diferente a p2
                win.blit(p2,(x+50,y-50))#p2 cambiará de posición           
        elif left:#si es izquierda
            win.blit(BoatLeft,(x,y))#moverá el barco a la izquierda
            win.blit(farmer,(x,y-50))#moverá el granjero junto con el barco
            if p2 != farmer:#si el granjero es diferente a p2
                win.blit(p2,(x+50,y-50))#p2 cambiará de posición            
    else:#de lo contrario
        win.blit(char,(x, y))
    pygame.display.update()#actualizar el display

def get_characters(d, p1, p2):#función para los personajes dentro del barco
    if p2 == 'Zorro':#si p2 es igual a zorro, el character será fox
        character = fox
    elif p2 == 'Maiz':#si p2 es igual a maiz, el character será corn
        character = corn
    elif p2 == 'Ganzo':#si p2 es igual a ganzo, el character será duck
        character = duck
    else:#de lo contrario
        character = farmer #el character será farmer lo que indicaría que va solo en el barco
    return (d, farmer, character)#regresando los que van en el barco

def Embark_characters(B, p1, p2):#funcion para la embarcación en el lado B
    if p1 in B:#mientras p1 se encuentre en B
        B.remove(p1)#se elimina p1 en B     
    if p2 in B: 
        B.remove(p2) #si el ganzo/zorro/maíz se encuentra en el barco removemos del lado B al ganzo/zorro/maíz.
 
def Disembark_characters(A, p1, p2): #Función para que un personaje se baje de un barco al otro lado del lago.
    if p1 not in A:
        A.append(p1) #si el granjero se encuentra en el barco removemos del lado B al granjero
    if p2 not in A:
        A.append(p2)
    
def HCR_animacion(P): #Función para mover lo que hay en la animación
    global x, y, left, right, vel #funciones globales que seguiremos usando, coordenadas x,y, izquierda, derecha y la velocidad en la que se mueve
    global Side_A, Side_B #funciones globales que seguiremos usando, Lado A, Lado B

    clock = pygame.time.Clock() #Creamos un reloj dentro de pygame
    run = True
    move = 0
    while run:
        clock.tick(27) #El reloj contará 27 milisegundos
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False #Cuando se presionen las teclas el juego se cerrará
        keys = pygame.key.get_pressed() #Agregamos una función para que detecte cuando se presionen teclas
        if keys[pygame.K_LEFT]: #Función cuando la tecla es la izquierda
            left = True
            right = False #Cuando la tecla izquierda sea presionada el personaje se moverá en esa diección y restringe el movimiento a la derecha
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_B, p1, p2) #Embarcamos a los personajes que elijamos del lado correspondiente
                for step in range(65): #Hacemos un rango de espacio para que se mueva nuestro personaje
                    x -= vel #Removemos la distancia de x y lo agregamos a la velocidad
                    redrawGameWindow(direction, p1, p2) #Cambiamos el tamaño de la ventana para acomodar en los personajes
                    pygame.time.delay(70) #Hacemos un retraso en el reloj para que no se desfase
                move += 3 #Agregamos 3 al valor de movimiento
                Disembark_characters(Side_A, p1, p2) #Llamamos a la función para que desenbarquen todos los personajes a la vez en el lado correspondiente

        elif keys[pygame.K_RIGHT]: #Función cuando la tecla es la derecha
            right = True
            left = False #Cuando presionas la tecla derecha, el personaje irá en esa dirección y se bloquea movimiento hacia la izquierda
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2) #Embarcamos a los personajes que elijamos del lado correspondiente
                for step in range(65): #Hacemos un rango de espacio para que se mueva nuestro personaje
                    x += vel #Removemos la distancia de x y lo agregamos a la velocidad
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3#Se le suma al valor de move un 3
                Disembark_characters(Side_B, p1, p2)#Se toma la posicion final, p1 y p2 y se usan en la funcion de desembarque
        else:#Caso ontrario
            redrawGameWindow ('Standby','Unknown', 'Unknown')#Se usa standby y dos desconocidos para ejecutar la funcion
        

    pygame.quit()#Se cierra pygame

def Busca_solucion():#Funcion para la busqueda de la solucion mas optima
    P = HCRfinal.HCR()#Se guarda la funcion del codigo de la solucion en una variable 
    while len(P) > 22:#El while nos permite no terminar el ciclo hasta optener la solucion mas optima
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()#Se usa la funcion del codigo de la solucion para reiciar el proceso
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))#Se imprimen las soluciones mas optimas
        P = HCRfinal.HCR()#La funcion del codigo de la solucion se guarda en una variable
    print (P)#Se imprime la solucion
    print (len(P))#Imprime el tamaño de la lista para saber el si el numero es optimo(En este caso se busca 21)
    print ('\n =====> Solución encontrada:')#Imprime mensaje de que la solucion fue encontrada 
    return (P)#Regresa la solucion

 
            
P = Busca_solucion()#Guardamos la funcionde buscar solucion en una variable 
print ('Aquí su animación')#Imprimimos un mensaje de inicio de la animacion

pygame.init()#Inicia los modulos importados de Pygame

win = pygame.display.set_mode((500,500))#Proporciones de la animacion
pygame.display.set_caption("How to Cross the River")#Titulo de la animacion

BoatRight   = pygame.image.load('BoteRight.png')#Usando el comando de image load obtenemos la imagen del bote a la derecha
BoatLeft    = pygame.image.load('BoteLeft.png')#Usando el comando de image load obtenemos la imagen del bote a la izquierda
bg          = pygame.image.load('seaL.png')#Usando el comando de image load obtenemos la imagen del rio
char        = pygame.image.load('BoteRight.png')#Usando el comando de image load obtenemos la imagen del bote a la derecha
fox         = pygame.image.load('fox.png')#Usando el comando de image load obtenemos la imagen del zorro
corn        = pygame.image.load('corn.png')#Usando el comando de image load obtenemos la imagen del maiz
duck        = pygame.image.load('duck.png')#Usando el comando de image load obtenemos la imagen del pato 
farmer      = pygame.image.load('farmer.png')#Usando el comando de image load obtenemos la imagen del granejero
x       = 10#Posicion inicial en x
y       = 425#Posicion inicial en y
vel     = 5#Velocidad de la animacion
left    = False#variable izquierda con booleano falso
right   = False#variable derecha con booleano falso

Side_A = [farmer, fox, duck, corn]#Posicion inicial
Side_B = []#Posicion final

HCR_animacion(P)#Funcion de la animacion llamando a varible con funcion de la solucion dentro




