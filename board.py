# board.py
import pygame
from abc import ABC, abstractmethod
from enum import Enum

pygame.init()

# Piece color in Enum form


class PieceColor(Enum):
    WHITE = 1
    BLACK = 2

# Piece type in Enum form


class PieceType(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"

# Parent class


class ChessPiece(ABC):
    def __init__(self, color: PieceColor, piece_type: PieceType, position: str):
        self.color = color
        self.type = piece_type
        self.position = position
        self.image = None
        self.x = 0
        self.y = 0
        self.size = (75, 75)

    def load_image(self, image_path):
        image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(image, self.size)
        return self.image

    def update_screen_position(self, board_x, board_y):
        if len(self.position) == 2:
            file = self.position[0].upper()  # A-H
            rank = int(self.position[1])  # 1-8

            col = ord(file) - ord('A')

            row = 8 - rank

            square_size = 75
            self.x = board_x + col * square_size
            self.y = board_y + row * square_size

    def draw(self, screen):
        if self.image and self.x and self.y:
            screen.blit(self.image, (self.x, self.y))

    @abstractmethod
    def can_move_to(self, new_position, board_state):
        pass

    def move_to(self, new_position):
        self.position = new_position

# Child class (pawn)


class Pawn(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.PAWN, position)
        image_name = "pawn.png" if color == PieceColor.WHITE else "pawn1.png"
        self.load_image(f"chess_resourses\\{image_name}")

    def can_move_to(self, new_position, board_state):
        current_file = self.position[0]
        current_rank = int(self.position[1])
        new_file = new_position[0]
        new_rank = int(new_position[1])

        direction = 1 if self.color == PieceColor.WHITE else -1

        if current_file == new_file:
            if new_rank - current_rank == direction:
                return True
            if ((self.color == PieceColor.WHITE and current_rank == 2) or
                    (self.color == PieceColor.BLACK and current_rank == 7)):
                if new_rank - current_rank == 2 * direction:
                    return True
        return False

# Child class (Rook)


class Rook(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.ROOK, position)
        image_name = "rook.png" if color == PieceColor.WHITE else "rook1.png"
        self.load_image(f"chess_resourses/{image_name}")

    def can_move_to(self, new_position, board_state):
        return (self.position[0] == new_position[0] or
                self.position[1] == new_position[1])

# Child class (Knight)


class Knight(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.KNIGHT, position)
        image_name = "knight.png" if color == PieceColor.WHITE else "knight1.png"
        self.load_image(f"chess_resourses/{image_name}")

    def can_move_to(self, new_position, board_state):
        current_file = ord(self.position[0])
        current_rank = int(self.position[1])
        new_file = ord(new_position[0])
        new_rank = int(new_position[1])

        dx = abs(current_file - new_file)
        dy = abs(current_rank - new_rank)

        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

# Child class (Bishop)


class Bishop(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.KNIGHT, position)
        image_name = "bishop.png" if color == PieceColor.WHITE else "bishop1.png"
        self.load_image(f"chess_resourses\\{image_name}")

    def can_move_to(self, new_position, board_state):
        pass

# Child class (Queen)


class Queen(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.KNIGHT, position)
        image_name = "queen.png" if color == PieceColor.WHITE else "queen1.png"
        self.load_image(f"chess_resourses\\{image_name}")

    def can_move_to(self, new_position, board_state):
        pass

# Child class (King)


class King(ChessPiece):
    def __init__(self, color: PieceColor, position: str):
        super().__init__(color, PieceType.KNIGHT, position)
        image_name = "king.png" if color == PieceColor.WHITE else "king1.png"
        self.load_image(f"chess_resourses\\{image_name}")

    def can_move_to(self, new_position, board_state):
        pass

# Game setup


class ChessGame:
    def __init__(self, board_x=0, board_y=0):
        self.board_x = board_x
        self.board_y = board_y
        self.square_size = 75
        self.pieces = []
        self.selected_piece = None
        self.current_turn = PieceColor.WHITE
        self.setup_board()

    def setup_board(self):

        self.pieces.append(Rook(PieceColor.WHITE, "A1"))
        self.pieces.append(Knight(PieceColor.WHITE, "B1"))
        self.pieces.append(Rook(PieceColor.WHITE, "H1"))

        for file in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.pieces.append(Pawn(PieceColor.WHITE, f"{file}2"))

        self.pieces.append(Rook(PieceColor.BLACK, "A8"))
        self.pieces.append(Knight(PieceColor.BLACK, "B8"))
        self.pieces.append(Rook(PieceColor.BLACK, "H8"))

        for file in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.pieces.append(Pawn(PieceColor.BLACK, f"{file}7"))

        self.update_piece_positions()

    def update_piece_positions(self):
        for piece in self.pieces:
            piece.update_screen_position(self.board_x, self.board_y)

    def get_piece_at(self, position):
        for piece in self.pieces:
            if piece.position == position:
                return piece
        return None

    def get_piece_at_screen(self, screen_x, screen_y):
        for piece in self.pieces:
            if (piece.x <= screen_x <= piece.x + piece.size[0] and
                    piece.y <= screen_y <= piece.y + piece.size[1]):
                return piece
        return None

    def handle_click(self, screen_x, screen_y):
        clicked_piece = self.get_piece_at_screen(screen_x, screen_y)

        if self.selected_piece is None:
            if clicked_piece and clicked_piece.color == self.current_turn:
                self.selected_piece = clicked_piece
                print(
                    f"Selected {clicked_piece.color.name} {clicked_piece.type.value}")
        else:

            board_pos = self.screen_to_board(screen_x, screen_y)
            if board_pos:
                if self.selected_piece.can_move_to(board_pos, self.pieces):
                    self.selected_piece.move_to(board_pos)
                    self.selected_piece = None
                    self.current_turn = (PieceColor.BLACK if self.current_turn == PieceColor.WHITE
                                         else PieceColor.WHITE)
                    self.update_piece_positions()
                else:
                    self.selected_piece = None

    def screen_to_board(self, screen_x, screen_y):
        if (self.board_x <= screen_x <= self.board_x + 8 * self.square_size and
                self.board_y <= screen_y <= self.board_y + 8 * self.square_size):

            col = (screen_x - self.board_x) // self.square_size
            row = (screen_y - self.board_y) // self.square_size

            file_char = chr(ord('A') + col)
            rank = 8 - row

            return f"{file_char}{rank}"
        return None

    def draw(self, screen):

        for piece in self.pieces:
            piece.draw(screen)
