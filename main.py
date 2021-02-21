"""Codigo Principal del Juego"""

#Bibliotecas
import pygame
import math, sys, os
import numpy as np
import random
from pygame.locals import *

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 853
IMG_DIR = ""
SONIDO_DIR = ""

preg = 0
ans = 0

Abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','Ñ','O','P','Q','R','S','T','V','W','X','Y','Z']
Diccionario = ['arena.png','burro.png','camello.png','dinosaurio.png','elefante.png','foca.png','grillo.png','hipopotamo.png','iguana.png','jirafa.png','koala.png','leon.png','mariposa.png','ñoño.png',
                'oso.png','perro.png','queso.png','raton.png','salsa.png','tiburon.png','volar.png','walmart.png','xmen.png','yoyo.png','zorro.png']

#Colores
BLACK=(0,0,0)
BLUE = (102,178,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 12)
WHITE = (255,255,255)
ORANGE = (255,128,0)

#font = pygame.font.Font('agencyfb', 24)
#mensaje = fuente.render(text, 1, (255, 255, 255))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()

#tipos de letra
default_font = pygame.font.SysFont(None, 28)
marcador_font = pygame.font.SysFont(None, 40)
consolas = pygame.font.match_font('consolas')
times = pygame.font.match_font('times')
arial = pygame.font.match_font('arial')
courier = pygame.font.match_font('courier')

#validar un dato flotante
def es_flotante(variable):
	try:
		float(variable)
		return True
	except:
		return False

#creacion de botones
def dibujar_botones(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])

#Cargar Imagenes
def load_image(nombre, dir_imagen, alpha=False):
    # Encontramos la ruta completa de la imagen
    ruta = os.path.join(dir_imagen, nombre)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    # Comprobar si la imagen tiene "canal alpha" (como los png)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

#Dibujar texto
def draw_text(text, font, surface, x, y, main_color, background_color=None):
    textobj = font.render(text, True, main_color, background_color)
    textrect = textobj.get_rect()
    textrect.centerx = x
    textrect.centery = y
    surface.blit(textobj, textrect)

#texto alternativo
def muestra_texto(pantalla,fuente,texto,color, dimensiones, x, y):
    tipo_letra = pygame.font.Font(fuente,dimensiones)
    superficie = tipo_letra.render(str(texto),True, color)
    rectangulo = superficie.get_rect()
    rectangulo.center = (x, y)
    pantalla.blit(superficie,rectangulo)

#agrega sonidos
def load_sound(nombre, dir_sonido):
    ruta = os.path.join(dir_sonido, nombre)
    # Intentar cargar el sonido
    try:
        sonido = pygame.mixer.Sound(ruta)
    except (pygame.error) as message:
        print("No se pudo cargar el sonido:", ruta)
        sonido = None
    return sonido

def math():
    i = True
    operaciones = random.randrange(4)

    if operaciones == 0 :
        x = random.randint (0,100)
        y = random.randint (0,100)
        ans = x + y
        xs = str(x)
        ys = str(y)
        opc = xs+" + "+ys
    elif operaciones == 1:
        while i:
            x = random.randint (50,100)
            y = random.randint (0,50)
            ans = x - y
            if(ans<1):
                i = True
            else:
                i = False
                xs = str(x)
                ys = str(y)
                opc = xs+" - "+ys
    elif operaciones == 2:
        while i:
            x = random.randint (0,100)
            y = random.randint (0,100)
            ans = x * y
            if(ans>100):
                i = True
            else:
                i = False
                xs = str(x)
                ys = str(y)
                opc = xs+" * "+ys
    elif operaciones == 3:
        while i:
            x = random.randint (1,100)
            y = random.randint (1,100)
            ans = x / y
            if(ans<1):
                i = True
            else:
                i = False
                xs = str(x)
                ys = str(y)
                opc = xs+" / "+ys

    print(opc)
    print(ans)
    return ans, "ball.png"

def esp():
    x = random.randint (0,24)
    print(x)
    preg=Abecedario[x]
    ans=Diccionario[x]
    print(preg, ans)
    return preg,ans

