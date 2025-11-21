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


white_rooks = []
rook_x = 0
for i in range(2):
    xx = (rook_x)
    rook_x = rook_x + 700
    yy = 0
    white_rooks.append(WhiteRook(0, xx, yy))
    white_b = WhiteRook(0, xx, yy)

black_rooks = []
rook_x = 0
for i in range(2):
    xx = (rook_x)
    rook_x = rook_x + 700
    yy = 525
    black_rooks.append(BlackRook(0, xx, yy))
    black_b = BlackRook(0, xx, yy)

white_knights = []
knight_x = 100
for i in range(2):
    xx = (knight_x)
    knight_x = knight_x + 500
    yy = 0
    white_knights.append(WhiteKnight(0, xx, yy))
    white_kn = WhiteKnight(0, xx, yy)

black_knights = []
knight_x = 100
for i in range(2):
    xx = (knight_x)
    knight_x = knight_x + 500
    yy = 525
    black_knights.append(BlackKnight(0, xx, yy))
    black_kn = BlackKnight(0, xx, yy)
# pawn = Pawn(0, "White", 300, 300)

white_kings = []
king_x = 300
for i in range(1):
    xx = (king_x)
    yy = 0
    white_kings.append(WhiteKing(0, xx, yy))
    white_k = WhiteKing(0, xx, yy)

black_kings = []
king_x = 300
for i in range(1):
    xx = (king_x)
    yy = 525
    black_kings.append(BlackKing(0, xx, yy))
    black_k = BlackKing(0, xx, yy)


white_queens = []
queen_x = 400
for i in range(1):
    xx = (queen_x)
    yy = 0
    white_queens.append(WhiteQueen(0, xx, yy))
    white_q = WhiteQueen(0, xx, yy)

black_queens = []
queen_x = 400
for i in range(1):
    xx = (queen_x)
    yy = 525
    black_queens.append(BlackQueen(0, xx, yy))
    black_q = BlackQueen(0, xx, yy)


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
        for white_r in white_rooks:
            white_r.rook1_set()
        for black_r in black_rooks:
            black_r.rook2_set()
        for white_kn in white_knights:
            white_kn.knight1_set()
        for black_kn in black_knights:
            black_kn.knight2_set()
        for white_k in white_kings:
            white_k.king1_set()
        for black_k in black_kings:
            black_k.king2_set()
        for white_q in white_queens:
            white_q.queen1_set()
        for black_q in black_queens:
            black_q.queen2_set()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip()
