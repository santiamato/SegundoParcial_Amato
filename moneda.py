import pygame

class Moneda(pygame.sprite.Sprite):
    def __init__(self,x,y, pantalla, imagen) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pantalla = pantalla
        self.imagen = imagen[0]
        self.escaler_imagen()   
        self.animacion = imagen
        self.rect = self.imagen.get_rect()        
        self.activo = True 
        self.rect.y = y
        self.rect.x = x
        self.accion = 0
    
    def escaler_imagen(self):
        self.imagen = pygame.transform.scale(self.imagen,(50,50))   
    
    def animar(self):
        largo = len(self.animacion)
        if self.accion >= largo:
            self.accion = 0
        self.imagen = self.animacion[self.accion]
        self.escaler_imagen()
        self.accion += 1

    def update(self,slave):
        if self.activo:
            self.animar()
            slave.blit(self.imagen, self.rect)