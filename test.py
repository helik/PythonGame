import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w,h))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()
screen = pygame.display.set_mode((600,800))
box = Box(400,200, 50, 50)

clock = pygame.time.Clock()

screen.fill((255,255,255))

pygame.display.flip()

box_sprite = pygame.sprite.RenderPlain()
box.add(box_sprite)

box_sprite.draw(screen)

pygame.display.flip()
for x in range(600):
    screen.fill((255,255,255))
    box.rect.y += 1
    box_sprite.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    
