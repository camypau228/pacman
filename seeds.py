from math import inf
from pygame import Vector2
import sys
import pygame

SIZE = WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode(SIZE)

class Small_seed:
    points = 0
    cnt_eaten_seeds = 0

    def __init__(self, x = 0, y = 0):
        self.name = 'Small seed'
        self.image = pygame.image.load('assets/seed.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.position = Vector2(x, y)
        self.is_eaten = False

    def eaten(self):
        if self.is_eaten: return
        Small_seed.points += 10
        self.is_eaten = True
        Small_seed.cnt_eaten_seeds += 1

    def load(self, screen):
        if not self.is_eaten:
            screen.blit(self.image, self.position)

    def get_seed_rect(self):
        return self.rect

class Buff_seed:

    def __init__(self, x = 0, y = 0):
        self.name = 'Buff seed'
        self.image = pygame.image.load('assets/seed_big.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.position = Vector2(x, y)
        self.is_eaten = False

    def eaten(self):
        if not self.is_eaten:
            self.is_eaten = True

    def load(self, screen):
        if not self.is_eaten:
            screen.blit(self.image, self.position)

    def get_buff_seed_rect(self):
        return self.rect

def init_seeds(seeds_arr):
    seeds_arr.append(Small_seed(-50, -50))
    # Первая линия
    seeds_arr.append(Small_seed(66, 40))
    seeds_arr.append(Small_seed(85, 40))
    seeds_arr.append(Small_seed(104, 40))
    seeds_arr.append(Small_seed(123, 40))
    seeds_arr.append(Small_seed(142, 40))
    seeds_arr.append(Small_seed(161, 40))
    seeds_arr.append(Small_seed(180, 40))
    seeds_arr.append(Small_seed(195, 40))
    seeds_arr.append(Small_seed(220, 40))
    seeds_arr.append(Small_seed(237, 40))
    seeds_arr.append(Small_seed(297, 40))
    seeds_arr.append(Small_seed(245, 65))

    seeds_arr.append(Small_seed(313, 40))
    seeds_arr.append(Small_seed(297, 65))
    seeds_arr.append(Small_seed(332, 40))
    seeds_arr.append(Small_seed(351, 40))
    seeds_arr.append(Small_seed(370, 40))
    seeds_arr.append(Small_seed(389, 40))
    seeds_arr.append(Small_seed(408, 40))
    seeds_arr.append(Small_seed(427, 40))
    seeds_arr.append(Small_seed(446, 40))
    seeds_arr.append(Small_seed(465, 40))
    seeds_arr.append(Small_seed(485, 40))
    seeds_arr.append(Buff_seed(66, 65))
    seeds_arr.append(Buff_seed(485, 65))
    # Вторая линия
    seeds_arr.append(Small_seed(66, 90))
    seeds_arr.append(Small_seed(85, 90))
    seeds_arr.append(Small_seed(104, 90))
    seeds_arr.append(Small_seed(123, 90))
    seeds_arr.append(Small_seed(142, 90))
    seeds_arr.append(Small_seed(161, 90))
    seeds_arr.append(Small_seed(180, 90))
    seeds_arr.append(Small_seed(197, 90))
    seeds_arr.append(Small_seed(197, 117))
    seeds_arr.append(Small_seed(220, 90))
    seeds_arr.append(Small_seed(237, 90))
    seeds_arr.append(Small_seed(256, 90))
    seeds_arr.append(Small_seed(275, 90))
    seeds_arr.append(Small_seed(294, 90))
    seeds_arr.append(Small_seed(313, 90))
    seeds_arr.append(Small_seed(332, 90))
    seeds_arr.append(Small_seed(351, 90))
    seeds_arr.append(Small_seed(370, 90))
    seeds_arr.append(Small_seed(389, 90))
    seeds_arr.append(Small_seed(408, 90))
    seeds_arr.append(Small_seed(427, 90))
    seeds_arr.append(Small_seed(446, 90))
    seeds_arr.append(Small_seed(465, 90))
    seeds_arr.append(Small_seed(485, 90))
    seeds_arr.append(Small_seed(66, 117))
    seeds_arr.append(Small_seed(485, 117))
    # Третья линия
    seeds_arr.append(Small_seed(66, 144))
    seeds_arr.append(Small_seed(85, 144))
    seeds_arr.append(Small_seed(104, 144))
    seeds_arr.append(Small_seed(123, 144))
    seeds_arr.append(Small_seed(197, 144))
    seeds_arr.append(Small_seed(216, 144))
    seeds_arr.append(Small_seed(235, 144))
    seeds_arr.append(Small_seed(250, 144))
    seeds_arr.append(Small_seed(300, 144))
    seeds_arr.append(Small_seed(319, 144))
    seeds_arr.append(Small_seed(338, 144))
    seeds_arr.append(Small_seed(353, 144))
    seeds_arr.append(Small_seed(353, 117))
    seeds_arr.append(Small_seed(405, 144))
    seeds_arr.append(Small_seed(405, 117))
    seeds_arr.append(Small_seed(405, 65))
    seeds_arr.append(Small_seed(424, 144))
    seeds_arr.append(Small_seed(443, 144))
    seeds_arr.append(Small_seed(462, 144))
    seeds_arr.append(Small_seed(485, 144))
    # Четвертая линия
    # 1 и 2 вертикальная
    seeds_arr.append(Small_seed(142, 197))
    seeds_arr.append(Small_seed(142, 170))
    seeds_arr.append(Small_seed(142, 144))
    seeds_arr.append(Small_seed(142, 117))
    seeds_arr.append(Small_seed(142, 65))
    seeds_arr.append(Small_seed(142, 249))
    seeds_arr.append(Small_seed(142, 223))
    seeds_arr.append(Small_seed(142, 275))
    seeds_arr.append(Small_seed(142, 302))
    seeds_arr.append(Small_seed(142, 328))
    seeds_arr.append(Small_seed(142, 354))
    seeds_arr.append(Small_seed(142, 380))
    seeds_arr.append(Small_seed(142, 406))
    seeds_arr.append(Small_seed(142, 432))
    seeds_arr.append(Small_seed(142, 459))

    seeds_arr.append(Small_seed(405, 249))
    seeds_arr.append(Small_seed(405, 197))
    seeds_arr.append(Small_seed(405, 170))
    seeds_arr.append(Small_seed(405, 223))
    seeds_arr.append(Small_seed(405, 275))
    seeds_arr.append(Small_seed(405, 302))
    seeds_arr.append(Small_seed(405, 328))
    seeds_arr.append(Small_seed(405, 354))
    seeds_arr.append(Small_seed(405, 380))
    seeds_arr.append(Small_seed(405, 406))
    seeds_arr.append(Small_seed(405, 432))
    seeds_arr.append(Small_seed(405, 459))
    # Пятая линия
    seeds_arr.append(Small_seed(405, 249))
    # Шестая линия
    # Седьмая линия
    seeds_arr.append(Small_seed(66, 354))
    seeds_arr.append(Small_seed(85, 354))
    seeds_arr.append(Small_seed(104, 354))
    seeds_arr.append(Small_seed(123, 354))
    seeds_arr.append(Small_seed(164, 354))
    seeds_arr.append(Small_seed(179, 354))
    seeds_arr.append(Small_seed(197, 354))
    seeds_arr.append(Small_seed(215, 354))
    seeds_arr.append(Small_seed(232, 354))
    seeds_arr.append(Small_seed(250, 354))
    seeds_arr.append(Small_seed(250, 380))

    seeds_arr.append(Small_seed(300, 354))
    seeds_arr.append(Small_seed(300, 380))
    seeds_arr.append(Small_seed(319, 354))
    seeds_arr.append(Small_seed(338, 354))
    seeds_arr.append(Small_seed(353, 354))
    seeds_arr.append(Small_seed(372, 354))
    seeds_arr.append(Small_seed(391, 354))
    seeds_arr.append(Small_seed(405, 354))
    seeds_arr.append(Small_seed(427, 354))
    seeds_arr.append(Small_seed(446, 354))
    seeds_arr.append(Small_seed(465, 354))
    seeds_arr.append(Small_seed(485, 354))
    # Восьмая линия
    seeds_arr.append(Small_seed(66, 406))
    seeds_arr.append(Buff_seed(66, 380))
    seeds_arr.append(Small_seed(85, 406))
    seeds_arr.append(Small_seed(85, 432))
    seeds_arr.append(Small_seed(142, 406))
    seeds_arr.append(Small_seed(161, 406))
    seeds_arr.append(Small_seed(180, 406))
    seeds_arr.append(Small_seed(197, 406))
    seeds_arr.append(Small_seed(216, 406))
    seeds_arr.append(Small_seed(232, 406))
    seeds_arr.append(Small_seed(250, 406))
    seeds_arr.append(Small_seed(269, 406))
    seeds_arr.append(Small_seed(285, 406))
    seeds_arr.append(Small_seed(300, 406))
    seeds_arr.append(Small_seed(318, 406))
    seeds_arr.append(Small_seed(337, 406))
    seeds_arr.append(Small_seed(353, 406))
    seeds_arr.append(Small_seed(367, 406))
    seeds_arr.append(Small_seed(386, 406))
    seeds_arr.append(Small_seed(405, 406))
    seeds_arr.append(Small_seed(457, 406))
    seeds_arr.append(Small_seed(480, 406))
    seeds_arr.append(Buff_seed(485, 380))
    # Девятая линия
    seeds_arr.append(Small_seed(66, 459))
    seeds_arr.append(Small_seed(85, 459))
    seeds_arr.append(Small_seed(104, 459))
    seeds_arr.append(Small_seed(123, 459))
    seeds_arr.append(Small_seed(197, 459))
    seeds_arr.append(Small_seed(197, 432))
    seeds_arr.append(Small_seed(216, 459))
    seeds_arr.append(Small_seed(235, 459))
    seeds_arr.append(Small_seed(250, 459))
    seeds_arr.append(Small_seed(250, 484))
    seeds_arr.append(Small_seed(300, 459))
    seeds_arr.append(Small_seed(300, 484))
    seeds_arr.append(Small_seed(319, 459))
    seeds_arr.append(Small_seed(338, 459))
    seeds_arr.append(Small_seed(353, 459))
    seeds_arr.append(Small_seed(353, 432))
    seeds_arr.append(Small_seed(405, 459))
    seeds_arr.append(Small_seed(405, 432))
    seeds_arr.append(Small_seed(424, 459))
    seeds_arr.append(Small_seed(443, 459))
    seeds_arr.append(Small_seed(465, 459))
    seeds_arr.append(Small_seed(455, 432))
    seeds_arr.append(Small_seed(480, 459))
    # Десятая линия
    seeds_arr.append(Small_seed(66, 510))
    seeds_arr.append(Small_seed(66, 484))
    seeds_arr.append(Small_seed(85, 510))
    seeds_arr.append(Small_seed(104, 510))
    seeds_arr.append(Small_seed(123, 510))
    seeds_arr.append(Small_seed(142, 510))
    seeds_arr.append(Small_seed(161, 510))
    seeds_arr.append(Small_seed(180, 510))
    seeds_arr.append(Small_seed(199, 510))
    seeds_arr.append(Small_seed(220, 510))
    seeds_arr.append(Small_seed(237, 510))
    seeds_arr.append(Small_seed(256, 510))
    seeds_arr.append(Small_seed(275, 510))
    seeds_arr.append(Small_seed(294, 510))
    seeds_arr.append(Small_seed(313, 510))
    seeds_arr.append(Small_seed(332, 510))
    seeds_arr.append(Small_seed(351, 510))
    seeds_arr.append(Small_seed(370, 510))
    seeds_arr.append(Small_seed(389, 510))
    seeds_arr.append(Small_seed(408, 510))
    seeds_arr.append(Small_seed(427, 510))
    seeds_arr.append(Small_seed(446, 510))
    seeds_arr.append(Small_seed(465, 510))
    seeds_arr.append(Small_seed(485, 510))
    seeds_arr.append(Small_seed(485, 484))

    # Вторая линия

def draw_seeds(screen, seeds_arr):
    for v in seeds_arr:
        v.load(screen)

def main():
    clr = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(clr)

    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        draw_seeds(screen)
        pygame.display.flip()
        screen.fill(clr)
        pygame.time.wait(1)
    sys.exit()

if __name__ == '__main__':
    main()
