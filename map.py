import pygame

SIZE = WIDTH, HEIGHT = 800, 600

class Map():

    def __init__(self):

        self.image = pygame.image.load('assets/background.png')
        self.image = pygame.transform.scale(self.image, (550, 550))
        self.rect = self.image.get_rect()
        self.position = (0, 0)

    def render(self, screen):
        p = self.position
        screen.blit(self.image, self.rect)
