# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

import pygame
import numpy as np
from variables import *


class Renderer:
    def __init__(this, game):
        this.game = game
        this.SCREEN = game.SCREEN
        this.wallTXT = this.loadWallTXT()
        this.sky = this.getTXT('models/background2.png', (WIDTH, HEIGH_HF))
        this.skyOffset = 0

    def draw(this):
        this.drawBckg()
        this.renderObj()

    def drawBckg(this):
        this.skyOffset = (this.skyOffset + 4.5 * this.game.player.rel) % WIDTH
        this.SCREEN.blit(this.sky, (-this.skyOffset, 0))
        this.SCREEN.blit(this.sky, (-this.skyOffset + WIDTH, 0))
        # Floor color
        pygame.draw.rect(this.SCREEN, FLOOR_CLR, (0, HEIGH_HF, WIDTH, HEIGHT))

    def renderObj(this):
        objects = sorted(this.game.raycasting.objects,
                         key=lambda t: t[0], reverse=True)
        for depth, image, pos in objects:
            this.SCREEN.blit(image, pos)

    @staticmethod
    def getTXT(path, res=(TEXTURE_SZ, TEXTURE_SZ)):
        txt = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(txt, res)

    def loadWallTXT(this):
        return {
            1: this.getTXT('models/metalwall2.png'),
            2: this.getTXT('models/metalwall.png'),
            3: this.getTXT('models/flagwall.png'),
            4: this.getTXT('models/metaldoor.png'),
            5: this.getTXT('models/floor.png')
        }
