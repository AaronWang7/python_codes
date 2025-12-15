import pygame
from board import *
from sounds import *
from animation import Animation

# Run Board function


def run_board():
    from main import screen

    game = ChessGame()

    try:
        from animation import Animation
        animation = Animation()
    except:

        class FakeAnimation:
            def show_checkmate(self, screen): pass
            def show_win(self, winner, screen): pass
        animation = FakeAnimation()

    try:
        from ai import SimpleAI
        ai_player = SimpleAI("Black")
    except:
        class FakeAI:
            def __init__(self, color): self.color = color
            def make_move(self, game): return False
            def draw_ai_thinking(self, screen): pass
        ai_player = FakeAI("Black")

    selected_piece = None
    run = True
    clock = pygame.time.Clock()

    bgm_2()  # Plays bgm 2

    while run:
        # Get event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                return
            # If enters the key "Esc" - Return s to main page
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    return
            # If game didn't end and it's White Piece's turn
            if not game.game_over and game.current_turn == "White":
                if event.type == pygame.MOUSEBUTTONDOWN:  # If clicked
                    x, y = event.pos  # Store it's location
                    col = x // 100  # column
                    row = y // 75  # row

                    if 0 <= col < 8 and 0 <= row < 8:
                        board_col = chr(ord('A') + col)
                        board_row = str(8 - row)
                        position = board_col + board_row

                        clicked_piece = game.get_piece_at(position)

                        if selected_piece:

                            if game.move_piece(selected_piece, position):
                                selected_piece = None

                                if game.check_game_over():
                                    if game.winner == "White":
                                        print("White wins!")
                                        animation.show_win("White", screen)
                                    elif game.winner == "Black":
                                        print("Black wins!")
                                        animation.show_win("Black", screen)
                                    elif game.winner == "Draw":
                                        print("Draw!")
                        else:
                            if clicked_piece and clicked_piece.color == "White":
                                selected_piece = clicked_piece

        screen.fill((0, 0, 0))
        board_img = pygame.image.load(
            "chess_resourses/board.png").convert()
        board_img = pygame.transform.scale(board_img, (800, 600))
        screen.blit(board_img, (0, 0))

        game.draw_all_pieces(screen)

        if selected_piece:
            pygame.draw.rect(screen, (255, 255, 0),
                             (selected_piece.x, selected_piece.y, 100, 75), 3)

        if not game.game_over and game.current_turn == "Black":
            ai_player.draw_ai_thinking(screen)
            pygame.display.update()
            pygame.time.delay(500)

            if ai_player.make_move(game):
                if game.check_game_over():
                    if game.winner == "White":
                        print("White wins!")
                        animation.show_win("White", screen)
                    elif game.winner == "Black":
                        print("Black wins!")
                        animation.show_win("Black", screen)
                    elif game.winner == "Draw":
                        print("It's a draw!")

        font = pygame.font.Font('freesansbold.ttf', 24)

        turn_color = (0, 0, 255)
        if game.current_turn == "White":
            turn_color = (0, 0, 255)
        else:
            turn_color = (0, 0, 0)

        turn_text = font.render(
            f"Turn: {game.current_turn}", True, turn_color)
        screen.blit(turn_text, (650, 20))

        white_count = len(game.white_pieces)
        black_count = len(game.black_pieces)
        count_text = font.render(
            f"White: {white_count}  Black: {black_count}", True, (255, 255, 255))
        screen.blit(count_text, (600, 50))

        if game.game_over:
            result_font = pygame.font.Font('freesansbold.ttf', 48)

            if game.winner == "Draw":
                result_text = result_font.render(
                    "DRAW!", True, (255, 255, 0))
            else:
                result_text = result_font.render(
                    f"{game.winner} WINS!", True, (0, 255, 0))

            result_rect = result_text.get_rect(center=(400, 100))
            screen.blit(result_text, result_rect)

            restart_font = pygame.font.Font('freesansbold.ttf', 24)
            restart_text = restart_font.render(
                "Press ESC to return to menu", True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(400, 500))
            screen.blit(restart_text, restart_rect)

        pygame.display.update()
        clock.tick(60)

    bgm_1()
