from email.mime import image
from textwrap import fill
import pygame, random, sys 
from pygame.locals import *

ANCHOVENTANA = 600
ALTOVENTANA = 600
COLORVENTANA = (255, 255, 255)
COLORFONDO = (0, 0, 0)
FPS = 40
TAMAÑOMINVILLANO = 10 
TAMAÑOMAXVILLANO = 40
VELOCIDADMINVILLANO = 1
VELOCIDADMAXVILLANO = 8
TASANUEVOVILLANO = 6
TASAMOVIMIENTOJUGADOR = 5

def terminar():
    pygame.quit()
    sys.exit()

def esperarTeclaJugador():
    while True:
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                terminar()
            if evento.key == K_ESCAPE:
                terminar()
            return


def jugadorGopeaVillano(rectanguloJugador, villanos):
    for v in villanos:
        if rectanguloJugador.colliderect(v["rect"]):
            return True
    return False

def dibujarTexto(texto, fuente, superficie, x, y):
    objetotexto = fuente.render(texto, 1, COLORVENTANA)
    rectangulotexto = objetotexto .get_rect()
    rectangulotexto.topleft = (x, y)
    superficie.blit(objetotexto, rectangulotexto)


pygame.init()
relojPrincipal = pygame.time.Clock()
superficieVentana = pygame.display.set_mode ((ANCHOVENTANA, ALTOVENTANA))
pygame.display.set_caption("Evasor")
pygame.mouse.set_visible


fuente = pygame.font.SysFont(None, 48)


sonidoJuegoTerminado = pygame.mixer.Sound("")
pygame.mixer.music.load("")

imagenJugador = pygame.image.load("prueba.png")
rectanguloJugador = imagenJugador.get_rect()
imagenVillano = pygame.image.load("prueba.png")


dibujarTexto("Evasor", fuente,superficieVentana,(ANCHOVENTANA / 9)+40,(ALTOVENTANA / 3))


pygame.display.update()
esperarTeclaJugador()


puntajeMax = 0
while True:

    villanos = []
    puntaje = 0
    rectanguloJugador.topleft = (ANCHOVENTANA / 2, ALTOVENTANA - 50)
    moverIzquierda = moverDerecha = moverArriba = moverAbajo = False
    trucoReversa = trucoLento = False
    contadorAgregarVillano = 0
    pygame.mixer.music.play(-1, 0.0)

    while True:
        puntaje += 1

        for evento in pygame.event.get():
            if evento.type == QUIT:
                terminar()

            if evento.type == KEYDOWN:
                if evento.key == ord("z"):
                    trucoReversa = True
                if evento.key == ord("x"):
                    trucoLento = True
                if evento.key == K_LEFT or evento.key == ord("a"):
                    moverDerecha = False
                    moverIzquierda = True
                if evento.key == K_RIGHT or evento.key == ord("d"):
                    moverIzquierda = False
                    moverDerecha = True
                if evento.key == K_UP or evento.ke == ord("w"):
                    moverArriba = False
                    moverAbajo = True
                
            if evento.type == KEYUP:
                if evento.key == ord("z"):
                    trucoReversa = 0
                    puntaje = 0
                if evento.key == ord("X"):
                    trucoLento = False
                    puntaje = 0
                if evento.key == K_ESCAPE:
                    terminar()

                if evento.key == K_LEFT or evento.key == ord("a"):
                    moverIzquierda = False
                if evento.key == K_RIGHT or evento.key == ord("d"):
                    moverDerecha = False
                if evento.key == K_UP or evento.key == ord("w"):
                    moverArriba = False
                if evento.key == K_DOWN or evento.key == ord("s"):
                    moverAbajo = False
            
            if evento.type == MOUSEMOTION:



                rectanguloJugador.move_ip(evento.pos[0] - rectanguloJugador.centerx, evento[1] - rectanguloJugador.centery)

                if not trucoReversa and not trucoLento:
                    contadorAgregarVillano += 1
                if contadorAgregarVillano == TASANUEVOVILLANO:
                    contadorAgregarVillano = 0
                    tamañoVillano = random.randint(TAMAÑOMINVILLANO, TAMAÑOMAXVILLANO)


                    nuevoVillano = {"rect": pygame.Rect(random.randint(0, ANCHOVENTANA-tamañoVillano), 0 - tamañoVillano, tamañoVillano, tamañoVillano),
                    
                    "velocidad":random.randint(VELOCIDADMINVILLANO, VELOCIDADMAXVILLANO),
                    "superficie":pygame.transform.scale(imagenVillano, (tamañoVillano, tamañoVillano)),
                    }
            villanos.append(nuevoVillano)

        if moverIzquierda and rectanguloJugador.left > 0:
            rectanguloJugador.move_ip(-1 * TASAMOVIMIENTOJUGADOR, 0)
        if moverDerecha and rectanguloJugador.top > 0:
            rectanguloJugador.move_ip(0, -1 * TASAMOVIMIENTOJUGADOR)
        

        pygame.mouse.set_pos(rectanguloJugador.centerx, rectanguloJugador.centery)



        for v in villanos:
            if not trucoReversa and not trucoLento:
                v["rect"].move.ip(0, v["velocidad"])
            elif trucoReversa:
                v["rect"].move_ip(0, -5)
            elif trucoLento:
                v["rect"].move_ip(0, 1)


        for v in villanos[:]:
            if v["rect"].top > ALTOVENTANA:
                villanos.remove(v)

        
        superficieVentana.fill(COLORFONDO)


        dibujarTexto("puntaje: %s" % (puntaje), fuente, superficieVentana, 10, 0)

        dibujarTexto("puntaje maximo: %s" % (puntajeMax), fuente, superficieVentana, 10, 40)


        superficieVentana.blit(imagenJugador, rectanguloJugador)


        for v in villanos:
            superficieVentana.blit(v["superficie"], v["rect"])
        

        pygame.display.update()

        if jugadorGopeaVillano(rectanguloJugador, villanos):
            if puntaje > puntajeMax:
                puntajeMax = puntaje
            break


        relojPrincipal.tick(FPS)

    pygame.mixer.music.stop()
    sonidoJuegoTerminado.play()

    dibujarTexto("juego terminado", fuente, superficieVentana, (ANCHOVENTANA / 3))
    dibujarTexto("presione una tecla para jugar de nuevo.", fuente,
    superficieVentana, (ANCHOVENTANA / 3) - 80, (ALTOVENTANA / 3) + 50)
    pygame.display.update()
    esperarTeclaJugador()

    sonidoJuegoTerminado.stop()





                       