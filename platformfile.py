import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, row, col):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.image.load("Textures/grass.png").convert_alpha()
        self.rect = pygame.Rect(self.col*50,self.row*50,50,50)
        self.topRect = self.PlatformRect(self.rect.x + 5, self.rect.y, self.rect.w - 10, 1)
        self.leftRect = self.PlatformRect(self.rect.x, self.rect.y + 10, 3, self.rect.h + 30)
        self.rightRect = self.PlatformRect(self.rect.x + 50, self.rect.y + 10, 3, self.rect.h + 30)
        self.bottomRect = self.PlatformRect(self.rect.x, self.rect.y + 50, self.rect.w, 1)
        self.rectSprites = pygame.sprite.Group()
        self.rectSprites.add(self.topRect, self.leftRect, self.rightRect, self.bottomRect)
        self.sideList = [self.topRect, self.leftRect, self.rightRect, self.bottomRect]
        # constants so we don't lose track of where these sides are in the list
        self.TOP = 0
        self.LEFT = 1
        self.RIGHT = 2
        self.BOTTOM = 3

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col

    def move_x(self, amt):
        self.rect.x += amt
        for r in self.sideList:
            r.rect.x += amt

    # returns list of booleans the correspond to sides' position in the list
    def side_check(self, player):
        temp = []
        collidedSprites = pygame.sprite.spritecollide(player, self.rectSprites, False)
        for r in self.sideList:
            if r in collidedSprites:
                temp.append(True)
            else:
                temp.append(False)
        return temp

    class PlatformRect(pygame.sprite.Sprite):

        def __init__(self, x, y, w, h):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((w,h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
