import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #level will scroll past player, so x position is fixed
        self.xPos = 300.0;
        self.yPos = 50.0; #initial y position
        self.yVel = 0.0;
        self.leftImage = pygame.image.load("Textures/player.png").convert_alpha()
        self.rightImage = pygame.image.load("Textures/player.png").convert_alpha()
        self.leftImage = pygame.transform.scale(self.rightImage, (75, 75))
        self.image = self.leftImage
        self.rightImage = pygame.transform.flip(pygame.transform.scale(self.leftImage, \
                                (75, 75)), True, False)
        self.rect = pygame.Rect(self.xPos, self.yPos, 75, 75)
        self.grounded = False

    def face_left(self):
        self.image = self.leftImage

    def face_right(self):
        self.image = self.rightImage
        
    def update(self, platform_sprites):
        #check if player is touching platform
        platformHitList = pygame.sprite.spritecollide(self, platform_sprites, False)

        if not platformHitList:
            #if the player isn't touching a platform, the player will fall
            self.grounded = False
            self.yVel += 1
        else:
            self.yVel = 0.0
            #find which platforms the player is touching
            for p in platformHitList:
                self.grounded = True
                # set the bottom of the player sprite to the top of the platform
                self.rect.bottom = p.rect.top

        self.yPos += self.yVel
        self.rect.y = int(self.yPos)



    def jump(self):
        self.grounded = False
        self.yVel = 100

        
