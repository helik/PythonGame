import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        #level will scroll past player, so x position is fixed
        self.xPos = 250;
        self.yPos = 650; #initial y position
        self.image = pygame.image.load("Textures/player.png").convert_alpha()
        self.rect = pygame.Rect(xPos, yPos, 75, 75)
