# Main - Finshed...

# Imports
import pygame
import sys
from sounds import *
from game import *
from board import *

pygame.init()
# set screen size
SCREEN_X = 800
SCREEN_Y = 600
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption("Chess Game")  # Name the title Chess game
# Convert the image and load it
back_ground = pygame.image.load("chess_resourses/board.png").convert()
# Change the background's size, set it to the screen size
background = pygame.transform.scale(back_ground, (800, 600))
# Load start botton and convert it
start = pygame.image.load("chess_resourses/image copy.png").convert_alpha()
start.set_colorkey((255, 255, 255))  # Removes all white color from the image
start_t = pygame.transform.scale(
    start, (270, 170))  # Change Start botton's size
back_groundmusic1 = True  # Set background music# 1 to be True
back_groundmusic2 = False  # Set background music 2 to be False
start_width = start_t.get_width()  # Get start botton's width
start_hight = start_t.get_height()  # Get start botton's hight
start_x = SCREEN_X/2 - start_width/2  # Set Start botton's location
start_y = SCREEN_Y/2 - start_hight/2  # Set Start botton's location
# Creates a rectangle around the start botton
image_rect = start_t.get_rect(topleft=(start_x, start_y))
pos_front = pygame.font.Font('freesansbold.ttf', 32)  # Set the front
bgm_1()  # play bgm 1
clicked = False
chess_game = ChessGame()
# Set running to true
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()  # Store mouse position
    screen.blit(background, (0, 0))  # Display background at 0,0
    # Display Start botton at start_x and start_y
    screen.blit(start_t, (start_x, start_y))
    # Get event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit game function
            running = False  # Set dunning to false
        if event.type == pygame.MOUSEBUTTONDOWN:  # Get mouse
            x, y = event.pos  # Store mouse location
            # Check if mouse location at where start botton is
            if image_rect.collidepoint(mouse_pos) and not clicked:
                clicked = True  # Set clicked to be True, incase of clicking too many times
                bgm_2()  # Play bgm 2
                run_board()  # Calls Run board, switches to game page
                # Checks if game is over, and exit out
                result = chess_game.check_game_over()
                if result == False:
                    print("Game over!")  # Prints out game over message
                    pygame.quit()
                    sys.exit()
                    running = False  # Set running to be false
                clicked = False

    pygame.display.update()

pygame.quit()
sys.exit()
