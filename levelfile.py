import pygame, pickle
import flingmain, platformfile, playerfile, enemyfile

class Level:
    
    def __init__(self):
        self.PLATFORM = 1
        self.ENEMY = 2

        self.player = playerfile.Player()
        self.playerSprite = pygame.sprite.Group()
        self.playerSprite.add(self.player)
        self.death = pygame.mixer.Sound("crafdeath.wav")

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
        self.platformSprites = pygame.sprite.Group()
        self.platforms = []
        # create a sprite group that holds the enemies & a list to keep track of them
        self.activeEnemySprites = pygame.sprite.Group()
        self.inactiveEnemySprites = pygame.sprite.Group()
        self.enemies = []
        enemyId = 0
        # traverse the layout and add sprites to their appropriate group by location
        for row in range(len(layout)):
            for col in range(len(layout[row])):
                if layout[row][col] == self.PLATFORM:
                    platform = platformfile.Platform(row, col)
                    self.platformSprites.add(platform)
                    self.platforms.append(platform)
                elif layout[row][col] == self.ENEMY:
                    enemy = enemyfile.Enemy(row, col, enemyId)
                    self.activeEnemySprites.add(enemy)
                    self.enemies.append(enemy)
                    enemyId += 1

        self.draw(window)

    def draw(self, window):
        # start to draw the level
        # draw background
        window.fill(flingmain.WHITE)

        # draw platforms
        self.platformSprites.draw(window)
        
        # draw enemies
        self.activeEnemySprites.draw(window)

        # draw enemy being held by the player
        self.inactiveEnemySprites.draw(window)
        
        # draw player
        self.playerSprite.draw(window)
        
    def update(self, window, amt):

        self.player.update(self.platformSprites)

        for e in self.enemies:
            e.update()

        playerEnemyColl = pygame.sprite.spritecollide(self.player, self.activeEnemySprites, False)
        if playerEnemyColl:
            if self.player.grabbing:
                for e in playerEnemyColl:
                    e.deactivate()
                    self.activeEnemySprites.remove(e)
                    self.inactiveEnemySprites.add(e)
                    if e not in self.player.holding:
                        self.player.holding.append(e)
            else:
                return False

        for e in self.inactiveEnemySprites:
            deadEnemies = pygame.sprite.spritecollide(e, self.activeEnemySprites, True)
            wallHitEnemies = pygame.sprite.spritecollide(e, self.platformSprites, False)
            if deadEnemies:
                self.inactiveEnemySprites.remove(e)
                self.death.play()
            if wallHitEnemies:
                self.inactiveEnemySprites.remove(e)
                self.death.play()

        if self.player.rect.y > 700:
            return False
        
        if self.player.booped:
            if amt > 0:
                amt = -7
            else:
                amt = 7

        if not self.activeEnemySprites and not self.inactiveEnemySprites:
            return False
        
        self.scroll(amt)
        return True
        
    def scroll(self, amt):

        if amt > 0:
            self.player.face_left()
        if amt < 0:
            self.player.face_right()
        
        for p in self.platforms:
            p.move_x(amt)

        for e in self.enemies:
            e.move_x(amt)

    def start(self, window):
        window.fill(flingmain.WHITE)
        startGameText = pygame.font.SysFont("Courier New", 48, True)
        startGameImage = startGameText.render("Start Game?", False, flingmain.GREEN)
        window.blit(startGameImage, (250, 100))
        questionText = pygame.font.SysFont("Courier New", 24)
        questionImage = questionText.render("Press Enter to start", False, flingmain.BLACK)
        window.blit(questionImage, (265, 200))

    def end(self, window):
        window.fill(flingmain.BLACK)
        gameOverText = pygame.font.SysFont("Courier New", 48, True)
        gameOverImage = gameOverText.render("Game Over!", False, flingmain.RED)
        window.blit(gameOverImage, (250, 100))
        continueText = pygame.font.SysFont("Courier New", 24)
        continueImage = continueText.render("Press Enter to restart", False, flingmain.WHITE)
        window.blit(continueImage, (242, 200))
        
        








