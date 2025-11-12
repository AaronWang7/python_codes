from abc import ABC, abstractmethod
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
    pass


class Pawn():
    def __init__(self, image):
        self.image = pygame.image.load("chess_resourses\\pawn.png")

    def get_image(self):
        if self.color == "White":
            image = pygame.image.load(
                "chess_resourses\\pawn.png").convert_alpha()
        else:
            image = pygame.image.load(
                "chess_resourses\\pawn1.png").convert_alpha()

    def can_move_to(self, new_pos):
        # Get current and new ranks
        current_rank = int(self.position[1])
        new_rank = int(new_pos[1])

        # Check if pawn moves forward
        if self.color == "White":
            # White pawns move up
            can_move = new_pos[0] == self.position[0] and new_rank == current_rank + 1
        else:
            # Black pawns move down
            can_move = new_pos[0] == self.position[0] and new_rank == current_rank - 1

        return can_move

    def pawn_set(self):
        screen.blit(self.image, (400, 300))

    # Return P for white pawns, p for black pawns


class Rook(ChessPiece):
    def get_image(self, image):
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

    # Import abc for abstract base class

# Parent class for all chess pieces


while run:
    Pawn.pawn_set()

    pygame.display.flip()


class ChessPiece(ABC):
    # Constructor
    def __init__(self, color, position):
        # Set the color (Black or White)
        self.color = color
        # Set starting position
        self.position = position

    # This function will check if a move is legal
    @abstractmethod
    def can_move_to(self, new_pos):
        pass

    # This function will return the piece symbol
    @abstractmethod
    def get_symbol(self):
        pass

    # Get the current position
    def get_position(self):
        return self.position

    # Change the position
    def set_position(self, new_pos):
        self.position = new_pos

# Pawn piece


class Pawn(ChessPiece):
    def can_move_to(self, new_pos):
        # Get current and new ranks
        current_rank = int(self.position[1])
        new_rank = int(new_pos[1])

        # Check if pawn moves forward
        if self.color == "White":
            # White pawns move up
            can_move = new_pos[0] == self.position[0] and new_rank == current_rank + 1
        else:
            # Black pawns move down
            can_move = new_pos[0] == self.position[0] and new_rank == current_rank - 1

        return can_move

    # Return P for white pawns, p for black pawns
    def get_symbol(self):
        if self.color == "White":
            return "P"
        else:
            return "p"


class Rook(ChessPiece):
    # Rook chess piece
    def can_move_to(self, new_pos):
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1])

    def get_symbol(self):
        return "R" if self.color == "White" else "r"


class Knight(ChessPiece):
    # Knight chess piece
    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (file_diff, rank_diff) in [(1, 2), (2, 1)]

    def get_symbol(self):
        return "N" if self.color == "White" else "n"


class Bishop(ChessPiece):
    # Bishop chess piece - moves diagonally
    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return file_diff == rank_diff

    def get_symbol(self):
        return "B" if self.color == "White" else "b"


class Queen(ChessPiece):
    # Queen chess piece
    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1] or
                file_diff == rank_diff)

    def get_symbol(self):
        return "Q" if self.color == "White" else "q"


class King(ChessPiece):
    # King chess piece - moves one square
    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return max(file_diff, rank_diff) == 1

    def get_symbol(self):
        return "K" if self.color == "White" else "k"

# Main game class


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
        self.white_pieces.append(Rook("White", "A1"))
        self.white_pieces.append(Knight("White", "B1"))
        self.white_pieces.append(Bishop("White", "C1"))
        self.white_pieces.append(Queen("White", "D1"))
        self.white_pieces.append(King("White", "E1"))
        self.white_pieces.append(Bishop("White", "F1"))
        self.white_pieces.append(Knight("White", "G1"))
        self.white_pieces.append(Rook("White", "H1"))

        # Create white pawns
        self.white_pieces.append(Pawn("White", "A2"))
        self.white_pieces.append(Pawn("White", "B2"))
        self.white_pieces.append(Pawn("White", "C2"))
        self.white_pieces.append(Pawn("White", "D2"))
        self.white_pieces.append(Pawn("White", "E2"))
        self.white_pieces.append(Pawn("White", "F2"))
        self.white_pieces.append(Pawn("White", "G2"))
        self.white_pieces.append(Pawn("White", "H2"))

        # Create black pieces
        self.black_pieces.append(Rook("Black", "A8"))
        self.black_pieces.append(Knight("Black", "B8"))
        self.black_pieces.append(Bishop("Black", "C8"))
        self.black_pieces.append(Queen("Black", "D8"))
        self.black_pieces.append(King("Black", "E8"))
        self.black_pieces.append(Bishop("Black", "F8"))
        self.black_pieces.append(Knight("Black", "G8"))
        self.black_pieces.append(Rook("Black", "H8"))

        # Create black pawns
        self.black_pieces.append(Pawn("Black", "A7"))
        self.black_pieces.append(Pawn("Black", "B7"))
        self.black_pieces.append(Pawn("Black", "C7"))
        self.black_pieces.append(Pawn("Black", "D7"))
        self.black_pieces.append(Pawn("Black", "E7"))
        self.black_pieces.append(Pawn("Black", "F7"))
        self.black_pieces.append(Pawn("Black", "G7"))
        self.black_pieces.append(Pawn("Black", "H7"))

    def move_piece(self, piece, new_pos):
        # Move a piece to a new position if the move is valid
        if piece and piece.can_move_to(new_pos):
            piece.set_position(new_pos)
            return True
        return False

    def remove_piece(self, piece):
        # Remove a piece from the game
        pieces = self.white_pieces if piece.color == "White" else self.black_pieces
        if piece in pieces:
            pieces.remove(piece)

    def get_pieces_left(self, color):
        # Get count of remaining pieces for a color
        pieces = self.white_pieces if color == "White" else self.black_pieces
        return len(pieces)

    def get_piece_at(self, position):
        # Get piece at a specific position
        for piece in self.white_pieces + self.black_pieces:
            if piece.get_position() == position:
                return piece
        return None

    def get_piece_info(self, piece):
        # Get formatted string with piece information
        if not piece:
            return "No piece"

        pieces = self.white_pieces if piece.color == "White" else self.black_pieces
        same_type = [p for p in pieces if type(p) == type(piece)]
        piece_num = same_type.index(piece) + 1

        return f"{piece.color} {type(piece).__name__} {piece_num}, Symbol {piece.get_symbol()} is at {piece.get_position()}"
