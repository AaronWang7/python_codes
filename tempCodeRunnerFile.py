            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print("Clicked:", x, y)
                chess_game = ChessGame()
                board.board_x = x
                board.board_y = y
                pos = board.board_get()
                chess_game.setup_pieces()
                print("Piece position:", pos)