import pygame
import sys
from pacman import Pacman

def live(screen):
    lv1 = pygame.image.load('assets/pacman_left.png')
    lv1rect = lv1.get_rect()
    lv1rect.x = 70
    lv1rect.y = 560
    
    lv2 = pygame.image.load('assets/pacman_left.png')
    lv2rect = lv2.get_rect()
    lv2rect.x = 40
    lv2rect.y = 560
        
    lv3 = pygame.image.load('assets/pacman_left.png')
    lv3rect = lv3.get_rect()
    lv3rect.x = 10
    lv3rect.y = 560
        
    if Pacman.lives >= 3:
        screen.blit(lv1, lv1rect)
        screen.blit(lv2, lv2rect)
        screen.blit(lv3, lv3rect)
    if Pacman.lives == 2:
        screen.blit(lv2, lv2rect)
        screen.blit(lv3, lv3rect)
    if Pacman.lives == 1:
        screen.blit(lv3, lv3rect)
