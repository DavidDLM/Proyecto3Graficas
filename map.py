# Map
# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso
import pygame
import sys
import numpy as np

MAPS = 16 # Tamano del mapa
floor = False # Identificar paredes y piso
MAP = [
    [1,     1,     1,     1,     1,     1,     1,     1,
        1,     1,     1,     1,     1,     1,     1,     1],
    [1,     1, floor, floor, floor, floor, floor, floor, floor,
        floor, floor,     2, floor,     2, floor,     1],
    [1, floor, floor, floor, floor, floor, floor, floor, floor,
        floor, floor, floor, floor, floor, floor,     1],
    [4, floor, floor, floor, floor, floor, floor, floor, floor,
        floor, floor, floor, floor, floor, floor,     4],
    [4, floor, floor,     2, floor, floor,     2, floor, floor,
        floor, floor,     3, floor, floor, floor,     4],
    [1, floor, floor, floor, floor,     2, floor, floor, floor,
        floor, floor, floor, floor, floor, floor,     1],
    [1, floor, floor, floor,     2, floor,     2, floor,
        2,     2, floor, floor, floor,     2, floor,     1],
    [1, floor, floor, floor, floor, floor, floor,     2, floor,
        floor, floor,     2, floor,     2, floor,     1],
    [1,     1,     1,     1,     1,     1,     1,     1,
        1,     1,     1,     1,     1,     1,     1,     1]
]


class Map:
    def __init__(this, game):
        this.game = game
        this.MAP = MAP
        this.world = {}
        this.getMap()

    def getMap(this):
        for j, r in enumerate(this.MAP):
            for i, v in enumerate(r):
                if v:
                    this.world[(i, j)] = v

    def drawMap(this): # Dibujar mapa segun MAP
        """
        for r in range(8):
            # Loop columnas
            for c in range(MAPS):
                # Calc index pixel
                pixel = r*MAPS+c
                # Draw
                pygame.draw.rect(SCREEN, (211, 211, 211)
                                if MAP[pixel] == 1 else (111, 111, 111), 
                                (c * PIXEL_SIZE, r * PIXEL_SIZE, PIXEL_SIZE - 2, PIXEL_SIZE-2))  
        """
        [pygame.draw.rect(this.game.SCREEN, (200, 200, 200), (pos[0]
                          * 100, pos[1] * 100, 100, 100), 2) for pos in this.world]
