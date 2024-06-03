import pygame
import sys

# from Vertex import draw_graph
from pygame import Vector2
from Vertex import init_neighbors
from Vertex import init_vertex
from ghost import Ghost
from map import Map
from pacman import Pacman
from menu import menu
from ghost import Ghost
from path import Path
from left_lifes import live
from seeds import draw_seeds, init_seeds, Small_seed

SIZE = WIDTH, HEIGHT = 550, 600

def main():
    record1 = int(0)  # для таблицы рекордов
    record2 = int(0)
    record3 = int(0)
    clr = 0, 0, 0
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen.fill(clr)
    vertex_arr = []
    init_vertex(vertex_arr)
    init_neighbors(vertex_arr)

    seeds_arr = []
    init_seeds(seeds_arr)
    for seed in seeds_arr:
        seed.position += Vector2(-10, -10)

    paths = Path(vertex_arr)

    hero = Pacman(vertex_arr[47], vertex_arr)
    ghost1 = Ghost(1, vertex_arr[70], paths)
    ghost2 = Ghost(2, vertex_arr[68], paths)
    ghost3 = Ghost(3, vertex_arr[67], paths)
    ghost4 = Ghost(4, vertex_arr[69], paths)

    #   clock object for fps
    clock = pygame.time.Clock()
    pause = False

    menu(screen)
    screen.fill(clr)
    pygame.display.flip()


    map = Map()

    clr_i = 0
    wait_for_end = False
    wait_for_good_end = False
    gameover = False
    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.KEYDOWN:
                if event.unicode == "p":
                    pause = not pause
        if wait_for_end:

            f1 = pygame.font.SysFont('serif', 50)
            clr_i = min(clr_i + 0.2, 255)

            text1 = f1.render('YOU DIED', False, (clr_i, 0, 0))
            screen.blit(text1, (WIDTH // 2, HEIGHT // 2))
            pygame.display.flip()
            screen.fill(clr)
            pygame.time.wait(0)
            if pygame.time.get_ticks() - start_time > 4000:
                gameover = True
            continue

        if wait_for_good_end:
            f1 = pygame.font.SysFont('serif', 50)
            clr_i = min(clr_i + 0.2, 255)
            text1 = f1.render('YOU WON', False, (0, clr_i, 0))
            screen.blit(text1, (WIDTH // 2, HEIGHT // 2))
            pygame.display.flip()
            screen.fill(clr)
            pygame.time.wait(0)
            if pygame.time.get_ticks() - start_time > 4000:
                gameover = True
            continue
        
        map.render(screen)

        draw_seeds(screen, seeds_arr)

        hero.render(screen)
        ghost1.render(screen)
        ghost2.render(screen)
        ghost3.render(screen)
        ghost4.render(screen)
        # Pause logic
        if not pause:
            hero.move()
            # Movement of ghosts 
            ghost1.move(hero.get_v())
            ghost2.move(hero.get_v())
            ghost3.move(hero.get_v())
            ghost4.move(hero.get_v())
        else:
            f1 = pygame.font.SysFont('serif', 100)
            pause_text = f1.render('PAUSE', False, (0, 255, 0))
            screen.blit(pause_text, (125, 200))

        for seed in seeds_arr:
            if hero.collision_seeds(seed) and seed.is_eaten == False:
                seed.eaten()
        
        if Small_seed.cnt_eaten_seeds == len(seeds_arr) - 5:
            wait_for_good_end = True
            start_time = pygame.time.get_ticks()
        
        if Ghost.fear == False and (hero.collide_ghosts(ghost1) or hero.collide_ghosts(ghost2) or hero.collide_ghosts(ghost3) or hero.collide_ghosts(ghost4)):
            hero.got_hit()
            lives = Pacman.lives
            if Pacman.lives == 0:
                start_time = pygame.time.get_ticks()
                wait_for_end = True
                continue
            hero = Pacman(vertex_arr[47], vertex_arr)
            Pacman.lives = lives
            ghost1 = Ghost(1, vertex_arr[70], paths)
            ghost2 = Ghost(2, vertex_arr[68], paths)
            ghost3 = Ghost(3, vertex_arr[67], paths)
            ghost4 = Ghost(4, vertex_arr[69], paths)
            clock.tick(1000)

        if Ghost.fear == True:
            if hero.collide_ghosts(ghost1):
                ghost1 = Ghost(1, vertex_arr[70], paths)
                Small_seed.points += Ghost.cur_given_points
                Ghost.cur_given_points *= 2
            if hero.collide_ghosts(ghost2):
                ghost2 = Ghost(2, vertex_arr[68], paths)
                Small_seed.points += Ghost.cur_given_points
                Ghost.cur_given_points *= 2
            if hero.collide_ghosts(ghost3):
                ghost3 = Ghost(3, vertex_arr[67], paths)
                Small_seed.points += Ghost.cur_given_points
                Ghost.cur_given_points *= 2
            if hero.collide_ghosts(ghost4):
                ghost4 = Ghost(4, vertex_arr[69], paths)
                Small_seed.points += Ghost.cur_given_points
                Ghost.cur_given_points *= 2

        #Result of eaten small seeds
        score_file = open("file.txt", "r")  # открытие файла для вывода таблицы рекордов
        lines = score_file.readlines()
        for line in lines:
            # print(line.strip())
            if (int(line.strip()) >= record1): record1 = int(line)
            if (int(line.strip()) >= record2 and int(line.strip()) <= record1): record2 = int(line)
            if (int(line.strip()) >= record3 and int(line.strip()) <= record1 and int(
                    line.strip()) < record2): record3 = int(line)
        score_file.close()  # закрытие файлa
        font = pygame.font.SysFont('serif', 30)
        text_result = Small_seed.points
        tr = font.render("SCORE: " + str(text_result), True, (255, 255, 255))
        best = font.render("BEST: " + str(record1), True, (255, 255, 255))
        screen.blit(tr, (350, 550))
        screen.blit(best, (150, 550))

        live(screen)
        
        pygame.display.flip()
        screen.fill(clr)
        
        #   makes game work in hard 30 fps
        clock.tick(30)
        # pygame.time.wait(1)
    else:
        f1 = pygame.font.SysFont('serif', 30)
        score_file = open("file.txt", "a+")  # открытие файла для записи результатов этой игры
        gototxt = Small_seed.points
        score_file.write(str(gototxt))
        score_file.write('\n')
        lines = score_file.readlines()
        score_file.close()  # закрытие файла

        score_file = open("file.txt", "r")  # открытие файла для вывода таблицы рекордов
        lines = score_file.readlines()
        for line in lines:
            # print(line.strip())
            if (int(line.strip()) >= record1): record1 = int(line)
            if (int(line.strip()) >= record2 and int(line.strip()) <= record1): record2 = int(line)
            if (int(line.strip()) >= record3 and int(line.strip()) <= record1 and int(
                line.strip()) < record2): record3 = int(line)
        score_file.close()  # закрытие файлa

        print(record1, record2, record3)
        text_score1 = f1.render(str(record1), False, (255, 255, 255))
        text_score2 = f1.render(str(record2), False, (255, 255, 255))
        text_score3 = f1.render(str(record3), False, (255, 255, 255))
        screen.blit(text_score1, (WIDTH - 450, HEIGHT - 500))
        screen.blit(text_score2, (WIDTH - 450, HEIGHT - 400))
        screen.blit(text_score3, (WIDTH - 450, HEIGHT - 300))
        pygame.display.flip()
        screen.fill(clr)
        pygame.time.wait(5000)
    sys.exit()


if __name__ == '__main__':
    main()
