import pygame
import platformfile

class Enemy(pygame.sprite.Sprite):

    def __init__(self, row, col, enemyId):
        pygame.sprite.Sprite.__init__(self)
        #starting position
        self.row = row
        self.col = col
        self.paramList = [[400, True, 3], [100, True, 3], [400, True, 3], [400, False, 3],\
                          [200, True, 2], [150, True, 8], [600, False, 3]]
        self.image = pygame.image.load("Textures/CRAF.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = pygame.Rect(self.col * 50, self.row * 50 - 10, 60, 60)
        self.paceDist = self.paramList[enemyId][0]
        self.facingRight = self.paramList[enemyId][1]
        self.stepsTaken = 0
        self.step = self.paramList[enemyId][2]
        self.active = True
        self.flungRight = False
        self.flung = False

    def update(self):
        if self.active:
            self.move()
        else:
            self.rotate_image()
            if self.flung:
                if self.flungRight:
                    self.fly(7)
                else:
                    self.fly(-7)
            

    def move(self):
        if self.facingRight:
            self.rect.x += self.step
        else:
            self.rect.x -= self.step
            
        self.stepsTaken += self.step
        if self.stepsTaken > self.paceDist:
            self.facingRight =  not self.facingRight
            self.stepsTaken = 0

    def move_x(self, amt):
        if self.active or self.flung:
            self.rect.x += amt

    def fly(self, amt):
        self.rect.x += amt

    def deactivate(self):
        self.active = False

    def rotate_image(self):
        self.image = pygame.transform.rotate(self.image, 90)
        
    def fling(self, right):
        self.flungRight = right
        self.flung = True
        
