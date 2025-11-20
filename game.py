# Game Play
from board import *
from sounds import *
board = Board(0, x=0, y=0)
# White Pawns
white_pawns = []
pawn_x = 0
for i in range(8):
    xx = (pawn_x)
    pawn_x = pawn_x + 100
    yy = 70
    white_pawns.append(WhitePawn(0, xx, yy))
    white_p = WhitePawn(0, xx, yy)
    print(xx, yy)
# Black Pawns
black_pawns = []
pawn_x = 0
for i in range(8):
    xx = (pawn_x)
    pawn_x = pawn_x + 100
    yy = 445
    black_pawns.append(BlackPawn(0, xx, yy))
    black_p = BlackPawn(0, xx, yy)
    print(xx, yy)

white_bishops = []
bishop_x = 200
for i in range(2):
    xx = (bishop_x)
    bishop_x = bishop_x + 300
    yy = 0
    white_bishops.append(WhiteBishop(0, xx, yy))
    white_b = WhiteBishop(0, xx, yy)


black_bishops = []
bishop1_x = 200
for i in range(2):
    xx = (bishop1_x)
    bishop1_x = bishop1_x + 300
    yy = 525
    black_bishops.append(BlackBishop(0, xx, yy))
    black_b = BlackBishop(0, xx, yy)


# pawn = Pawn(0, "White", 300, 300)


def run_board():
    bgm_2()
    run = True
    while run:
        board.board_set()
        for white_p in white_pawns:
            white_p.pawn1_set()
        for black_p in black_pawns:
            black_p.pawn2_set()
        for white_b in white_bishops:
            white_b.bishop1_set()
        for black_b in black_bishops:
            black_b.bishop2_set()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
