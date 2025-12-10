    def get_pieces_left(self, color):
        # Get count of remaining pieces for a color
        pieces = self.white_pieces if color == "White" else self.black_pieces
        return len(pieces)