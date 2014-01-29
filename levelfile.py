import pygame, pickle
import flingmain, platformfile

class Level:
    
    def __init__(self, player, enemies):

        self.player = player
        self.enemies = enemies

        self.PLATFORM = 1
        self.ENEMY = 2
        
    def get_player(self):
        pass

    # return sprite group
    def get_enemies(self):
        pass

    # return sprite group
    def get_platforms(self):
        pass

    # this is a list with numerical representations of the level
    def get_layout(self):
        with open("layoutList.pickle", "rb") as myRestoredList:
            layout = pickle.load(myRestoredList)
        return layout
    def get_background(self):
        pass

    def draw(self, window):
        layout = self.get_layout()
        
        # create a sprite group that holds the platforms & a list to keep track of them
        self.platform_sprites = pygame.sprite.Group()
        self.platforms = []
        # create a sprite group that holds the enemies & a list to keep track of them
     #   self.enemy_sprites = pygame.sprite.Group()
     #   self.enemies = []

        # traverse the layout and add sprites to their appropriate group by location
        for row in range(len(layout)):
            for col in range(len(layout[row])):
                if layout[row][col] == self.PLATFORM:
                    platform = platformfile.Platform(row, col)
                    self.platform_sprites.add(platform)
                    self.platforms.append(platform)
##                elif layout[row][col] == self.ENEMY:
##                    enemy = enemyfile.Enemy(row, col)
##                    self.enemy_sprites.add(enemy)
##                    self.enemies.append(enemy)

        # start to draw the level
        # draw background
        window.fill(flingmain.WHITE)

        # draw platforms
        self.platform_sprites.draw(window)
        
        # draw enemies
       # self.enemy_sprites.draw(window)
        
    def update(self):

        #check if player is touching platform

        for p in platform_sprites:
            if not pygame.collide_rect(self.player, p):
                player.yPos -= 10
                
