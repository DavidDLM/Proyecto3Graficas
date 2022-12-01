# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

import pygame
import math
import numpy as np
from variables import *

# ALGORITMO RAYCASTING
class Raycasting:
    def __init__(this, game):
        this.game = game
        this.rcResult = []
        this.objRenderer = []
        this.txts = this.game.renderer.wallTXT

    def drawObject(this):
        this.objects = []
        for r, v in enumerate(this.rcResult):
            depth, projHeight, txt, offset = v
            if projHeight < HEIGHT:
                wallCol = this.txts[txt].subsurface(
                    offset * (TEXTURE_SZ - SCALE), 0, SCALE, TEXTURE_SZ
                )
                wallCol = pygame.transform.scale(
                    wallCol, (SCALE, projHeight))
                wallPos = (r * SCALE, HEIGH_HF - projHeight // 2)
            else:
                heightTXT = TEXTURE_SZ * HEIGHT / projHeight
                wallCol = this.txts[txt].subsurface(
                    offset * (TEXTURE_SZ - SCALE), TEXTURE_HF -
                    heightTXT // 2,
                    SCALE, heightTXT
                )
                wallCol = pygame.transform.scale(
                    wallCol, (SCALE, HEIGHT))
                wallPos = (r * SCALE, 0)

            this.objects.append((depth, wallCol, wallPos))

    def raycast(this):
        # Clr
        this.rcResult = []

        # Angulo XY
        angX, angY = this.game.player.pos

        # Player posicion XY
        mapX, mapY = this.game.player.map_pos

        vertTXT = 1
        horTXT = 2
        startingAngle = this.game.player.angle - FOV_HF + 0.0001
        for r in range(CASTED_RAYS):
            sinA = np.sin(startingAngle)
            cosA = np.cos(startingAngle)

            # Horizontal
            horY, dy = (mapY + 1, 1) if sinA > 0 else (mapY - 1e-6, -1)

            horDepth = (horY - angY) / sinA
            horX = angX + horDepth * cosA

            deltaDepth = dy / sinA
            dx = deltaDepth * cosA

            for i in range(MAX_DEPTH):
                pixel = int(horX), int(horY)
                if pixel in this.game.MAP.world:
                    horTXT = this.game.MAP.world[pixel]
                    break
                horX += dx
                horY += dy
                horDepth += deltaDepth

            # Vertical
            vertX, dx = (mapX + 1, 1) if cosA > 0 else (mapX - 1e-6, -1)

            vertDepth = (vertX - angX) / cosA
            vertY = angY + vertDepth * sinA

            deltaDepth = dx / cosA
            dy = deltaDepth * sinA

            for i in range(MAX_DEPTH):
                pixel = int(vertX), int(vertY)
                if pixel in this.game.MAP.world:
                    vertTXT = this.game.MAP.world[pixel]
                    break
                vertX += dx
                vertY += dy
                vertDepth += deltaDepth

            # Depth, offset de texturas para que no se vean raras
            if vertDepth < horDepth:
                depth, txt = vertDepth, vertTXT
                vertY %= 1
                offset = vertY if cosA > 0 else (1 - vertY)
            else:
                depth, txt = horDepth, horTXT
                horX %= 1
                offset = (1 - horX) if sinA > 0 else horX

            # pygame.draw.line(this.game.SCREEN, 'yellow', (100 * angX, 100 * angY),
                # (100 * angX + 100 * depth * cosA, 100 * angY + 100 * depth * sinA), 2)

            # Shading
            # clr = 255 / (1 + d * d * 0.0001)
            clr = [255 / (1 + depth ** 5 * 0.00002)] * 3

            # Depth bug
            depth *= np.cos(this.game.player.angle - startingAngle)

            # 3D proyeccion
            projHeight = DISTANCE / (depth + 0.0001)

            # 3D proyeccion
            # pygame.draw.rect(this.game.SCREEN, clr, (r * SCALE,
            #                 HEIGH_HF - projHeight // 2, SCALE, projHeight))

            # Resultado de raycasting
            this.rcResult.append((depth, projHeight, txt, offset))

            startingAngle += DELTA_ANG

    def update(this):
        this.raycast()
        this.drawObject()
