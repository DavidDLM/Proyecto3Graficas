# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

# Gun inherits from AnimatedSprite because animated shot
from sprites import *


class Gun(AnimatedSprite):
    def __init__(this, game, path='models/sprites/animated/gun/1.png', scale=3, time=90):
        super().__init__(game=game, path=path, scale=scale, time=time)
        this.imgs = deque(
            [pygame.transform.smoothscale(img, (this.image.get_width() * scale, this.image.get_height() * scale))
             for img in this.imgs])
        this.gunPos = (
            WIDTH_HF + (this.imgs[0].get_width() * 0.5), HEIGHT - this.imgs[0].get_height())
        this.numImgs = len(this.imgs)
        this.reload = False
        this.frames = 0

    def shot(this):
        if this.reload:
            this.game.player.fire = False
            if this.trigger:
                this.imgs.rotate(-1)
                this.image = this.imgs[0]
                this.frames += 1
                if this.frames == this.numImgs:
                    this.reload = False
                    this.frames = 0

    def drawGun(this):
        this.game.SCREEN.blit(this.imgs[0], this.gunPos)

    def update(this):
        this.compareTime()
        this.shot()
