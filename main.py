import pygame
import sys
from sounds import *
from game import *
from timer import *


pygame.init()


SCREEN_X = 800
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("My Pygame Game")
back_ground = pygame.image.load("chess_resourses/board.png").convert()
background = pygame.transform.scale(
    back_ground, (800, 600))  # Resize background
start = pygame.image.load("chess_resourses/image copy.png").convert_alpha()
start.set_colorkey((255, 255, 255))
# Set up
start_t = pygame.transform.scale(start, (270, 170))
back_groundmusic1 = True
back_groundmusic2 = False
start_width = start_t.get_width()
start_hight = start_t.get_height()
start_x = SCREEN_X/2 - start_width/2
start_y = SCREEN_Y/2 - start_hight/2
image_rect = start_t.get_rect(topleft=(start_x, start_y))
pos_front = pygame.font.Font('freesansbold.ttf', 32)
# Plays music
bgm_1()
clicked = False

game = ChessGame
white_knight = game.get_piece_at("White", "B1")  # Knight at B1
black_pawn = game.get_piece_at("Black", "D7")    # Pawn at D7
white_pawn = game.get_piece_at("White", "D2")    # Pawn at D2
black_bishop = game.get_piece_at("Black", "C8")   # Bishop at C8
white_rook = game.get_piece_at("White", "A1")
print(game.get_piece_info(white_knight, white_knight))
print(game.get_piece_info(black_pawn, black_pawn))
print(game.get_piece_info(white_pawn, white_pawn))
print(game.get_piece_info(black_bishop, black_bishop))
print(game.get_piece_info(white_rook, white_rook))


running = True
# While loop that displays the starting screen
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
            score_display = pos_front.render(
                f"Score: {x, y}", True, (255, 255, 255))
            if image_rect.collidepoint(mouse_pos) and clicked == False:
                print("yes")
                clicked = True
                # Plays music two
                bgm_2()
                # Call run board from a different page
                run_board()
                clicked = False
            else:
                pass

    pygame.display.update()

pygame.quit()
sys.exit()
