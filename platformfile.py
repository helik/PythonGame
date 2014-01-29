import pygame

class Platform(pygame.sprite.Sprite):

    def __init__(self, row, col):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.image = pygame.image.load("Textures/grass.png").convert_alpha()
        self.rect = pygame.Rect(self.col*50,self.row*50,50,50)#(self.col * self.image.get_width(),\
                                #self.row * self.image.get_height(),\
                          #      self.image.get_width(), self.image.get_height())

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
        
    
