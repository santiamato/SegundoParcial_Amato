import pygame, sys, time
from configuraciones import *
from pygame.locals import *
from modo import *
from enemigo import Enemigo
from personaje import Personaje
from plataformas import plataforma
from corazon import Corazon
from moneda import Moneda
from boton import Button
import json
from data import *

pygame.init()
#FUENTE
fuente = pygame.font.SysFont("Arco Font",70)
cronometro = 0
tiempo = fuente.render(f"00:0{cronometro}", True, "White")
#FONDO
fondo = pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\fondo.png").convert()
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)
# ICONO  ###############################################################3
icono = pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-1.png")
pygame.display.set_icon(icono)
pygame.display.set_caption("Juego Raton")

cronometro_1 = time.time()
#MUSICA
pygame.mixer.music.load("recursos\musica.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
def nivel(tiempo_transcurrido):
        RELOJ.tick(FPS)

        lista_eventos = pygame.event.get()
        for evento in lista_eventos:
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            personaje.mover_derecha()
            personaje.saltar()
        elif (keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]) and (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            personaje.mover_izquierda()
            personaje.saltar()
        elif keys[pygame.K_UP] or keys[pygame.K_w]  or keys[pygame.K_SPACE]:
            personaje.saltar()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            personaje.mover_derecha()
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            personaje.mover_izquierda()
        else:
            personaje.quieto()
        if keys[pygame.K_p]:
            ahora = pygame.time.get_ticks()
            if ahora - personaje.ultimo_disparo > personaje.retrazo_disparo:
                personaje.disparar(PANTALLA)
                personaje.ultimo_disparo = ahora

        
        tiempo = fuente.render(f"00:{int(60-tiempo_transcurrido)}", True, "Black")

        PANTALLA.blit(fondo, (0,0))
        
        score = fuente.render(f"Score:{personaje.puntuacion}", True, "Black")
        PANTALLA.blit(tiempo, (500,20))
        PANTALLA.blit(score, (912,20))
        personaje.mostrar_vidas(PANTALLA)
        
        
    
def nivel_1(tiempo_transcurrido):
        nivel(tiempo_transcurrido)
        flag = True
        for platform in lista_plataformas_n1:
                platform.update(PANTALLA)
            
        for enemigo in lista_enemigos_n1:
            enemigo.update(PANTALLA)
            personaje.collision(enemigo, corazones_n1, monedas_n1)
            if enemigo.esta_vivo:
                flag = False
        personaje.update(PANTALLA,lista_plataformas_n1,enemigo, corazones_n1)

        for x in corazones_n1:
            x.update(PANTALLA)

        for x in monedas_n1:
            x.update(PANTALLA)
            if x.activo:
                flag = False
        
        if flag:
            return 1
        
def nivel_2(tiempo_transcurrido):
        nivel(tiempo_transcurrido)
        flag = True
        for platform in lista_plataformas_n2:
                platform.update(PANTALLA)
            
        for enemigo in lista_enemigos_n2:
            enemigo.update(PANTALLA)
            personaje.collision(enemigo, corazones_n2, monedas_n2)
            if enemigo.esta_vivo:
                flag = False
        personaje.update(PANTALLA,lista_plataformas_n2,enemigo, corazones_n2)

        for x in corazones_n2:
            x.update(PANTALLA)

        for x in monedas_n2:
            x.update(PANTALLA)
            if x.activo:
                flag = False
        
        if flag:
            return 2


def nivel_3(tiempo_transcurrido):
        nivel(tiempo_transcurrido)
        flag = True
        for platform in lista_plataformas_n3:
                platform.update(PANTALLA)
            
        for enemigo in lista_enemigos_n3:
            enemigo.update(PANTALLA)
            personaje.collision(enemigo, corazones_n3, monedas_n3)
            if enemigo.esta_vivo:
                flag = False
        personaje.update(PANTALLA,lista_plataformas_n3,enemigo, corazones_n3)

        for x in corazones_n3:
            x.update(PANTALLA)

        for x in monedas_n3:
            x.update(PANTALLA)
            if x.activo:
                flag = False
        
        if flag:
            return 3
        
def cargar_ranking(ranking_nivel):
    try:
        with open("ranking_nivel_%s" % str(ranking_nivel), 'r') as f:
            datos = json.load(f)
        return sorted(datos, key=lambda x: x['puntuacion'], reverse=True)[:5]
    except FileNotFoundError:
        return []
    
def mostrar_ranking(ranking):
    # Encabezado de la tabla
    encabezado = fuente.render("TOP 5", True, "Black")
    PANTALLA.blit(encabezado, (800, 200))

    # Mostrar filas del ranking
    y = 250
    for i, usuario in enumerate(ranking, start=1):
        nombre = fuente.render(usuario['nombre'], True, "Black")
        puntuacion = fuente.render(str(usuario['puntuacion']), True, "Black")

        PANTALLA.blit(nombre, (TAMAÑO_PANTALLA[0] // 3, y))
        PANTALLA.blit(puntuacion, (1.5 * TAMAÑO_PANTALLA[0]// 3, y))
            
        y += 40


def agregar_elemento_a_json(nombre, puntuacion, ranking_nivel):
    try:
        with open("ranking_nivel_%s" % str(ranking_nivel), 'r') as f:
            datos = json.load(f)
    except FileNotFoundError:
        datos = []

    usuario_existente = None
    for usuario in datos:
        if usuario['nombre'] == nombre:
            usuario_existente = usuario
            break

    if usuario_existente:
        if puntuacion > usuario_existente['puntuacion']:
            usuario_existente['puntuacion'] = puntuacion
    else:
        nuevo_id = len(datos) + 1
        nuevo_usuario = {'id': nuevo_id, 'nombre': nombre, 'puntuacion': puntuacion}
        datos.append(nuevo_usuario)

    with open("ranking_nivel_%s" % str(ranking_nivel), 'w') as i:
        json.dump(datos, i, indent=2)

def gano(tiempo_transcurrido, nombre, ranking_nivel):
    pygame.event.clear()
    PANTALLA.blit(fondo, (0, 0))
    ranking = cargar_ranking(ranking_nivel)
    mostrar_ranking(ranking)

    tiempo_restante = max(0, 60 - int(tiempo_transcurrido))
    puntos_obtenidos_tiempo = tiempo_restante * 100

    info_rect = pygame.Rect(0, 0, 350, 75)
    pygame.draw.rect(PANTALLA, "black", info_rect)

    puntos_texto = fuente.render(f"+{puntos_obtenidos_tiempo} score", True, "White")
    PANTALLA.blit(puntos_texto, (50, 20))

    agregar_elemento_a_json(nombre, puntos_obtenidos_tiempo, ranking_nivel)

def reiniciar_variables():
    global cronometro_1
    cronometro_1 = time.time()
    personaje.vidas = 3
    personaje.esta_vivo = True
    personaje.puntuacion = 0
    
def juego():
    musica_activa = True
    menu1 = "MENU"

    input_rect = pygame.Rect(900,100,300,50)
    nombre_usuario = ""
    text_activo = False
    
    while True:
        PANTALLA.fill((0, 0, 0))
        PANTALLA.blit(fondo, (0, 0))
        
        posicion_mouse = pygame.mouse.get_pos()
        
        fuente_texto = fuente.render("NOMBRE:", True, "#CD5C5C")
        menu = fuente_texto.get_rect(center=(780, 130))

        button_nivel_1 = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\fondo_button.png"), (900, 250), 
                            fuente, "NIVEL 1")
        button_nivel_2 = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\fondo_button.png"), (900, 400), 
                            fuente, "NIVEL 2")
        button_nivel_3 = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\fondo_button.png"), (900, 550), 
                            fuente,"NIVEL 3")
        button_salir = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\fondo_button.png"), (900, 700), 
                            fuente, "SALIR")
        button_musica = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\boton_musica.png"), (1750, 100), fuente)
        
        button_volver = Button(pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\button_volver.png"), (1750, 800), fuente)

        PANTALLA.blit(fuente_texto, menu)

        for button in [button_nivel_1, button_nivel_2, button_nivel_3, button_salir, button_musica]:
            button.changeColor(posicion_mouse)
            button.update(PANTALLA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if button_nivel_1.posicion_mouse_rect(posicion_mouse):
                    menu1 = "NIVEL_1"  
                elif button_nivel_2.posicion_mouse_rect(posicion_mouse):
                    menu1 = "NIVEL_2"
                elif button_nivel_3.posicion_mouse_rect(posicion_mouse):
                    menu1 = "NIVEL_3"
                elif button_salir.posicion_mouse_rect(posicion_mouse):
                    pygame.quit()
                    sys.exit()
                elif button_musica.posicion_mouse_rect(posicion_mouse):
                    print(musica_activa)
                    if musica_activa:
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                    musica_activa = not musica_activa
                elif button_volver.posicion_mouse_rect(posicion_mouse):
                    reiniciar_variables()
                    menu1 = "MENU"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                 if input_rect.collidepoint(evento.pos):
                      text_activo = True
            if evento.type == pygame.KEYDOWN:
                if text_activo == True:
                    if evento.key == pygame.K_BACKSPACE:
                        nombre_usuario = nombre_usuario[:-1]
                    elif evento.unicode.isprintable():
                        nombre_usuario += evento.unicode

        
        pygame.draw.rect(PANTALLA, "WHITE", input_rect,2)
        text_surface = fuente.render(nombre_usuario,True,(0,0,0))
        PANTALLA.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(250,text_surface.get_width() + 10)
       
        estado = None
        if menu1 == "NIVEL_1":
            estado = nivel_1(tiempo_transcurrido)
        if menu1 == "NIVEL_2" :
            estado = nivel_2(tiempo_transcurrido)
        if menu1 == "NIVEL_3":
            estado = nivel_3(tiempo_transcurrido)
        if estado == "MENU":
                continue
            

        if not estado:
            tiempo_transcurrido = time.time() - cronometro_1 
        if int(60-tiempo_transcurrido) == 0 or personaje.vidas == 0:
                reiniciar_variables()
                menu1 = "MENU"

        if estado:
            button_volver.changeColor(posicion_mouse)
            gano(tiempo_transcurrido, nombre_usuario, estado)
            button_volver.update(PANTALLA)
            
        
        
        
        
        
        
        pygame.display.update()
        

juego()