import pygame
from abc import ABC, abstractmethod  # abstractmethod

# Class - ChessPiece(uses ABC, - so child class can get it's...)


class ChessPiece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.x = 0
        self.y = 0
        self.update_coords()

    def update_coords(self):
        col = ord(self.position[0]) - ord('A')
        row = 8 - int(self.position[1])
        self.x = col * 100
        self.y = row * 75

    def set_position(self, new_pos):
        self.position = new_pos
        self.update_coords()

    def get_position(self):
        return self.position

    @abstractmethod
    def can_move_to(self, new_pos):
        pass

    @abstractmethod
    def draw(self, screen):
        pass

# WhitePawn Child class of ChessPiece


class WhitePawn(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/pawn.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        current_col = self.position[0]
        current_row = int(self.position[1])
        new_col = new_pos[0]
        new_row = int(new_pos[1])

        if current_col == new_col and new_row == current_row + 1:
            return True

        if current_row == 2 and current_col == new_col and new_row == 4:
            return True

        if abs(ord(new_col) - ord(current_col)) == 1 and new_row == current_row + 1:
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackPawn Child class of ChessPiece


class BlackPawn(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/pawn1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        current_col = self.position[0]
        current_row = int(self.position[1])
        new_col = new_pos[0]
        new_row = int(new_pos[1])

        if current_col == new_col and new_row == current_row - 1:
            return True

        if current_row == 7 and current_col == new_col and new_row == 5:
            return True

        if abs(ord(new_col) - ord(current_col)) == 1 and new_row == current_row - 1:
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# WhiteBishop Child class of ChessPiece


class WhiteBishop(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/bishop.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return col_diff == row_diff

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackBishop Child class of ChessPiece


class BlackBishop(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/bishop1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return col_diff == row_diff

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# WhiteRook Child class of ChessPiece


class WhiteRook(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/rook.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        return self.position[0] == new_pos[0] or self.position[1] == new_pos[1]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackRook Child class of ChessPiece


class BlackRook(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/rook1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        return self.position[0] == new_pos[0] or self.position[1] == new_pos[1]

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# WhiteKnight Child class of ChessPiece


class WhiteKnight(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/knight.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (col_diff == 1 and row_diff == 2) or (col_diff == 2 and row_diff == 1)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackKnight Child class of ChessPiece


class BlackKnight(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/knight1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (col_diff == 1 and row_diff == 2) or (col_diff == 2 and row_diff == 1)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# WhiteKing Child class of ChessPiece


class WhiteKing(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/king.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return col_diff <= 1 and row_diff <= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackKing Child class of ChessPiece


class BlackKing(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/king1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return col_diff <= 1 and row_diff <= 1

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# WhiteQueen Child class of ChessPiece


class WhiteQueen(ChessPiece):
    def __init__(self, position):
        super().__init__("White", position)
        self.image = pygame.image.load("chess_resourses/queen.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1] or
                col_diff == row_diff)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# BlackQueen Child class of ChessPiece


class BlackQueen(ChessPiece):
    def __init__(self, position):
        super().__init__("Black", position)
        self.image = pygame.image.load("chess_resourses/queen1.png")
        self.image = pygame.transform.scale(self.image, (100, 75))

    def can_move_to(self, new_pos):
        col_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        row_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1] or
                col_diff == row_diff)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))


class ChessGame:
    def __init__(self):
        self.white_pieces = []
        self.black_pieces = []
        self.current_turn = "White"
        self.selected_piece = None
        self.game_over = False
        self.winner = None
        self.setup_pieces()
    # Set up piece locations

    def setup_pieces(self):

        self.white_pieces = [
            WhiteRook("A1"), WhiteKnight(
                "B1"), WhiteBishop("C1"), WhiteQueen("D1"),
            WhiteKing("E1"), WhiteBishop(
                "F1"), WhiteKnight("G1"), WhiteRook("H1"),
            WhitePawn("A2"), WhitePawn("B2"), WhitePawn("C2"), WhitePawn("D2"),
            WhitePawn("E2"), WhitePawn("F2"), WhitePawn("G2"), WhitePawn("H2")
        ]

        self.black_pieces = [
            BlackRook("A8"), BlackKnight(
                "B8"), BlackBishop("C8"), BlackQueen("D8"),
            BlackKing("E8"), BlackBishop(
                "F8"), BlackKnight("G8"), BlackRook("H8"),
            BlackPawn("A7"), BlackPawn("B7"), BlackPawn("C7"), BlackPawn("D7"),
            BlackPawn("E7"), BlackPawn("F7"), BlackPawn("G7"), BlackPawn("H7")
        ]

    def get_piece_at(self, position):

        for piece in self.white_pieces + self.black_pieces:
            if piece.get_position() == position:
                return piece
        return None

    def move_piece(self, piece, new_position):

        target_piece = self.get_piece_at(new_position)

        if target_piece and target_piece.color == piece.color:
            return False

        if piece.can_move_to(new_position):

            if target_piece:
                self.remove_piece(target_piece)

            piece.set_position(new_position)

            self.current_turn = "Black" if self.current_turn == "White" else "White"

            self.check_game_over()

            return True
        return False

    def remove_piece(self, piece):
        if piece.color == "White":
            if piece in self.white_pieces:
                self.white_pieces.remove(piece)
        else:
            if piece in self.black_pieces:
                self.black_pieces.remove(piece)

    def draw_all_pieces(self, screen):

        for piece in self.white_pieces + self.black_pieces:
            piece.draw(screen)

    def check_game_over(self):

        white_king_exists = any(isinstance(piece, WhiteKing)
                                for piece in self.white_pieces)
        black_king_exists = any(isinstance(piece, BlackKing)
                                for piece in self.black_pieces)

        if not white_king_exists:
            self.game_over = True
            self.winner = "Black"
            return True

        if not black_king_exists:
            self.game_over = True
            self.winner = "White"
            return True

        if len(self.white_pieces) == 0:
            self.game_over = True
            self.winner = "Black"
            return True

        if len(self.black_pieces) == 0:
            self.game_over = True
            self.winner = "White"
            return True

        if not self.has_legal_moves():
            self.game_over = True
            self.winner = "Draw"
            return True

        return False

    def has_legal_moves(self):
        pieces = self.white_pieces if self.current_turn == "White" else self.black_pieces

        for piece in pieces:
            current_pos = piece.get_position()
            current_col = current_pos[0]
            current_row = int(current_pos[1])

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue

                    new_col = chr(ord(current_col) + dx)
                    new_row = current_row + dy

                    if 'A' <= new_col <= 'H' and 1 <= new_row <= 8:
                        new_pos = new_col + str(new_row)

                        if piece.can_move_to(new_pos):

                            target = self.get_piece_at(new_pos)
                            if not target or target.color != piece.color:
                                return True
        return False


def pos_to_coords(position):
    col = ord(position[0]) - ord('A')
    row = 8 - int(position[1])
    return col * 100, row * 75


def coords_to_pos(x, y):
    col = x // 100
    row = 8 - (y // 75)
    if 0 <= col < 8 and 1 <= row <= 8:
        return chr(ord('A') + col) + str(row)
    return None
