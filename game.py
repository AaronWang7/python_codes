import pygame
import time
from board import *
from sounds import *
from animation import *
from ai import *

def run_board():
    from main import screen
    
    game = ChessGame()
    animation = Animation()
    ai_player = SimpleAI("Black")
    
    clock = pygame.time.Clock()
    selected_piece = None
    game_over = False
    winner = None
    
    bgm_2()
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return
            
            if not game_over and game.current_turn == "White":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    position = coords_to_pos(x, y)
                    
                    if position:
                        clicked_piece = game.get_piece_at(position)
                        
                        if selected_piece:
                            if clicked_piece and clicked_piece.color == "White":
                                selected_piece = clicked_piece
                            else:
                                if game.move_piece(selected_piece, position):
                                    selected_piece = None
                                    
                                    if game.is_checkmate():
                                        game_over = True
                                        winner = "White"
                                        animation.show_checkmate(screen)
                                        animation.show_win(winner, screen)
                        else:
                            if clicked_piece and clicked_piece.color == "White":
                                selected_piece = clicked_piece
        
        screen.fill((0, 0, 0))
        
        board_img = pygame.image.load("chess_resourses/board.png").convert()
        board_img = pygame.transform.scale(board_img, (800, 600))
        screen.blit(board_img, (0, 0))
        
        game.draw_all_pieces(screen)
        
        if selected_piece:
            pygame.draw.rect(screen, (255, 255, 0), 
                           (selected_piece.x, selected_piece.y, 100, 75), 3)
        
        if not game_over and game.current_turn == "Black":
            ai_player.draw_ai_thinking(screen)
            pygame.display.update()
            pygame.time.delay(500)
            
            if ai_player.make_move(game):
                if game.is_checkmate():
                    game_over = True
                    winner = "Black"
                    animation.show_checkmate(screen)
                    animation.show_win(winner, screen)
        
        if game_over:
            font = pygame.font.Font('freesansbold.ttf', 36)
            text = font.render("Game Over! Press ESC to exit", True, (255, 255, 255))
            screen.blit(text, (200, 500))
        
        pygame.display.update()
        clock.tick(60)
