import pygame
import sys
from sounds import *
from board import *


pygame.init()


SCREEN_X = 800
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("My Pygame Game")
back_ground = pygame.image.load("chess_resourses/board.png").convert()
background = pygame.transform.scale(back_ground, (800, 600))  # 调整到窗口大小
start = pygame.image.load("chess_resourses/image copy.png").convert_alpha()
start.set_colorkey((255, 255, 255))

start_t = pygame.transform.scale(start, (150, 100))
back_groundmusic1 = True
back_groundmusic2 = False
start_width = start_t.get_width()
start_hight = start_t.get_height()
start_x = SCREEN_X/2 - start_width/2
start_y = SCREEN_Y/2 - start_hight/2
image_rect = start_t.get_rect(topleft=(start_x, start_y))

clicked = False


running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(background, (0, 0))
    screen.blit(start_t, (start_x, start_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print("Mouse clicked at:", x, y)
            if image_rect.collidepoint(mouse_pos) and clicked == False:
                print("yes")
                clicked = True
                run_board()
                back_groundmusic1 = False
                bgm_2()

            else:
                pass

    if back_groundmusic1 == True:
        bgm_1()

    pygame.display.update()

pygame.quit()
sys.exit()
