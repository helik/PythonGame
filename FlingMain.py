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

# main class, houses main loop of game
class FlingMain:
                                                          
    def start_game(self, width = WIDTH, height = HEIGHT):

        self.width = width
        self.height = height
        
        pygame.init()
        
        screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Boopin'-Ass Game")

        clock = pygame.time.Clock()

        #instantiate new player and enemies
        player = []
        enemies = []

        firstLevel = levelfile.Level(player, enemies)

        self.main_loop(screen, firstLevel, clock, False, False)

    def main_loop(self, window, level, clock, stop, pause):
        level.draw(window)
        pygame.display.flip()
        
        if stop == True:
            # change to something more accessible to the user
            again = raw_input("Restart?\n")
            if again == 'yes':
                start_game()
        
        while stop == False:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    stop = True
                    pygame.quit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        if pause:
                            pause = False
                        else:
                            pause = True

            if stop == False and pause == False: 
                level.draw(window)
                level.update()
                pygame.display.flip()
                clock.tick(60)

            
                # main game loops
                # Update state of all entities
                # Read Player input

        pygame.quit()
