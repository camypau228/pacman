import pygame
from pygame import Vector2
from pygame.locals import *
from map import Map
import Vertex
import sys
import copy
import time

# consts for ghost movement
STOP = 0
UP = 1
DOWN = -1
LEFT = 2
RIGHT = -2

#Screen's size
SIZE = WIDTH, HEIGHT = 800, 600

def dist(v1, v2):
    return ((v1.x - v2.x) ** 2 + (v1.y - v2.y) ** 2)

class Ghost(object):
    #Scared ghost/not scared ghost
    fear = False
    fear_begin = 0
    cur_given_points = 200
    
    def __init__(self, number_of_ghost, cur_v, paths):
        self.number_of_ghost = number_of_ghost
        self.directions = {STOP:Vector2(), UP:Vector2(0,-1), DOWN:Vector2(0,1), LEFT:Vector2(-1,0), RIGHT:Vector2(1,0)}

        # All paths from all vertexes to other
        self.paths = paths

        self.direction = STOP
        #   Ghost`s vertex on start
        self.cur_vertex = copy.deepcopy(cur_v)
        #   Ghost`s vertex on end
        self.target = copy.deepcopy(cur_v)
        #   Ghost`s current position
        self.position = (copy.copy(cur_v.position))
        #   Vertex in which pacman currently is
        self.pacmans_v = -1
        self.speed = 1
        # Ghost next steps to Pacman
        self.way = []
        self.cur_ind = 0
        self.is_moving = False
        self.time_found_way = -2500
        self.first_move = True
        if self.number_of_ghost == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/ghost_blue_left.png'), (27, 27))
        elif self.number_of_ghost == 2:
            self.image = pygame.transform.scale(pygame.image.load('assets/ghost_orange_left.png'), (27, 27))
        elif self.number_of_ghost == 3:
            self.image = pygame.transform.scale(pygame.image.load('assets/ghost_pink_left.png'), (27, 27))
        elif self.number_of_ghost == 4:
            self.image = pygame.transform.scale(pygame.image.load('assets/ghost_red_left.png'), (27, 27))
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update(self):
        # Checks if ghost reached his target
        if self.cur_vertex == self.target:
            self.is_moving = False
        # Checks if ghost is resting
        if self.is_moving == False:
            # Find new direction
            direction = self.getDirection()
            if direction == STOP or self.cur_vertex.neighbor[direction] == -1:
                return
            self.target = self.cur_vertex.neighbor[direction]
            self.is_moving = True
        else:
            # Using current path
            direction = self.direction

        if self.is_moving:
            self.position += self.directions[direction] * self.speed
        
        self.change_texture(direction)
        self.direction = direction
        # Checks if ghost missed the 'target' Vertex
        if dist(self.position, self.cur_vertex.position) >= dist(self.target.position, self.cur_vertex.position):
            self.position = copy.copy(self.target.position) 
            self.cur_vertex = self.target
            self.arrival_time = pygame.time.get_ticks()
            self.is_moving = False
            self.direction = STOP
        self.rect.center = self.position

    def getDirection(self):
        if self.cur_ind == len(self.way):
            return STOP
        ans = self.way[self.cur_ind]
        self.cur_ind += 1
        return ans

    def change_texture(self, direction):
        if Ghost.fear_begin + 5000 < pygame.time.get_ticks():
            Ghost.fear = False
            Ghost.cur_given_points = 200
        if (Ghost.fear):
            self.image = pygame.transform.scale(pygame.image.load('assets/ghost_fear_1.png'), (27, 27))
        else:
            if direction == 1:
                if self.number_of_ghost == 1:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_blue_up.png'), (27, 27))
                if self.number_of_ghost == 2:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_orange_up.png'), (27, 27))
                if self.number_of_ghost == 3:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_pink_up.png'), (27, 27))
                if self.number_of_ghost == 4:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_red_up.png'), (27, 27))
                self.rect = self.image.get_rect()
            if direction == -1:
                if self.number_of_ghost == 1:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_blue_down.png'), (27, 27))
                if self.number_of_ghost == 2:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_orange_down.png'), (27, 27))
                if self.number_of_ghost == 3:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_pink_down.png'), (27, 27))
                if self.number_of_ghost == 4:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_red_down.png'), (27, 27))
                self.rect = self.image.get_rect()
            if direction == 2:
                if self.number_of_ghost == 1:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_blue_left.png'), (27, 27))
                if self.number_of_ghost == 2:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_orange_left.png'), (27, 27))
                if self.number_of_ghost == 3:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_pink_left.png'), (27, 27))
                if self.number_of_ghost == 4:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_red_left.png'), (27, 27))
                self.rect = self.image.get_rect()
            if direction == -2: #right
                if self.number_of_ghost == 1:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_blue_right.png'), (27, 27))
                if self.number_of_ghost == 2:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_orange_right.png'), (27, 27))
                if self.number_of_ghost == 3:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_pink_right.png'), (27, 27))
                if self.number_of_ghost == 4:
                    self.image = pygame.transform.scale(pygame.image.load('assets/ghost_red_right.png'), (27, 27))
                self.rect = self.image.get_rect()
    
    def render(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, pacman_v):
        if self.first_move == True:
            self.begin_time = pygame.time.get_ticks()
            self.first_move = False
            return
        if self.begin_time + (self.number_of_ghost - 1) * 10000 > pygame.time.get_ticks():
            return
        if pacman_v != self.pacmans_v and self.time_found_way + 1000 < pygame.time.get_ticks():
            self.pacmans_v = pacman_v
            self.way = self.paths.get_path(self.target.num, pacman_v.num)
            self.cur_ind = 0
            self.time_found_way = pygame.time.get_ticks()
        self.update()

    def get_rect(self):
        return self.rect

def main():
    clr = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(clr)

    vertex_arr = []
    Vertex.init_vertex(vertex_arr)
    Vertex.init_neighbors(vertex_arr)
    
    ghost1 = Ghost(1, vertex_arr[6], vertex_arr)
    ghost2 = Ghost(2, vertex_arr[1], vertex_arr)
    ghost3 = Ghost(3, vertex_arr[63], vertex_arr)
    ghost4 = Ghost(4, vertex_arr[66], vertex_arr)

    
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
        pygame.display.flip()
        screen.fill(clr)
        Map.render(Map(), screen)
        
        ghost1.move(vertex_arr[30])
        ghost2.move(vertex_arr[30])
        ghost3.move(vertex_arr[30])
        ghost4.move(vertex_arr[30])

        ghost1.render(screen)
        ghost2.render(screen)
        ghost3.render(screen)
        ghost4.render(screen)

        pygame.time.wait(0)
    sys.exit()

#for tests    
if __name__ == '__main__':
    main()

