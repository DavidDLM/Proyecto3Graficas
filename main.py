# main
# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

import pygame
import sys
import numpy as np
# IMPORTAR LAS CLASES
from variables import *
from map import *
from player import *
from raycasting import *
from renderer import *
from sprites import *
from mapObjects import *
from music import *
from gun import *


class raycastingGame:
    def __init__(this):
        
        ###########################
        pygame.init()
        pygame.mouse.set_visible(False)
        ###########################
        
        this.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # Inicia la surface
        # pygame.display.set_caption("Raycasting")
        # timer
        this.TIMER = pygame.time.Clock() # Para los FPS
        this.delta = 1
        this.newGame()
       
    # Inicializa las funciones de las clases
    def newGame(this): 
        this.MAP = Map(this)
        this.player = Player(this)
        this.renderer = Renderer(this)
        this.raycasting = Raycasting(this)
        # this.sprite = Sprite(this)
        # this.animSprite = AnimatedSprite(this)
        this.objmap = mapObjects(this)
        this.gun = Gun(this)
        this.music = Music(this)
        pygame.mixer.music.play(-1) # Tocar musica de fondo siempre

    def update(this): # Actualiza
        # Actualiza con las funciones update de las clases
        this.player.update()
        this.raycasting.update()
        this.objmap.update()
        this.gun.update()
        # this.sprite.update()
        # this.animSprite.update()
        pygame.display.flip()
        # Set FPS
        this.delta = this.TIMER.tick(45)
        pygame.display.set_caption(f'{this.TIMER.get_fps() :.1f}') # Imprime contador de FPS en el borde superior

    def drawScreen(this): # Crea la escena
        this.renderer.draw() 
        this.gun.drawGun() # Dibuja arma al centro de pantalla

    def checkE(this):
        # Quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            this.player.gunFire(event) # Click izquierdo dispara

    def run(this): # Corre la funcion update principal, que contiene las demas
        while True:
            this.checkE() # Check evento
            this.update()
            this.drawScreen()


if __name__ == '__main__':
    game = raycastingGame()
    game.run()
