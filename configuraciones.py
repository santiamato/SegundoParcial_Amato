import pygame
WIDTH,HEIGHT = 1900, 900
TAMAÑO_PANTALLA = (WIDTH, HEIGHT)      
ORIGEN = (0, 0)


RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
FPS = 18


def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))

    return lista_girada
