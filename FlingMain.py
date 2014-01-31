import pygame, sys
import levelfile

# RGB Color definitions
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

HEIGHT = 600
WIDTH = 800

# main class, houses main loop of gamed
class FlingMain:
                                                          
    def start_game(self, waitStart=True, width = WIDTH, height = HEIGHT):

        self.width = width
        self.height = height
        
        pygame.init()
        
        screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Boopin'-Ass Game")

        clock = pygame.time.Clock()

        firstLevel = levelfile.Level()

        self.main_loop(screen, firstLevel, clock, waitStart)

    def main_loop(self, window, level, clock, delayStart):
        run = True
        waitStart = delayStart
        waitEnd = True
        scrollAmt = 0
        level.build(window)
        pygame.display.flip()

        while waitStart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #user clicks close
                    waitStart = False
                    run = False
                    waitEnd = False
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                waitStart = False
                
            level.start(window)
            
            pygame.display.flip()
        
        while run:
            keys = pygame.key.get_pressed()
            
            if keys[pygame.K_d]:
                scrollAmt -= 4
            if keys[pygame.K_a]:
                scrollAmt += 4
            if keys[pygame.K_SPACE]:
                level.player.jump()
            if keys[pygame.K_u]:
                level.player.grabbing = True
            else:
                level.player.grabbing = False
            
            run = level.update(window, scrollAmt)
            level.draw(window)
            pygame.display.flip()
            clock.tick(60)
            scrollAmt = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #user clicks close
                    run = False
                    waitEnd = False
                
        while waitEnd:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #user clicks close
                    waitEnd = False
                
            keys = pygame.key.get_pressed()

            if keys[pygame.K_RETURN]:
                self.start_game(False)
                
            level.end(window)
            
            pygame.display.flip()
        
        pygame.quit()
