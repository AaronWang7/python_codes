# Chess Board
import pygame

pygame.init()


run = True
x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Chess Board")
back_ground = pygame.image.load("chess_resourses\\board.png")
background = pygame.transform.scale(back_ground, (800, 600))


class ChessPiece:
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


class Pawn(ChessPiece):
    def __init__(self):
        pass

    def get_image(self):
        if self.color == "White":
            self.image = pygame.image.load("chess_resourses\\pawn.png")
        else:
            self.image = pygame.image.load("chess_resourses\\pawn1.png")

    def pawn_set(self):
        screen.blit(self.image, (300, 300))


class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")
        self.x = x
        self.y = y

    def board_set(self):
        screen.blit(background, (0, 0))


while run:
    Board.board_set(background)
    Pawn.pawn_set()

    pygame.display.flip()
