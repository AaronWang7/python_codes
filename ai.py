import random
import pygame

class SimpleAI:
    def __init__(self, color):
        self.color = color
        self.move_count = 0
    
    def get_random_move(self, game):
        pieces = game.black_pieces if self.color == "Black" else game.white_pieces
        
        if not pieces:
            return None, None
        
        valid_moves = []
        
        for piece in pieces:
            current_pos = piece.get_position()
            current_col = current_pos[0]
            current_row = int(current_pos[1])
            
            possible_moves = []
            
            if isinstance(piece, (BlackPawn, WhitePawn)):
                dir = -1 if self.color == "Black" else 1
                new_row = current_row + dir
                if 1 <= new_row <= 8:
                    new_pos = current_col + str(new_row)
                    if not game.get_piece_at(new_pos):
                        possible_moves.append(new_pos)
                
                attack_cols = [chr(ord(current_col) - 1), chr(ord(current_col) + 1)]
                for col in attack_cols:
                    if 'A' <= col <= 'H':
                        new_pos = col + str(new_row)
                        target = game.get_piece_at(new_pos)
                        if target and target.color != self.color:
                            possible_moves.append(new_pos)
            
            elif isinstance(piece, (BlackKnight, WhiteKnight)):
                moves = [(1, 2), (2, 1), (-1, 2), (2, -1), 
                        (1, -2), (-2, 1), (-1, -2), (-2, -1)]
                for dc, dr in moves:
                    new_col = chr(ord(current_col) + dc)
                    new_row = current_row + dr
                    if 'A' <= new_col <= 'H' and 1 <= new_row <= 8:
                        new_pos = new_col + str(new_row)
                        target = game.get_piece_at(new_pos)
                        if not target or target.color != self.color:
                            possible_moves.append(new_pos)
            
            elif isinstance(piece, (BlackKing, WhiteKing)):
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
            
            for move in possible_moves:
                valid_moves.append((piece, move))
        
        if valid_moves:
            return random.choice(valid_moves)
        return None, None
    
    def make_move(self, game):
        piece, new_pos = self.get_random_move(game)
        if piece and new_pos:
            if game.move_piece(piece, new_pos):
                self.move_count += 1
                return True
        return False
    
    def draw_ai_thinking(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 24)
        text = font.render("AI is thinking...", True, (255, 255, 255))
        screen.blit(text, (600, 50))
        pygame.display.update()
