from email.mime import image
from json import load
from pickle import TRUE
import jupyter_client
import pygame, sys, time,random
from pygame.locals import *


pygame.init()
relojPrincipal = pygame.time.Clock()


ANCHOVENTANA = 1200
ALTOVENTANA = 1200
superficieVentana = pygame.display.set_mode((ANCHOVENTANA, ALTOVENTANA), 0, 32)
pygame.display.set_caption("sprites y sonido")


NEGRO = (0, 0, 0)


jugador = pygame.Rect(300, 100, 40, 40)
imagenJugador = pygame.image.load("prueba.png")
imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (40,40))
imagenComida = pygame.image.load("prueba.png")
comidas = []
for i in range(20):
    comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

contadorComida = 0
NUEVACOMIDA = 40

moverseIzquierda = False
moverseDerecha = False
moverseArriba = False 
moverseAbajo = False

VELOCIDADMOVIMIENTO = 6

#sonidoRecoleccion = pygame.mixer.Sound("")
#pygame.mixer.music.load("")
#pygame.mixer.music.play(-1, 0.0)
#musicaSonando = True

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == KEYDOWN:

            if evento.key == K_LEFT or evento.key == ord("a"):
                moverseDerecha = False
                moverseIzquierda = True
            if evento.key == K_RIGHT or evento.key == ord("d"):
                moverseIzquierda = False
                moverseDerecha = True
            if evento.key == K_UP or evento.key == ord("w"):
                moverseAbajo = False
                moverseArriba = False
            if evento.key == K_DOWN or evento.key == ord("s"):
                moverseArriba = False
                moverseAbajo = TRUE
            
            if evento.type == KEYUP:
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key == K_LEFT or evento.key == ord("a"):
                    moverseIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord("d"):
                    moverseDerecha = False
                if evento.key == K_UP or evento.key == ord("w"):
                    moverseArriba = False
                if evento.key == K_DOWN or evento.key == ord("s"):
                    moverseAbajo = False
                if evento.key == ord("x"):
                    jugador.top = random.randint(0, ALTOVENTANA - jugador.height)
                    jugador.left = random.randint(0, ANCHOVENTANA - jugador.width)
                if evento.key == ord("m"):
                    if musicaSonando:
                        pygame.mixer.music.play(-1, 0.0)
                    musicaSonando = not musicaSonando

            if evento.type == MOUSEBUTTONUP:
                comidas.append(pygame.Rect(evento.pos[0] - 10, evento.pos[1] - 10, 20, 20))
        contadorComida += 1
        if contadorComida >= NUEVACOMIDA:

            contadorComida = 0
            comidas.append(pygame.Rect(random.randint(0, ANCHOVENTANA - 20), random.randint(0, ALTOVENTANA - 20), 20, 20))

        superficieVentana.fill(NEGRO)

        if moverseAbajo and jugador.bottom < ALTOVENTANA:
            jugador.top += VELOCIDADMOVIMIENTO
        if moverseArriba and jugador.top > 0:
            jugador.left -= VELOCIDADMOVIMIENTO
        if moverseIzquierda and jugador.right < ANCHOVENTANA:
            jugador.right += VELOCIDADMOVIMIENTO

        
    superficieVentana.blit(imagenEstiradaJugador, jugador)

    for comida in comidas[:]:
        if jugador.colliderect(comida):
            comidas.remove(comida)
            jugador = pygame.Rect(jugador.left, jugador.left, jugador.top, jugador.width + 2, jugador.height + 2)

            imagenEstiradaJugador = pygame.transform.scale(imagenJugador, (jugador.width, jugador.height))
            #if musicaSonando:
             #   sonidoRecoleccion.play()
        
    for comida in comidas:
        superficieVentana.blit(imagenComida, comida)

        pygame.display.update()
        relojPrincipal.tick(40)
