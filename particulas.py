import sys
import random
import pygame
from pygame.locals import *
from colores import *

PANTALLA_ANCHO = 800
PANTALLA_ALTURA = 600
FPS = 30
LISTA_COLORES = [NAVYBLUE, ORANGE, DARKTURQUOISE, RED, GREEN, YELLOW]
CANTIDAD_PARTICULAS = 5000

pygame.init()
PANTALLA = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTURA))
pygame.display.set_caption(F'PyGame - {CANTIDAD_PARTICULAS} PARTÍCULAS')
fpsclock = pygame.time.Clock()


class Particula(pygame.sprite.Sprite):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.desciende = True
        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 0))
        pygame.draw.circle(self.image,
                            random.choice(LISTA_COLORES),
                            (3, 3), 
                            2)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centery += random.randint(0, 3) if self.desciende else random.randint(-3, 0)
        if self.rect.center[1] >= pygame.display.get_surface().get_rect().height:
            print(F'PARTÍCULA {self.nombre} ALCANZÓ EL SUELO')
            self.desciende = False 
        if self.rect.center[1] < 0:
            print(F'PARTÍCULA {self.nombre} ALCANZÓ EL TECHO')
            self.desciende = True     


particulas = pygame.sprite.Group()

for i in range(CANTIDAD_PARTICULAS):
    copo = Particula(i)
    copo.rect.center = (random.randint(0, PANTALLA_ANCHO), 0)
    particulas.add(copo)

while True:
    PANTALLA.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    particulas.update()
    particulas.draw(PANTALLA)

    if len(particulas) == 0:
        print('No hay más partículas para mostrar...')
        pygame.quit()
        sys.exit()

    pygame.display.update()
    fpsclock.tick(FPS)
