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
        self.jumping = False

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
        elif not self.jumping:
            # If the player is currently on the upward part of the jump arc, they
            # they shouldn't check to see if they're grounded. Otherwise they'd get stuck
            self.grounded = True
            self.yVel = 0.0
            # find which platforms the player is touching
            # temp holds the first platform, just in case there aren't any others in the list 
            temp = platformHitList[0].rect
            tempY = temp.top
            for p in platformHitList:
                if p.rect.top > tempY:
                    temp = p.rect
                    tempY = temp.top

            self.rect.bottom = temp.top + 1
            self.yPos = self.rect.y

        self.yPos += self.yVel
        self.rect.y = int(self.yPos)

        if self.yVel >= 0 and self.jumping and not self.grounded:
            self.jumping = False
            
    def jump(self):
        if self.grounded and not self.jumping:
            self.grounded = False
            self.jumping = True
            self.yVel = -15

        
