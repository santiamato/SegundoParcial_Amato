import pygame,random
from personaje import Personaje
from configuraciones import *

class Enemigo(Personaje):
    def __init__(self, pantalla, imagen, size: tuple, x, y,acciones,limite_mayor, limite_menor, vidas=1) -> None:
        super().__init__(pantalla, imagen, size, x, y, 10, 0, acciones)
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor
        self.retrazo = 5500
        self.ultima_direccion = pygame.time.get_ticks()
        self.esta_vivo = True
        self.vidas = vidas
        self.velocidad = 5
        self.muerte_1 = False

    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
        else:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultima_direccion > self.retrazo:
                self.ultima_direccion = ahora
                random_number = random.randint(0, 1)
                if random_number == 0:
                    self.posicion = "izquierda"
                else:
                    self.posicion = "derecha"

    def mover(self):
        if self.esta_vivo:
            self.direccion()
            if self.posicion == "derecha":
                self.mover_derecha()
            elif self.posicion == "izquierda":
                self.mover_izquierda()

    def reset(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.vidas = 1
        self.esta_vivo = True
        self.muerte_1 = False
        self.ultima_direccion = pygame.time.get_ticks()
        
    def reescalar_imagenes(lista_imagenes, W, H):
        for lista in lista_imagenes:
            for i in range(len(lista)):
                lista[i] = pygame.transform.scale(lista[i], (W,H))
    
    def collision(self,personaje):
        for x in personaje.lista_proyectiles:
            if x.disparo_rect.colliderect(self.rect):
                self.vidas -= 1
                personaje.lista_proyectiles.remove(x)

    def muerte(self):
        if self.vidas <= 0:
            self.esta_vivo = False

    def update(self,slave):
        self.muerte()
        if self.esta_vivo == True:
            self.mover()
            slave.blit(self.imagen, self.rect)
        else:
            if self.muerte_1:
                self.rect = None
            else:
                self.rect = None
                self.muerte_1 = True
          