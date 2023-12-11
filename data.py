import pygame
from pygame.locals import *
from enemigo import Enemigo
from personaje import Personaje
from plataformas import plataforma
from corazon import Corazon
from moneda import Moneda
from configuraciones import *
#PERSONAJE
personaje_quieto = [pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\idle\player-idle-1.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\idle\player-idle-2.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\idle\player-idle-3.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\idle\player-idle-4.png")]


personaje_camina = [pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-1.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-2.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-3.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-4.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-5.png"),
                    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\run\player-run-6.png")]


personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\jump\player-jump-1.png"),
                   pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\player\jump\player-jump-2.png")]

lista_animaciones = [personaje_quieto,
                     personaje_camina,
                     personaje_salta,
                     personaje_camina_izquierda]

personaje = Personaje(PANTALLA, personaje_quieto[0], (60,90), 80, 650, 7, -15, lista_animaciones)

# PLATAFORMA   ########################################################

piso = plataforma(PANTALLA,r"recursos\small-platform.png", (WIDTH,0),0,700)



#ENEMIGOS   ##################################################

enemigo_quieto = [pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-1.png")]

enemigo_camina_izquierda = [pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-1.png"),
           pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-2.png"),
           pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-3.png"),
           pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-4.png"),
           pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-5.png"),
           pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\opossum\opossum-6.png")]

enemigo_camina_derecha = girar_imagenes(enemigo_camina_izquierda, True, False)

enemigo_movimientos = [enemigo_quieto,enemigo_camina_derecha,enemigo_camina_izquierda]


# CORAZON
cora = pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\corazon.png")
imagen_corazon = [
    cora,
    cora,
    pygame.transform.flip(cora,True,False),
    pygame.transform.flip(cora,True,False)
]


#MONEDA
imagen_moneda = [
    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\gem\gem-1.png"),
    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\gem\gem-2.png"),
    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\gem\gem-3.png"),
    pygame.image.load(r"F:\UTN\Primero-Python-Recu\segundoParcial\recursos\gem\gem-4.png")
]
#NIVEL 1
plataforma_a_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),0,260)
plataforma_b_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (500,35),900,200)
plataforma_c_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),0,500)
plataforma_d_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (500,35),1070,500)
plataforma_e_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (600,35),425,380)
plataforma_f_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (400,35),364,600)
plataforma_g_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (200,35),600,250)
plataforma_h_n1 = plataforma(PANTALLA,r"recursos\small-platform.png", (75,35),450,200)
lista_plataformas_n1 = [piso, plataforma_a_n1,plataforma_b_n1,plataforma_c_n1,plataforma_d_n1,plataforma_e_n1,plataforma_f_n1,plataforma_g_n1,plataforma_h_n1]

enemigo1_n1 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),900,355,enemigo_movimientos,990,430)
enemigo2_n1 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),700,575,enemigo_movimientos,720,380)
lista_enemigos_n1 = [enemigo1_n1,enemigo2_n1]

corazon = Corazon(1100,150,PANTALLA,imagen_corazon)
corazones_n1 = [corazon]

moneda = Corazon(460,150,PANTALLA,imagen_moneda)
monedas_n1 = [moneda]

#NIVEL 2
plataforma_a_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (50,35),700,280)
plataforma_b_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (500,35),900,200)
plataforma_c_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),0,500)
plataforma_d_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),1600,500)
plataforma_e_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (600,35),425,380)
plataforma_f_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (1150,35),364,600)
plataforma_g_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),1240,380)
plataforma_h_n2 = plataforma(PANTALLA,r"recursos\small-platform.png", (75,35),1450,130)
lista_plataformas_n2 = [piso, plataforma_a_n2,plataforma_b_n2,plataforma_c_n2,plataforma_d_n2,plataforma_e_n2,plataforma_f_n2,plataforma_g_n2,plataforma_h_n2]

enemigo1_n2 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),900,355,enemigo_movimientos,990,430)
enemigo2_n2 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),700,575,enemigo_movimientos,1200,380)
enemigo3_n2 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),900,175,enemigo_movimientos,1300,1000)
enemigo4_n2 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),1240,355,enemigo_movimientos,1500,1250)
lista_enemigos_n2 = [enemigo1_n2,enemigo2_n2, enemigo3_n2, enemigo4_n2]

corazon = Corazon(1100,270,PANTALLA,imagen_corazon)
corazones_n2 = [corazon]

moneda = Corazon(1460,70,PANTALLA,imagen_moneda)
monedas_n2 = [moneda]

#NIVEL 3
plataforma_b_n3 = plataforma(PANTALLA,r"recursos\small-platform.png", (500,35),900,260)
plataforma_c_n3 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),1000,500)
plataforma_e_n3 = plataforma(PANTALLA,r"recursos\small-platform.png", (600,35),425,380)
plataforma_f_n3 = plataforma(PANTALLA,r"recursos\small-platform.png", (700,35),364,600)
plataforma_g_n3 = plataforma(PANTALLA,r"recursos\small-platform.png", (300,35),1240,380)
lista_plataformas_n3 = [piso,plataforma_b_n3,plataforma_c_n3,plataforma_e_n3,plataforma_f_n3,plataforma_g_n3]

enemigo1_n3 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),900,355,enemigo_movimientos,990,520)
enemigo2_n3 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),500,575,enemigo_movimientos,1000,350)
enemigo3_n3 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),900,235,enemigo_movimientos,1300,1000)
enemigo4_n3 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),1240,355,enemigo_movimientos,1500,1250)
enemigo5_n3 = Enemigo(PANTALLA, enemigo_quieto[0],(60,90),1000,475,enemigo_movimientos,1220,1050)
lista_enemigos_n3 = [enemigo1_n3,enemigo2_n3, enemigo3_n3, enemigo4_n3, enemigo5_n3]

corazon = Corazon(450,320,PANTALLA,imagen_corazon)
corazones_n3 = [corazon]

moneda = Corazon(1120,190,PANTALLA,imagen_moneda)
monedas_n3 = [moneda]