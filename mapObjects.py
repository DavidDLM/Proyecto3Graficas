# Basado en lo escrito por Coder Space:
# https://youtu.be/ECqUrT7IdqQ
# Basado en lo escrito por Code Monkey King tambien:
# https://youtu.be/Rt5rEW0jQjw
# E Ing. Dennis Aldana / Ing. Carlos Alonso

from sprites import *


class mapObjects:
    def __init__(this, game):
        this.game = game
        this.collection = []
        this.spritePath = 'models/sprites/'
        this.animSpritePath = 'models/sprites/animated/'
        addObject = this.addObject

        # Mapa
        addObject(Sprite(game))
        addObject(AnimatedSprite(game))
        addObject(AnimatedSprite(game, pos=(7, 1.5)))
        addObject(AnimatedSprite(game, path=this.animSpritePath +
                  'zombie2/1.png', pos=(14, 5.8), scale=0.6))
        addObject(AnimatedSprite(game, path=this.animSpritePath +
                  'zombie2/1.png', pos=(6.9, 7.8), scale=0.6))
        addObject(Sprite(game, path=this.spritePath +
                  '6.png', pos=(4.9, 5.5), scale=0.4))
        addObject(Sprite(game, path=this.spritePath +
                  '1.png', pos=(6.1, 5.5), scale=0.4))
        addObject(Sprite(game, path=this.spritePath +
                  '3.png', pos=(14.9, 5.5), scale=0.4))

    def update(this):
        [sprite.update() for sprite in this.collection]

    def addObject(this, sprite):
        this.collection.append(sprite)
