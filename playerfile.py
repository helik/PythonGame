import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #level will scroll past player, so x position is fixed
        self.xPos = 300.0;
        self.yPos = 50.0; #initial y position
        self.image = pygame.image.load("Textures/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = pygame.Rect(self.xPos, self.yPos, 75, 75)
        self.grounded = False
