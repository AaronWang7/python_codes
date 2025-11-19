# Chess Board
import pygame
from abc import ABC, abstractmethod

pygame.init()


run = True
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Chess Board")
# back_ground = pygame.image.load("chess_resourses\\board.png")
# background = pygame.transform.scale(back_ground, (800, 600))


class ChessPiece(ABC):
    def __init__(self, color, type, x, y, image, position):
        self.color = color
        self.type = type
        self.x = x
        self.y = y
        self.image = image
        self.white_pieces = []
        self.black_pieces = []
        self.position = position

    def can_move(self, new_pos):
        pass

    def get_position(self):
        return self.position

    # Change the position
    def set_position(self, new_pos):
        self.position = new_pos


class WhitePawn(ChessPiece):

    def __init__(self, white_pawn, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_pawn = pygame.image.load("chess_resourses\\pawn.png")
        self.whitep_transfrom = pygame.transform.scale(
            self.white_pawn, (100, 75))

    def pawn1_set(self):
        screen.blit(self.whitep_transfrom, (self.x, self.y))


class BlackPawn(ChessPiece):

    def __init__(self, black_pawn, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_pawn = pygame.image.load("chess_resourses\\pawn1.png")
        self.blackp_transfrom = pygame.transform.scale(
            self.black_pawn, (100, 75))

    def pawn2_set(self):
        screen.blit(self.blackp_transfrom, (self.x, self.y))


class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")
        self.board_transfrom = pygame.transform.scale(self.board, (800, 600))
        self.x = x
        self.y = y

    def board_set(self):
        screen.blit(self.board_transfrom, (self.x, self.y))


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


# pawn = Pawn(0, "White", 300, 300)
def run_board():
    while run:
        board.board_set()
        for white_p in white_pawns:
            white_p.pawn1_set()
        for black_p in black_pawns:
            black_p.pawn2_set()
        pygame.display.flip()
