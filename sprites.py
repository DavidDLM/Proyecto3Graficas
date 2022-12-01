# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

import math
import os
from collections import deque
import pygame
from variables import *


class Sprite:
    def __init__(this, game, path='models/sprites/5.png', pos=(10.8, 1.5), scale=0.3, shift=0):
        this.game = game
        this.game = game
        this.player = game.player
        this.x, this.y = pos
        this.image = pygame.image.load(path).convert_alpha() # Cargar sprite
        this.IM_WIDTH = this.image.get_width()
        this.IM_HF = this.image.get_width() // 2
        this.IMAGE_RAT = this.IM_WIDTH / this.image.get_height()
        this.dx, this.dy, this.theta, this.scrX, this.dist, this.normDist = 0, 0, 0, 0, 1, 1
        this.SPRITE_HFWD = 0
        this.SPRITE_SCL = scale
        this.SPRITE_HTSH = shift

    def getProjection(this): # Proyeccion de los sprites, y dejarlos en un lugar sin moverse
        proj = DISTANCE / this.normDist * this.SPRITE_SCL
        projW, projH = proj * this.IMAGE_RAT, proj

        image = pygame.transform.scale(this.image, (projW, projH))

        this.SPRITE_HFWD = projW // 2
        heightShtf = projH * this.SPRITE_HTSH
        pos = this.scrX - this.SPRITE_HFWD,  HEIGH_HF - projH // 2 * heightShtf

        this.game.raycasting.objects.append(
            (this.normDist, image, pos))

    def getSprite(this):
        dx = this.x - this.player.x
        dy = this.y - this.player.y
        this.dx, this.dy = dx, dy
        this.theta = np.arctan2(dy, dx)

        # Para vision del jugador diferencia de theta
        delta = this.theta - this.player.angle

        if(dx > 0 and this.player.angle > np.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        deltaRay = delta / DELTA_ANG
        this.scrX = (HALF_RAYS + deltaRay) * SCALE

        this.dist = np.hypot(dx, dy)
        this.normDist = this.dist * np.cos(delta)
        if -this.IM_HF < this.scrX < (WIDTH + this.IM_HF) and this.normDist > 0.5:
            this.getProjection()

    def update(this):
        this.getSprite()


class AnimatedSprite(Sprite):
    def __init__(this, game, path='models/sprites/animated/zombie1/1.png',
                 pos=(9, 5.5), scale=0.9, shift=0, time=120):
        # Super function -> parent: Sprite
        super().__init__(game, path, pos, scale, shift)
        this.time = time
        this.path = path.rsplit('/', 1)[0]
        this.imgs = this.getImgs(this.path)  # Get all images from the path
        this.prevTime = pygame.time.get_ticks()
        this.trigger = False

    def update(this):
        # Super function -> parent: Sprite
        super().update()
        this.compareTime()
        this.animate(this.imgs)

    def animate(this, imgs): # Animar rotando imagenes
        if this.trigger:
            imgs.rotate(-1)
            this.image = imgs[0]

    def compareTime(this):
        this.trigger = False
        # Comparar prev y curr time
        currTime = pygame.time.get_ticks()
        if currTime - this.prevTime > this.time:
            this.prevTime = currTime
            this.trigger = True

    def getImgs(this, path): # Obtener imagenes a usar con los paths para las animaciones
        imgs = deque()
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                img = pygame.image.load(path + '/' + file).convert_alpha()
                imgs.append(img)
        return imgs
