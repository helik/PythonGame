import pygame
import platformfile

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #level will scroll past player, so x position is fixed
        self.xPos = 300.0;
        self.yPos = 400.0; #initial y position
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
        self.falling = True
        self.hitTop = []
        self.hitLeft = False
        self.hitRight = False
        self.booped = False
    def face_left(self):
        self.image = self.leftImage

    def face_right(self):
        self.image = self.rightImage
        
    def update(self, platform_sprites):
        #check if player is touching platform
        platformHitList = pygame.sprite.spritecollide(self, platform_sprites, False)
        self.check_platform_collisions(platformHitList)

        # print "jumping: " + str(self.jumping) + " falling: " + str(self.falling) + " grounded: " + str(self.grounded)
        
        # at or past the top of the arc
        if self.yVel > 0:
            self.jumping = False
            self.falling = True
        
        if not platformHitList:
            #if the player isn't touching a platform, the player is either jumping or falling
            self.grounded = False
            self.yVel += 1
        else:
            # if the player is hitting the top of a platform
            if self.hitTop:
                # if the player is traveling upwards
                if self.jumping:
                    pass
                # once the player is no longer traveling upwards
                elif self.falling:
                    #check to see if the bottom of the sprite is hitting the top of platform
                    if self.check_height():
                        self.grounded = True
                        self.falling = False
                        self.yVel = 0.0
                        
                        # find which platforms the player is touching
                        # temp holds the first platform, just in case there aren't any others in the list 
                        temp = self.hitTop[0].rect
                        tempY = temp.top
                        for p in self.hitTop:
                            if p.rect.top > tempY:
                                temp = p.rect
                                tempY = temp.top

                        self.rect.bottom = temp.top + 1
                        self.yPos = self.rect.y
                    else:
                        # this is falling so it should act like it isn't touching any platforms
                        self.grounded = False
                        self.yVel += 1
                else:
                    self.grounded = False
                    self.yVel += 1

        self.yPos += self.yVel
        self.rect.y = int(self.yPos)
            
    def jump(self):
        if self.grounded and not self.jumping:
            self.grounded = False
            self.jumping = True
            self.falling = False
            self.yVel = -15

    def check_platform_collisions(self, platList):
        self.hitTop = []
        self.booped = False
        for p in platList:
            hitList = p.side_check(self)
            if hitList[p.TOP]:
                self.hitTop.append(p)
            self.hitLeft = hitList[p.LEFT]
            self.hitRight = hitList[p.RIGHT]
            if self.hitLeft or self.hitRight:
                self.booped = True

    def check_height(self):
        for p in self.hitTop:
            if (self.rect.bottom - p.rect.top) < 25:
                return True
        return False

    def get_hitLeft(self):
        return self.hitLeft

    def get_hitRight(self):
        return self.hitRight
