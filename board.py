import pygame
from abc import ABC, abstractmethod


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


class WhitePawn:
    def __init__(self, white_pawn, x, y):
        self.x = x
        self.y = y
        self.white_pawn = pygame.image.load("chess_resourses\\pawn.png")
        self.whitep_transfrom = pygame.transform.scale(
            self.white_pawn, (100, 75))

    def pawn1_set(self, screen):
        screen.blit(self.whitep_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        # Get current and new ranks
        current_rank = int(self.position[1])
        new_rank = int(new_pos[1])

        can_move = new_pos[0] == self.position[0] and new_rank == current_rank + 1

        return can_move


class BlackPawn:
    def __init__(self, black_pawn, x, y):
        self.x = x
        self.y = y
        self.black_pawn = pygame.image.load("chess_resourses\\pawn1.png")
        self.blackp_transfrom = pygame.transform.scale(
            self.black_pawn, (100, 75))

    def pawn2_set(self, screen):
        screen.blit(self.blackp_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        # Get current and new ranks
        current_rank = int(self.position[1])
        new_rank = int(new_pos[1])
        can_move = new_pos[0] == self.position[0] and new_rank == current_rank - 1

        return can_move


class WhiteBishop:
    def __init__(self, white_bishop, x, y):
        self.x = x
        self.y = y
        self.white_bishop = pygame.image.load("chess_resourses\\bishop.png")
        self.whiteb_transfrom = pygame.transform.scale(
            self.white_bishop, (100, 75))

    def bishop1_set(self, screen):
        screen.blit(self.whiteb_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return file_diff == rank_diff


class BlackBishop:
    def __init__(self, black_bishop, x, y):
        self.x = x
        self.y = y
        self.black_bishop = pygame.image.load("chess_resourses\\bishop1.png")
        self.blackb_transfrom = pygame.transform.scale(
            self.black_bishop, (100, 75))

    def bishop2_set(self, screen):
        screen.blit(self.blackb_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return file_diff == rank_diff


class WhiteRook:
    def __init__(self, white_rook, x, y):
        self.x = x
        self.y = y
        self.white_rook = pygame.image.load("chess_resourses\\rook.png")
        self.whiter_transfrom = pygame.transform.scale(
            self.white_rook, (100, 75))

    def rook1_set(self, screen):
        screen.blit(self.whiter_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1])


class BlackRook:
    def __init__(self, black_rook, x, y):
        self.x = x
        self.y = y
        self.black_rook = pygame.image.load("chess_resourses\\rook1.png")
        self.blackr_transfrom = pygame.transform.scale(
            self.black_rook, (100, 75))

    def rook2_set(self, screen):
        screen.blit(self.blackr_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1])


class WhiteKnight:
    def __init__(self, white_knight, x, y):
        self.x = x
        self.y = y
        self.white_knight = pygame.image.load("chess_resourses\\knight.png")
        self.whitekn_transfrom = pygame.transform.scale(
            self.white_knight, (100, 75))

    def knight1_set(self, screen):
        screen.blit(self.whitekn_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (file_diff, rank_diff) in [(1, 2), (2, 1)]


class BlackKnight:
    def __init__(self, black_knight, x, y):
        self.x = x
        self.y = y
        self.black_knight = pygame.image.load("chess_resourses\\knight1.png")
        self.blackkn_transfrom = pygame.transform.scale(
            self.black_knight, (100, 75))

    def knight2_set(self, screen):
        screen.blit(self.blackkn_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (file_diff, rank_diff) in [(1, 2), (2, 1)]


class WhiteKing:
    def __init__(self, white_king, x, y):
        self.x = x
        self.y = y
        self.white_king = pygame.image.load("chess_resourses\\king.png")
        self.whitek_transfrom = pygame.transform.scale(
            self.white_king, (100, 75))

    def king1_set(self, screen):
        screen.blit(self.whitek_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return max(file_diff, rank_diff) == 1


class BlackKing:
    def __init__(self, black_king, x, y):
        self.x = x
        self.y = y
        self.black_king = pygame.image.load("chess_resourses\\king1.png")
        self.blackk_transfrom = pygame.transform.scale(
            self.black_king, (100, 75))

    def king2_set(self, screen):
        screen.blit(self.blackk_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return max(file_diff, rank_diff) == 1


class WhiteQueen:
    def __init__(self, white_queen, x, y):
        self.x = x
        self.y = y
        self.white_queen = pygame.image.load("chess_resourses\\queen.png")
        self.whiteq_transfrom = pygame.transform.scale(
            self.white_queen, (100, 75))

    def queen1_set(self, screen):
        screen.blit(self.whiteq_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1] or
                file_diff == rank_diff)


class BlackQueen:
    def __init__(self, black_queen, x, y):
        self.x = x
        self.y = y
        self.black_queen = pygame.image.load("chess_resourses\\queen1.png")
        self.blackq_transfrom = pygame.transform.scale(
            self.black_queen, (100, 75))

    def queen2_set(self, screen):
        screen.blit(self.blackq_transfrom, (self.x, self.y))

    def can_move_to(self, new_pos):
        file_diff = abs(ord(new_pos[0]) - ord(self.position[0]))
        rank_diff = abs(int(new_pos[1]) - int(self.position[1]))
        return (self.position[0] == new_pos[0] or
                self.position[1] == new_pos[1] or
                file_diff == rank_diff)


class Board:
    def __init__(self, board, x, y):
        self.board = pygame.image.load("chess_resourses\\board.png")
        self.board_transfrom = pygame.transform.scale(self.board, (800, 600))
        self.x = x
        self.y = y
        self.board_x = self.x
        self.board_y = self.y

    def board_set(self, screen):
        screen.blit(self.board_transfrom, (self.x, self.y))

    def board_get(self):
        x = self.board_x
        y = self.board_y

        if y <= 75:
            if x <= 100:
                return "A8"
            elif x <= 200:
                return "B8"
            elif x <= 300:
                return "C8"
            elif x <= 400:
                return "D8"
            elif x <= 500:
                return "E8"
            elif x <= 600:
                return "F8"
            elif x <= 700:
                return "G8"
            elif x <= 800:
                return "H8"
        elif y <= 150:
            if x <= 100:
                return "A7"
            elif x <= 200:
                return "B7"
            elif x <= 300:
                return "C7"
            elif x <= 400:
                return "D7"
            elif x <= 500:
                return "E7"
            elif x <= 600:
                return "F7"
            elif x <= 700:
                return "G7"
            elif x <= 800:
                return "H7"
        elif y <= 225:
            if x <= 100:
                return "A6"
            elif x <= 200:
                return "B6"
            elif x <= 300:
                return "C6"
            elif x <= 400:
                return "D6"
            elif x <= 500:
                return "E6"
            elif x <= 600:
                return "F6"
            elif x <= 700:
                return "G6"
            elif x <= 800:
                return "H6"
        elif y <= 300:
            if x <= 100:
                return "A5"
            elif x <= 200:
                return "B5"
            elif x <= 300:
                return "C5"
            elif x <= 400:
                return "D5"
            elif x <= 500:
                return "E5"
            elif x <= 600:
                return "F5"
            elif x <= 700:
                return "G5"
            elif x <= 800:
                return "H5"
        elif y <= 375:
            if x <= 100:
                return "A4"
            elif x <= 200:
                return "B4"
            elif x <= 300:
                return "C4"
            elif x <= 400:
                return "D4"
            elif x <= 500:
                return "E4"
            elif x <= 600:
                return "F4"
            elif x <= 700:
                return "G4"
            elif x <= 800:
                return "H4"
        elif y <= 450:
            if x <= 100:
                return "A3"
            elif x <= 200:
                return "B3"
            elif x <= 300:
                return "C3"
            elif x <= 400:
                return "D3"
            elif x <= 500:
                return "E3"
            elif x <= 600:
                return "F3"
            elif x <= 700:
                return "G3"
            elif x <= 800:
                return "H3"
        elif y <= 525:
            if x <= 100:
                return "A2"
            elif x <= 200:
                return "B2"
            elif x <= 300:
                return "C2"
            elif x <= 400:
                return "D2"
            elif x <= 500:
                return "E2"
            elif x <= 600:
                return "F2"
            elif x <= 700:
                return "G2"
            elif x <= 800:
                return "H2"
        elif y <= 600:
            if x <= 100:
                return "A1"
            elif x <= 200:
                return "B1"
            elif x <= 300:
                return "C1"
            elif x <= 400:
                return "D1"
            elif x <= 500:
                return "E1"
            elif x <= 600:
                return "F1"
            elif x <= 700:
                return "G1"
            elif x <= 800:
                return "H1"

        return None


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
        try:
            # Get piece at a specific position
            for piece in self.white_pieces + self.black_pieces:
                if piece.get_position() == position:
                    return piece
        except AttributeError:
            print("Error")

        return None

    def get_piece_info(self, piece):
        # Get formatted string with piece information
        if not piece:
            return "No piece"
        pieces = self.white_pieces if piece.color == "White" else self.black_pieces
        same_type = [p for p in pieces if type(p) == type(piece)]
        piece_num = same_type.index(piece) + 1

        return f"{piece.color} {type(piece).__name__} {piece_num}, Symbol {piece.get_symbol()} is at {piece.get_position()}"