#Juego en si
def start_the_game(modo):

    # cargamos los objetos
    bola = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    posbola = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    click_rect  = pygame.Rect( SCREEN_WIDTH//6, SCREEN_HEIGHT//6, SCREEN_WIDTH//6, SCREEN_HEIGHT//6 )
    puntaje = 0

    #carga componentes esteticos
    fondo = load_image("Imagenes/fondo.jpg", IMG_DIR, alpha=False)
    sonido_punto = load_sound("Sonidos/rebote.mp3", SONIDO_DIR)

    if modo == 2:
        let,img = math()
        for i in range(0,24):
            bola[i] = Pelota(sonido_punto,("Imagenes/"+"ball.png"))
    elif modo == 1:
        let,img = esp()
        for i in range(0,24):
            bola[i] = Pelota(sonido_punto,("Imagenes/"+Diccionario[i]))
    else:
        print("error")
        sys.exit(0)

    muestra_texto(screen,consolas,puntaje, RED, 40, 700, 50)

    #toda la musica de fondo
    pygame.mixer.music.load("Sonidos/musicafondo.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    sonido_fondo = pygame.mixer.Sound("Sonidos/rebote.mp3")

    #Variables
    running = True

    for i in range(0,10):
        x = bola[i].rect.centerx
        y = bola[i].rect.centery

    clock = pygame.time.Clock()
    pygame.mouse.set_visible(True)


    #bucle principal del juego
    while running:

        #calculos para el movimiento segun FPS's
        clock.tick(60)

        #obtener la pocision del mouse
        pos_mouse = pygame.mouse.get_pos()
        mov_mouse = pygame.mouse.get_rel()

        handled = False

        #actualiza las imagenes

        for i in range(0,10):
            bola[i].update()
            for j in range(0,10):
                bola[i].colision(bola[j])

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                posx = pos_mouse[0]
                posy = pos_mouse[1]
                pos = posx, posy

                print(posx, posy)

                for i in range(0,10):
                    posbola[i] = bola[i].rect.centerx,bola[i].rect.centery
                    print(posbola)
                    if click_rect.collidepoint( posbola[i] ):
                        puntaje-=-1
                        pygame.mixer.Sound.play(sonido_fondo)
                    print("Puntos: ",puntaje)

                handled = pygame.mouse.get_pressed()[0]

            #Escuchar las teclas que se precionan
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

        #Actualiza la imagen
        screen.blit(fondo, (0, 0))
        for i in range(0,10):
            screen.blit(bola[i].image, bola[i].rect)
        marcador = marcador_font.render(str(puntaje),True,ORANGE)
        screen.blit(marcador,(200,20,50,50))
        pygame.display.flip()
pass

#Declaracion de las sprite
class Pelota(pygame.sprite.Sprite):
    "La bola y su comportamiento en la pantalla"

    #inicia el sprite
    def __init__(self, sonido_punto, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(imagen, IMG_DIR, alpha=True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(SCREEN_WIDTH) / 2
        self.rect.centery = random.randrange(SCREEN_HEIGHT) / 2
        self.speed = [3, 3]
        self.rect.inflate(250,250)
        self.sonido_punto = sonido_punto
        self.hitbox = (self.rect.centerx+50, self.rect.centery+50, 0, 0)

    #actualiza el sprite
    def update(self):
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.speed[1] = -self.speed[1]
        self.rect.move_ip((self.speed[0], self.speed[1]))
        pygame.draw.rect(screen, GREEN, self.hitbox,2)

    def colision(self, objetivo):
        if self.rect.colliderect(objetivo.rect):
            self.speed[0] = -self.speed[0]

#actualiza la ventana
pygame.display.flip()

#Inicia la ventana
pygame.mixer.init()

# creamos la ventana y le indicamos un titulo:
pygame.display.set_caption("HackLearn")

def main():

    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    while True:
        title_font = pygame.font.Font('freesansbold.ttf', 65)
        big_font = pygame.font.Font(None, 36)
        draw_text('Hack-Learner', title_font, screen,
                  SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3, RED, YELLOW)
        draw_text('Usa el mouse para seleccionar la respuesta correcta', big_font, screen,
                  SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BLUE, BLACK)
        draw_text('Presiona E para jugar Español o M para jugar Matematicas',
                  default_font, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.7, BLUE, BLACK)
        draw_text('Presiona Esc para salir del juego',
                  default_font, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.4, BLUE, BLACK)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    start_the_game(1)
                elif event.key == pygame.K_m:
                    start_the_game(2)

if __name__ == "__main__":
    main()
