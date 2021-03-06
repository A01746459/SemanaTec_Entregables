"""
Integrantes del equipo 8:
Sebastian Burgos Alanis A01746459
Brian Axel Velarde Rodríguez A01753036
Eric Manuel Navarro Martínez A01746219
"""

"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
import turtle
from turtle import *

from freegames import vector


def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    
    up() #levantamos la pluma
    goto(start.x, start.y) #la pluma avanza a donde está el cursor
    down()#baja la pluma y empieza a pintar 
    begin_fill() #rellenar el circulo
   
    for count in range(1):
      turtle.circle(end.x - start.x)#se crea el circulo a partir de donde apunta nuestro circulo 

    end_fill()#deja de llenar y se detiene la acción
    
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()#pluma levantada
    goto(start.x, start.y)#mover la pluma a donde está nuestro cursor
    down()#bajar la pluma para comenzar a pintar
    begin_fill()#llenar la figura

    for count in range(2):
        forward(end.x - start.x)#determina la distancia de la base en el eje x
        left(90)
        forward(end.y - start.y)#determina la distancia de la altura en el eje y
        left(90)

    end_fill()
  


def triangle(start, end):
    "Draw triangle from start to end."
    up()#pluma levantada
    goto(start.x, start.y)#mover la pluma a donde está nuestro cursor
    down()#bajar la pluma para comenzar a pintar
    begin_fill()#llenar la figura

    for count in range(2): #range toma a partir de 0, por lo que pusimos 2 para que haga 0,1,2 cambios de 60 grados. 
      forward(end.x - start.x)
      right(60) #modificamos el angulo al de un triangulo equilatero. 

    end_fill()


def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    "Store value in state at key."
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y') #agregamos un color nuevo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
