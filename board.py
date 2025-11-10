import pygame


class ChessPiece:
    def __init__(self, color, type, x, y, image):
        self.color = color
        self.type = type
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)


class Pawn(ChessPiece):
    def get_image(self):
        if self.color == "White":
            image = pygame.image.load(
                "chess_resourses\\pawn.png").convert_alpha()
        else:
            image = pygame.image.load(
                "chess_resourses\\pawn1.png").convert_alpha()


class Rook(ChessPiece):
    def get_image(self):
        if self.color == "White":
            image = pygame.image.load(
                "chess_resourses\\rook.png").convert_alpha()
        else:
            image = pygame.image.load(
                "chess_resourses\\rook1.png").convert_alpha()


class knight(ChessPiece):
    def get_image(self):
        if self.color == "White":
            image = pygame.image.load(
                "chess_resourses\\knight.png").convert_alpha()
        else:
            image = pygame.image.load(
                "chess_resourses\\knight1.png").convert_alpha()


class Bishop(ChessPiece):
    pass


class Queen(ChessPiece):
    pass


class King(ChessPiece):
    pass


class Board:
    def __init__(self):
        self.white_pieces = []
        self.black_pieces = []
        self.setup_pieces()

    def setup_pieces(self):
        pass

    def move_piece(self, piece, new_pos):
        pass

    def remove_piece(self, piece):
        pass

    def get_pieces_left(self, color):
        pass

    def get_piece_at(self, position):
        pass

    def get_piece_info(self, piece):
        pass
