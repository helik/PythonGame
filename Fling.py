import pygame, sys

# RGB Color definitions
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)
green = (0, 255, 0)
red   = (255, 0, 0)
blue  = (0, 0, 255)

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

        # define level firstLevel

        main_loop(screen, firstLevel, clock, False, False)

    def main_loop(window, level, clock, stop, pause):
        level.assets.draw(window)
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
                level.assets.draw(screen)
                pygame.display.flip()
                clock.tick(60)

                # main game loops
                # Update state of all entities
                # Read Player input

            pygame.quit()
    
    def LoadSprites(self):
        """Load the sprites that we need"""
        self.snake = Snake()
        self.snake_sprites = pygame.sprite.RenderPlain((self.snake))
        
        """figure out how many pellets we can display"""
        nNumHorizontal = int(self.width/64)
        nNumVertical = int(self.height/64)       
        """Create the Pellet group"""
        self.pellet_sprites = pygame.sprite.Group()
        """Create all of the pellets and add them to the 
        pellet_sprites group"""
        for x in range(nNumHorizontal):
            for y in range(nNumVertical):
                self.pellet_sprites.add(Pellet(pygame.Rect(x*64, y*64, 64, 64)))
