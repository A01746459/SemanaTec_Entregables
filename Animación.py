import HCRfinal

import pygame

def redrawGameWindow(Dir, p1, p2):
    global x, y, Side_A, Side_B
            
    win.blit(bg,(0,0))
    ypos = 300
    for item in Side_A:
        win.blit(item,(5,ypos))
        ypos = ypos - 60

    ypos = 300
    for item in Side_B:
        win.blit(item,(450,ypos))
        ypos = ypos - 60

    if p1 != 'Unknown':
        if right:
            win.blit(BoatRight,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))           
        elif left:
            win.blit(BoatLeft,(x,y))
            win.blit(farmer,(x,y-50))
            if p2 != farmer:
                win.blit(p2,(x+50,y-50))            
    else:
        win.blit(char,(x, y))
    pygame.display.update()

def get_characters(d, p1, p2):
    if p2 == 'Zorro':
        character = fox
    elif p2 == 'Maiz':
        character = corn
    elif p2 == 'Ganzo':
        character = duck
    else:
        character = farmer
    return (d, farmer, character)

def Embark_characters(B, p1, p2): #Función para que suban al barco los personajes
    if p1 in B:
        B.remove(p1) #si el granjero se encuentra en el barco removemos del lado B al granjero.
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
                move += 3
                Disembark_characters(Side_B, p1, p2)
        else:
            redrawGameWindow ('Standby','Unknown', 'Unknown') 
        

    pygame.quit()

def Busca_solucion():
    P = HCRfinal.HCR()
    while len(P) > 22:
    #while len(P) > 42:
        HCRfinal.reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCRfinal.HCR()
    print (P)
    print (len(P))
    print ('\n =====> Solución encontrada:')
    return (P)

 
            
P = Busca_solucion()
print ('Aquí su animación')

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("How to Cross the River")

BoatRight   = pygame.image.load('BoteRight.png')
BoatLeft    = pygame.image.load('BoteLeft.png')
bg          = pygame.image.load('seaL.png')
char        = pygame.image.load('BoteRight.png')
fox         = pygame.image.load('fox.png')
corn        = pygame.image.load('corn.png')
duck        = pygame.image.load('duck.png')
farmer      = pygame.image.load('farmer.png')
x       = 10
y       = 425
vel     = 5
left    = False
right   = False

Side_A = [farmer, fox, duck, corn]
Side_B = []

HCR_animacion(P)




