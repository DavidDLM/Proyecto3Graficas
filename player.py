# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

from variables import *
import pygame
import math


class Player:
    def __init__(this, game):
        this.game = game
        this.x = PLAYER_X # Coordenadas desde variables
        this.y = PLAYER_Y
        this.angle = PLAYER_ANG
        this.fire = False

    def gunFire(this, event): # Accion de disparar con el boton izquierdo
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not this.fire and not this.game.gun.reload:
                this.game.music.fire.play()
                this.fire = True
                this.game.gun.reload = True

    def mov(this): # MOVIMIENTO DEL JUGADOR
        sinA = math.sin(this.angle)
        cosA = math.cos(this.angle)
        dx, dy = 0, 0
        speed = PLAYER_SP * this.game.delta
        speedSN = speed * sinA
        speedCN = speed * cosA

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speedCN
            dy += speedSN
        if keys[pygame.K_s]:
            dx += -speedCN
            dy += -speedSN
        if keys[pygame.K_a]:
            dx += speedSN
            dy += -speedCN
        if keys[pygame.K_d]:
            dx += -speedSN
            dy += speedCN

        this.collision(dx, dy) # Check de colisiones

        """
        if keys[pygame.K_LEFT]:
            this.angle -= PLAYER_ROT * this.game.delta
        if keys[pygame.K_RIGHT]:
            this.angle += PLAYER_ROT * this.game.delta
        """

        this.angle %= math.tau

    def walls(this, x, y):
        return (x, y) not in this.game.MAP.world

    def collision(this, dx, dy): # Manejar colisiones
        scale = PLAYER_SZ / this.game.delta
        if this.walls(int(this.x + dx * scale), int(this.y)):
            this.x += dx
        if this.walls(int(this.x), int(this.y + dy * scale)):
            this.y += dy

    def drawPlayer(this):
        # pygame.draw.line(this.game.SCREEN, 'yellow', (this.x * 100, this.y * 100),
        #                (this.x * 100 + WIDTH * math.cos(this.angle),
        #                this.y * 100 + WIDTH * math. sin(this.angle)), 2)
        pygame.draw.circle(this.game.SCREEN, 'green',
                           (this.x * 100, this.y * 100), 15)

    def mouse(this): # Movimiento con mouse
        mX, mY = pygame.mouse.get_pos()
        if mX < LEFT_BORDER or mX > RIGHT_BORDER:
            pygame.mouse.set_pos([WIDTH_HF, HEIGH_HF])
        this.rel = pygame.mouse.get_rel()[0]
        this.rel = max(-MOVEMENT, min(MOVEMENT, this.rel))
        this.angle += this.rel * SENSITIVITY * this.game.delta

    def update(this): # Actualizar
        this.mov()
        this.mouse()

    # Propiedades del jugador para usar en el futuro    
    @property
    def pos(this):
        return this.x, this.y

    @property
    def map_pos(this):
        return int(this.x), int(this.y)
