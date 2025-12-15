import random
import pygame


class SimpleAI:
    def __init__(self, color):
        self.color = color

    def make_move(self, game):
        pieces = game.black_pieces if self.color == "Black" else game.white_pieces

        if not pieces:
            return False

        random.shuffle(pieces)

        for piece in pieces:
            current_pos = piece.get_position()
            current_col = current_pos[0]
            current_row = int(current_pos[1])

            possible_moves = []

            piece_type = piece.__class__.__name__

            if "Pawn" in piece_type:
                direction = -1 if self.color == "Black" else 1
                new_row = current_row + direction

                if 1 <= new_row <= 8:
                    forward_pos = current_col + str(new_row)
                    if not game.get_piece_at(forward_pos):
                        possible_moves.append(forward_pos)

                    for col_offset in [-1, 1]:
                        attack_col = chr(ord(current_col) + col_offset)
                        if 'A' <= attack_col <= 'H':
                            attack_pos = attack_col + str(new_row)
                            target = game.get_piece_at(attack_pos)
                            if target and target.color != self.color:
                                possible_moves.append(attack_pos)

            elif "Knight" in piece_type:
                knight_moves = [(1, 2), (2, 1), (-1, 2), (2, -1),
                                (1, -2), (-2, 1), (-1, -2), (-2, -1)]
                for dc, dr in knight_moves:
                    new_col = chr(ord(current_col) + dc)
                    new_row = current_row + dr
                    if 'A' <= new_col <= 'H' and 1 <= new_row <= 8:
                        new_pos = new_col + str(new_row)
                        target = game.get_piece_at(new_pos)
                        if not target or target.color != self.color:
                            possible_moves.append(new_pos)

            else:
                for dc in [-1, 0, 1]:
                    for dr in [-1, 0, 1]:
                        if dc == 0 and dr == 0:
                            continue
                        new_col = chr(ord(current_col) + dc)
                        new_row = current_row + dr
                        if 'A' <= new_col <= 'H' and 1 <= new_row <= 8:
                            new_pos = new_col + str(new_row)
                            target = game.get_piece_at(new_pos)
                            if not target or target.color != self.color:
                                possible_moves.append(new_pos)

            if possible_moves:
                new_pos = random.choice(possible_moves)
                if game.move_piece(piece, new_pos):
                    return True

        return False

    def draw_ai_thinking(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render("AI...", True, (255, 255, 255))
        screen.blit(text, (600, 50))
