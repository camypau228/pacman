import pygame
from pygame import Vector2
from pygame.locals import *
import sys
import Vertex
import copy
from ghost import Ghost
import seeds
# consts for pacman movement
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

#   Screen`s size
SIZE = WIDTH, HEIGHT = 800, 600

def dist(v1, v2):
    return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

class Pacman(object):
    #   Pacman`s lives
    lives = 3

    def __init__(self, cur_v, vertex_arr):
        #   Object name
        self.name = 'Pacman'
        #   Pacman`s position when init (=> doesnt move)
        self.direction = STOP
        #   dictionary that contains directions
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}
        #   Pacman`s speed
        self.speed = 1.2
        #   Pacman`s vertex on start
        self.cur_vertex = copy.deepcopy(cur_v)
        #   Pacman`s vertex on end
        self.target = copy.deepcopy(cur_v)
        #   Pacman`s current position
        self.position = (copy.deepcopy(cur_v)).position
        #   Pacman`s arrival time to 'target' Vertex
        self.arrival_time = 0
        #   Pacman`s image
        self.image = pygame.transform.scale(pygame.image.load('assets/pacman_right.png'), (27, 27))
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        #   Map of vertexes
        self.map = copy.deepcopy(vertex_arr)

    def got_hit(self):
        Pacman.lives -= 1

    #   Updates position and direction
    def update(self):
        direction = self.getValidKey()
        # Changes direction on the opposite
        if direction == -self.direction:
            self.target, self.cur_vertex = self.cur_vertex, self.target
        # Searching new 'target' Vertex
        elif direction != STOP and self.cur_vertex.neighbor[direction] != -1 and self.target == self.cur_vertex:
            self.target = copy.deepcopy(self.cur_vertex.neighbor[direction])
            self.position = copy.deepcopy(self.cur_vertex.position)
        # Non-correct direction
        elif direction != self.direction and direction != -self.direction and self.target != self.cur_vertex and self.direction != 0:
            direction = self.direction
        self.change_texture(direction)
        self.position += self.directions[direction] * self.speed
        self.direction = direction
        # Checks if pacman missed the 'target' Vertex
        if dist(self.position, self.cur_vertex.position) > dist(self.target.position, self.cur_vertex.position):
            self.position = copy.deepcopy(self.target.position)
            self.cur_vertex = self.target
            self.arrival_time = pygame.time.get_ticks()
        self.rect.center = self.position


    def move(self):
        self.update()
        if self.cur_vertex.position == self.map[32].position and self.target == self.cur_vertex:
            self.cur_vertex = copy.deepcopy(self.map[27])
            self.target = copy.deepcopy(self.map[28])
            self.position = copy.deepcopy(self.cur_vertex.position)
        elif self.cur_vertex.position == self.map[27].position and self.target == self.cur_vertex:
            self.cur_vertex = copy.deepcopy(self.map[32])
            self.target = copy.deepcopy(self.map[31])
            self.position = copy.deepcopy(self.cur_vertex.position)

    #   Returns direction number
    def getValidKey(self):
        # which key pressed right now
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_UP] or key_pressed[K_w]:
            return UP
        if key_pressed[K_DOWN] or key_pressed[K_s]:
            return DOWN
        if key_pressed[K_LEFT] or key_pressed[K_a]:
            return LEFT
        if key_pressed[K_RIGHT] or key_pressed[K_d]:
            return RIGHT
        return STOP

    def change_texture(self, direction):
        if direction == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/pacman_up.png'), (27, 27))
            self.rect = self.image.get_rect()
        if direction == -1:
            self.image = pygame.transform.scale(pygame.image.load('assets/pacman_down.png'), (27, 27))
            self.rect = self.image.get_rect()
        if direction == 2:
            self.image = pygame.transform.scale(pygame.image.load('assets/pacman_left.png'), (27, 27))
            self.rect = self.image.get_rect()
        if direction == -2:
            self.image = pygame.transform.scale(pygame.image.load('assets/pacman_right.png'), (27, 27))

    #   Draw`s pacman
    def render(self, screen):
        screen.blit(self.image, self.rect)

    def get_pacman_rect(self):
        return self.rect

    def collision_seeds(self, seeds):
        if seeds.is_eaten:
            return False
        if (self.rect.colliderect(seeds.rect)) and (seeds.name == 'Small seed'): #collision check   
            return True
        if (self.rect.colliderect(seeds.rect)) and (seeds.name == 'Buff seed'):
            Ghost.fear = True
            Ghost.fear_begin = pygame.time.get_ticks()
            return True
    
    def get_v(self):
        return self.target

    def collide_ghosts(self, ghost) -> bool:
        if self.rect.colliderect(ghost.get_rect()):
            return True
        return False
    
def main():
    clr = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(clr)
    pc = Pacman(Vertex.Vertex(250, 406))
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        pygame.display.flip()
        screen.fill(clr)

        # Vertex.draw_graph()
        # screen.blit(pc)
        Vertex.draw_graph()
        pc.render(screen)
        pc.move()
        pygame.time.wait(0)
    sys.exit()





# for tests
if __name__ == '__main__':
    main()

