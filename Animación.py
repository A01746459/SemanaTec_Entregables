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

def Embark_characters(B, p1, p2):
    if p1 in B:
        B.remove(p1)     
    if p2 in B:
        B.remove(p2)
 
def Disembark_characters(A, p1, p2):
    if p1 not in A:
        A.append(p1)
    if p2 not in A:
        A.append(p2)
    
def HCR_animacion(P):
    global x, y, left, right, vel
    global Side_A, Side_B

    clock = pygame.time.Clock()
    run = True
    move = 0
    while run:
        clock.tick(27)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            left = True
            right = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_B, p1, p2)
                for step in range(65):
                    x -= vel
                    redrawGameWindow(direction, p1, p2)
                    pygame.time.delay(70)
                move += 3
                Disembark_characters(Side_A, p1, p2)

        elif keys[pygame.K_RIGHT]:
            right = True
            left = False
            if move < len(P):
                direction, p1, p2 = get_characters(P[move], P[move + 1], P[move + 2])
                Embark_characters(Side_A, p1, p2)
                for step in range(65):
                    x += vel
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




