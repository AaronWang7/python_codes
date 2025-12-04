# Game Play
import time
from board import *
from sounds import *

chess_pawns = []
for i in range(8):
    chess_pawns.append(Pawn(i*100, 0))

chess_knights = []
for i in range(8):
    chess_knights.append(Pawn(i*100, 0))


def run_board():
    bgm_2()
    run = True
    while run:
        for chess_piece in chess_pawns:
            chess_piece.draw(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
        pygame.display.flip()
