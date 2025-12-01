# Chess Board
import pygame
from abc import ABC, abstractmethod

pygame.init()


x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Chess Board")


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

    def can_move_to(self, new_pos):
        pass

    def get_symbol(self):
        pass

    def get_position(self):
        return self.position

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

    def can_move(self, new_pos=[]):
        pass


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


class WhiteBishop(ChessPiece):

    def __init__(self, white_bishop, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_bishop = pygame.image.load("chess_resourses\\bishop.png")
        self.whiteb_transfrom = pygame.transform.scale(
            self.white_bishop, (100, 75))

    def bishop1_set(self):
        screen.blit(self.whiteb_transfrom, (self.x, self.y))


class BlackBishop(ChessPiece):

    def __init__(self, black_bishop, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_bishop = pygame.image.load("chess_resourses\\bishop1.png")
        self.blackb_transfrom = pygame.transform.scale(
            self.black_bishop, (100, 75))

    def bishop2_set(self):
        screen.blit(self.blackb_transfrom, (self.x, self.y))


class WhiteRook(ChessPiece):

    def __init__(self, white_rook, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_rook = pygame.image.load("chess_resourses\\rook.png")
        self.whiter_transfrom = pygame.transform.scale(
            self.white_rook, (100, 75))

    def rook1_set(self):
        screen.blit(self.whiter_transfrom, (self.x, self.y))


class BlackRook(ChessPiece):

    def __init__(self, black_rook, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_rook = pygame.image.load("chess_resourses\\rook1.png")
        self.blackr_transfrom = pygame.transform.scale(
            self.black_rook, (100, 75))

    def rook2_set(self):
        screen.blit(self.blackr_transfrom, (self.x, self.y))


class WhiteKnight(ChessPiece):

    def __init__(self, white_knight, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_knight = pygame.image.load("chess_resourses\\knight.png")
        self.whitekn_transfrom = pygame.transform.scale(
            self.white_knight, (100, 75))

    def knight1_set(self):
        screen.blit(self.whitekn_transfrom, (self.x, self.y))


class BlackKnight(ChessPiece):

    def __init__(self, black_knight, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_knight = pygame.image.load("chess_resourses\\knight1.png")
        self.blackkn_transfrom = pygame.transform.scale(
            self.black_knight, (100, 75))

    def knight2_set(self):
        screen.blit(self.blackkn_transfrom, (self.x, self.y))


class WhiteKing(ChessPiece):

    def __init__(self, white_king, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_king = pygame.image.load("chess_resourses\\king.png")
        self.whitek_transfrom = pygame.transform.scale(
            self.white_king, (100, 75))

    def king1_set(self):
        screen.blit(self.whitek_transfrom, (self.x, self.y))


class BlackKing(ChessPiece):

    def __init__(self, black_king, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_king = pygame.image.load("chess_resourses\\king1.png")
        self.blackk_transfrom = pygame.transform.scale(
            self.black_king, (100, 75))

    def king2_set(self):
        screen.blit(self.blackk_transfrom, (self.x, self.y))


class WhiteQueen(ChessPiece):

    def __init__(self, white_queen, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.white_queen = pygame.image.load("chess_resourses\\queen.png")
        self.whiteq_transfrom = pygame.transform.scale(
            self.white_queen, (100, 75))

    def queen1_set(self):
        screen.blit(self.whiteq_transfrom, (self.x, self.y))


class BlackQueen(ChessPiece):

    def __init__(self, black_queen, x, y):
        # self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.black_queen = pygame.image.load("chess_resourses\\queen1.png")
        self.blackq_transfrom = pygame.transform.scale(
            self.black_queen, (100, 75))

    def queen2_set(self):
        screen.blit(self.blackq_transfrom, (self.x, self.y))


class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")
        self.board_transfrom = pygame.transform.scale(self.board, (800, 600))
        self.x = x
        self.y = y
        self.board_x = self.x
        self.board_y = self.y

    def board_set(self):
        screen.blit(self.board_transfrom, (self.x, self.y))

    def board_get(self):
        if self.board_x <= 100 and self.board_y <= 75:
            return "A8"
        elif self.board_x <= 200 and self.board_y <= 75:
            return "B8"
        elif self.board_x <= 300 and self.board_y <= 75:
            return "C8"
        elif self.board_x <= 400 and self.board_y <= 75:
            return "D8"
        elif self.board_x <= 500 and self.board_y <= 75:
            return "E8"
        elif self.board_x <= 600 and self.board_y <= 75:
            return "F8"
        elif self.board_x <= 700 and self.board_y <= 75:
            return "G8"
        elif self.board_x <= 800 and self.board_y <= 75:
            return "H8"


class ChessGame:
    def __init__(self):
        # Lists to store pieces
        self.white_pieces = []
        self.black_pieces = []
        # Setup the board
        self.setup_pieces()

    # Put all pieces in starting positions
    def setup_pieces(self):
        # Create white pieces
        self.white_pieces.append(WhiteRook("White", "A1"))
        self.white_pieces.append(WhiteKnight("White", "B1"))
        self.white_pieces.append(WhiteBishop("White", "C1"))
        self.white_pieces.append(WhiteQueen("White", "D1"))
        self.white_pieces.append(WhiteKing("White", "E1"))
        self.white_pieces.append(WhiteBishop("White", "F1"))
        self.white_pieces.append(WhiteKnight("White", "G1"))
        self.white_pieces.append(WhiteRook("White", "H1"))

        # Create white pawns
        self.white_pieces.append(WhitePawn("White", "A2"))
        self.white_pieces.append(WhitePawn("White", "B2"))
        self.white_pieces.append(WhitePawn("White", "C2"))
        self.white_pieces.append(WhitePawn("White", "D2"))
        self.white_pieces.append(WhitePawn("White", "E2"))
        self.white_pieces.append(WhitePawn("White", "F2"))
        self.white_pieces.append(WhitePawn("White", "G2"))
        self.white_pieces.append(WhitePawn("White", "H2"))

        # Create black pieces
        self.black_pieces.append(BlackRook("Black", "A8"))
        self.black_pieces.append(BlackKnight("Black", "B8"))
        self.black_pieces.append(BlackBishop("Black", "C8"))
        self.black_pieces.append(BlackQueen("Black", "D8"))
        self.black_pieces.append(BlackKing("Black", "E8"))
        self.black_pieces.append(BlackBishop("Black", "F8"))
        self.black_pieces.append(BlackKnight("Black", "G8"))
        self.black_pieces.append(BlackRook("Black", "H8"))

        # Create black pawns
        self.black_pieces.append(BlackPawn("Black", "A7"))
        self.black_pieces.append(BlackPawn("Black", "B7"))
        self.black_pieces.append(BlackPawn("Black", "C7"))
        self.black_pieces.append(BlackPawn("Black", "D7"))
        self.black_pieces.append(BlackPawn("Black", "E7"))
        self.black_pieces.append(BlackPawn("Black", "F7"))
        self.black_pieces.append(BlackPawn("Black", "G7"))
        self.black_pieces.append(BlackPawn("Black", "H7"))

    def get_piece_at(self, position):
        for piece in self.white_pieces + self.black_pieces:
            if piece.get_position() == position:
                return piece
        return None
