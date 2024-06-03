import pygame
import sys

SIZE = WIDTH, HEIGHT = 800, 600

def table(screen):

    clr = 0, 0, 0
    record1 = int(0)  # для таблицы рекордов
    record2 = int(0)
    record3 = int(0)
    f1 = pygame.font.SysFont('serif', 30)
    score_file = open("file.txt", "r")  # открытие файла для вывода таблицы рекордов
    lines = score_file.readlines()
    for line in lines:
        print(line.strip())
        if (int(line.strip()) >= record1): record1 = int(line)
        if (int(line.strip()) >= record2 and int(line.strip()) <= record1): record2 = int(line)
        if (int(line.strip()) >= record3 and int(line.strip()) <= record1 and int(
                line.strip()) < record2): record3 = int(line)
    score_file.close()  # закрытие файлa


    text_score1 = f1.render(str(record1), False, (255, 255, 255))
    text_score2 = f1.render(str(record2), False, (255, 255, 255))
    text_score3 = f1.render(str(record3), False, (255, 255, 255))

    exit_text = f1.render('EXIT', False, (0, 0, 0))
    pygame.display.flip()
    screen.fill(clr)
    exit_rect = pygame.Rect(350, 450, 100, 50)



    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if  exit_rect.collidepoint(pos):
                    return
        screen.fill(clr)
        pygame.draw.rect(screen, (0, 255, 0), exit_rect)
        screen.blit(exit_text, (360, 460))
        screen.blit(text_score1, (WIDTH - 450, HEIGHT - 500))
        screen.blit(text_score2, (WIDTH - 450, HEIGHT - 400))
        screen.blit(text_score3, (WIDTH - 450, HEIGHT - 300))
        pygame.display.flip()
        pygame.time.wait(1)
    sys.exit()


def menu(screen):
    clr = 0, 0, 0
    pygame.init()
    screen.fill(clr)

    h1 = pygame.image.load('assets/pacman-logo.png')
    h1 = pygame.transform.scale(h1, (550, 150))
    h1_rect = h1.get_rect()
    h1_rect.center = (275, 150)

    f1 = pygame.font.SysFont('serif', 30)
    play_text = f1.render('PLAY', False, (0, 0, 0))
    footer = f1.render('Made by "Unicorn" team', False, (255, 255, 255))
    exit_text = f1.render('EXIT', False, (0, 0, 0))
    table_text = f1.render('TABLE', False, (0, 0, 0))
    
    play_rect = pygame.Rect(225, 250, 100, 50)
    exit_rect = pygame.Rect(225, 450, 100, 50)
    table_rect = pygame.Rect(225, 350, 100, 50)

    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(pos):
                    return
                if  exit_rect.collidepoint(pos):
                    gameover = True
                if  table_rect.collidepoint(pos):
                    a = 1
                    table(screen)
                    # Нарисовать таблицу
        screen.fill(clr)
        screen.blit(h1, h1_rect)
        screen.blit(footer, (125, 600))
        pygame.draw.rect(screen, (0, 255, 0), play_rect)
        screen.blit(play_text, (235, 260))
        pygame.draw.rect(screen, (0, 255, 0), exit_rect)
        screen.blit(exit_text, (235, 460))
        pygame.draw.rect(screen, (0, 255, 0), table_rect)
        screen.blit(table_text, (225, 360))
        pygame.display.flip()
        pygame.time.wait(1)
    sys.exit()


if __name__ == '__main__':
    menu(pygame.display.set_mode(SIZE))
