# Game Play
import time
from board import *
from sounds import *
chess_pawns = []

for i in range(8):
    chess_pawns.append(Pawn(i*100, 0))

chess_knights = []
j = 200
for i in range(1, 2):
    print(((i*(j)), 0))
    # chess_knights.append(Knight((i*(1*j)), 0))
    j = 350
    print(((i*(j)), 0))

chess_rooks = []
for i in range(2):
    chess_rooks.append(Rook(i*100, 0))

chess_queens = []
for i in range(2):
    chess_queens.append(Queen(i*100, 0))

chess_kings = []
for i in range(2):
    chess_kings.append(King(i*100), 0)

chess_bishops = []
for i in range(2):
    chess_bishops.append(Bishop(i*100), 0)


def run_board():
    bgm_2()
    run = True
    while run:
        for chess_pawn in chess_pawns:
            Pawn.draw(0)
        for chess_knights in chess_knights:
            Knight.draw(0)
        for chess_rook in chess_rook:
            Rook.draw(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
        pygame.display.flip()
