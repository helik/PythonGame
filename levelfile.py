import pygame, pickle
import flingmain, platformfile, playerfile

class Level:
    
    def __init__(self):
        self.PLATFORM = 1
        self.ENEMY = 2

        p = playerfile.Player()
        self.player = pygame.sprite.Group()
        self.player.add(p)

    # this is a list with numerical representations of the level
    def get_layout(self):
        with open("layoutList.pickle", "rb") as myRestoredList:
            layout = pickle.load(myRestoredList)
        return layout
    def get_background(self):
        pass

    def build(self, window):
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

        self.draw(window)

    def draw(self, window):
        # start to draw the level
        # draw background
        window.fill(flingmain.WHITE)

        # draw platforms
        self.platform_sprites.draw(window)
        
        # draw enemies
       # self.enemy_sprites.draw(window)

        # draw player
        self.player.draw(window)
        
    def update(self):

        #check if player is touching platform

        for p in self.platform_sprites:
            collision = pygame.sprite.collide_rect(self.player.sprites()[0], p)
            
            if collision:
                self.player.sprites()[0].grounded = True

        if not self.player.sprites()[0].grounded:
            self.player.sprites()[0].rect.y += 10
        else:
            currY = self.player.sprites()[0].rect.y + 75

            self.player.sprites()[0].rect.y = currY / 50 * 50 - 75 #herpaderp

        # set player to proper height if grounded
        
    def scroll(self, window, amt):
        # DONT 4GET TO UPDATE THE ENEMY POSITIONS >:O

        if amt > 0:
            self.player.sprites()[0].face_left()
        if amt < 0:
            self.player.sprites()[0].face_right()
        
        for p in self.platforms:
            p.rect.x += amt
        print amt

