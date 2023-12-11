import pygame

class Button:
    def __init__(self, imagen, pos, fuente, texto="", color_base="#d7fcd4", is_text_box=False):
        self.imagen = imagen
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.fuente = fuente
        self.color_base, self.color_texto_seleccionado = color_base, "White"
        self.texto = texto
        self.text = self.fuente.render(self.texto, True, self.color_base)
        if self.imagen is None:
            self.imagen = self.text
        self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.musica_activa = True
        self.is_text_box = is_text_box
        self.input_text = ""
    
    def text_box(self, pantalla, eventos):
        for evento in eventos:
            if self.is_text_box and evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif evento.unicode.isprintable():
                    self.input_text += evento.unicode

        pygame.draw.rect(pantalla, (255, 255, 255), (850, 150, 300, 40))
        pygame.draw.rect(pantalla, (0, 0, 0), (850, 150, 300, 40), 2)

        texto_ingresado = self.fuente.render(self.input_text, True, (0, 0, 0))
        pantalla.blit(texto_ingresado, (860, 160))

    def update(self, pantalla):
        if self.imagen is not None:
            pantalla.blit(self.imagen, self.rect)
        pantalla.blit(self.text, self.text_rect)

        if self.is_text_box:
            pygame.draw.rect(pantalla, (255, 255, 255), (850, 150, 300, 40))
            pygame.draw.rect(pantalla, (0, 0, 0), (850, 150, 300, 40), 2)
            texto_ingresado = self.fuente.render(self.input_text, True, (0, 0, 0))
            pantalla.blit(texto_ingresado, (860, 160))

    def posicion_mouse_rect(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def activar_musica(self):
        self.musica_activa = not self.musica_activa

    def cambiar_color(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.fuente.render(self.texto, True, self.color_texto_seleccionado)
        else:
            self.text = self.fuente.render(self.texto, True, self.color_base)