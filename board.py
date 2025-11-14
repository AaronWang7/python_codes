import pygame

pygame.init()


run = True
x = 800
y = 600
screen = pygame.display.set_mode((x, y))


class ChessPiece:
    def __init__(self, color, type, x, y, image, position):
        self.color = color
        self.type = type
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
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


class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")

    def board_set(self):
        screen.blit(self.board, (300, 500))


while run:
    Board.board_set()

    pygame.display.update()
