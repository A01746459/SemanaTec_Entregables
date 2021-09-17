# SemanaTec_Entregables
Equipo #8 primer entrega. 

Miembros:
Sebastián Burgos Alanís A01746459
Eric Manuel Navarro Martínez A01746219
Brian Axel Velarde Rodriguez A01753036

Situacion a resolver:
How to Cross the River.
Un pequeño puzzle que nos pone en las botas de un granjero que quiere cruzar un pato, un zorro y un maiz al lado de un rio,
pero tenemos ciertas reglas que debemos de seguir:

1-Solo podemos trasladar una cosa a la vez.
2-El zorro no se puede quedar solo con el pato o este se lo comera.
3-el pato no se puede quedar solo con el maiz o este se lo comera.

objetivo:
Resolver el acertijo con todas las condiciones anteriores de la manera mas optima y en el menor numero de pasos posibles y generar
una pequeña animacion con el resultado obtenido.

Lenguaje implementado:
-Python 3.8.2

Librerias utilizadas:
-Pygame 2.0.1
-random
-matplotlib
-pyplot

Implementacion:
Para la creacion de la animacion era necesario primero resolver el problema, teniendo esto en mente el proyecto se dividio en 2 partes:
-Parte logica
-Parte animada
En la parte logica se hace uso de la libreria random, funciones, listas, ciclos etc.
se crean 3 listas que contiene a los personajes y sus posibles posiciones, y con las funciones 
los personajes van saltando de lista en lista hasta que llegan todos al destino.
Haciendo uso de while podemos obtener muchos resultados pero solo mostrar el que se busca, en este caso es el que tiene menos turnos usados
En la parte animada hacemos uso de la libreria Pygame en su version 2.0.1 ademas se importa el codigo anterio para poder hacer uso de sus funciones,
haciendo uso de la libreria de pygame se pudo agregar imagenes de los personajes del acertijo, se crean funciones para las posiciones de los personajes,
para cuando los personajes se montan en el barco, para cuando desembarcan, para mover la animacion y funciones para poder controlar la animacion con
las teclas derecha e izquierda.

Experiencia trabajando en Github:
El uso de Github en nuestro caso, es para poder agregar nuestras partes y unirlas, tratamos de usar todas las funciones de la mejor manera posible
hubo ocasiones en las cuales se tuvo algunos problemas pero en general siempre se trato de hacer uso de todas las herramientas posibles.
Debido al corto tamaño o complejidad de cada programa, github no fue muy util, replit puede ser una herramienta un poco más agil y eficaz, ya que los integrantes podemos trabajar y editar los archivos al mismo tiempo. Sin emabrgo, github fue de suma utilidad a la hora de subir al repositorio más de un archivo. 
