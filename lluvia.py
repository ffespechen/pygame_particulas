# Imagen de fondo https://www.freepik.com/free-photo/lone-tree_17247798.htm#query=beautiful%20landscape&position=2&from_view=keyword&track=ais&uuid=43ce949a-804c-45cd-a5a3-0d698103d328 Image by wirestock
import sys
import random
import pygame
from pygame.locals import *
from colores import *

PANTALLA_ANCHO = 1000
PANTALLA_ALTURA = 667
FPS = 30
CANTIDAD_PARTICULAS = 500

pygame.init()
PANTALLA = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTURA))
pygame.display.set_caption(F'PyGame - {CANTIDAD_PARTICULAS} GOTAS')
fpsclock = pygame.time.Clock()

fondo = pygame.image.load('lone-tree.jpg')


class Gota(pygame.sprite.Sprite):

    def __init__(self, velx, vely):
        super().__init__()
        self.velx = velx
        self.vely = vely
        self.image = pygame.Surface((2, 5))
        # self.image.fill((0, 0, 0))
        pygame.draw.line(self.image,
                            WHITE,
                            (0, 0),
                            (2, 5), 
                            2)
        self.rect = self.image.get_rect()
        self.__posicion_inicial()

    def update(self):
        self.rect.centerx += self.velx
        self.rect.centery += self.vely
        if (self.rect.center[1] >= pygame.display.get_surface().get_rect().height) or (self.rect.center[0] >= pygame.display.get_surface().get_rect().width):
            self.__posicion_inicial()
   
    def __posicion_inicial(self):
        self.rect.centerx = random.uniform(0, pygame.display.get_surface().get_rect().width)
        self.rect.centery = random.uniform(0, pygame.display.get_surface().get_rect().height)


particulas = pygame.sprite.Group()

for i in range(CANTIDAD_PARTICULAS):
    gota = Gota(1, 2)
    particulas.add(gota)

while True:
    PANTALLA.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    PANTALLA.blit(fondo, (0, 0))
    particulas.update()
    particulas.draw(PANTALLA)

    pygame.display.update()
    fpsclock.tick(FPS)
