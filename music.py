import pygame


class Music:
    def __init__(this, game):
        this.game = game
        pygame.mixer.init()
        this.path = 'models/music/'
        this.fire = pygame.mixer.Sound(this.path + 'Gun.mp3')
        this.music = pygame.mixer.music.load(this.path + 'Abyss.mp3')
        pygame.mixer.music.set_volume(0.5)
