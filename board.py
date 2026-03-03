import json
from pieces import Rook, Knight, Bishop, Queen, King, Pawn
    

class Board:

    def __init__(self):
        self.squares = {
            f"{chr(col)}{row}": None
            for col in range(ord('a'), ord('i'))
            for row in range(1, 9)
        }

        self.setup_board()

        for square, piece in self.squares.items():
            if piece is not None:
                piece.set_initial_position(square)
                piece.define_board(self)

    def setup_board(self):

        # Black pieces
        self.squares['a1'] = Rook('BLACK', 1)
        self.squares['b1'] = Knight('BLACK', 1)
        self.squares['c1'] = Bishop('BLACK', 1)
        self.squares['d1'] = Queen('BLACK', 1)
        self.squares['e1'] = King('BLACK', 1)
        self.squares['f1'] = Bishop('BLACK', 2)
        self.squares['g1'] = Knight('BLACK', 2)
        self.squares['h1'] = Rook('BLACK', 2)

        black_pawns = {
            f"{chr(col)}2": Pawn("BLACK", col - 96)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(black_pawns)

        # White pawns
        white_pawns = {
            f"{chr(col)}7": Pawn("WHITE", col - 96)
            for col in range(ord('a'), ord('i'))
        }

        self.squares.update(white_pawns)

        # White pieces
        self.squares['a8'] = Rook('WHITE', 1)
        self.squares['b8'] = Knight('WHITE', 1)
        self.squares['c8'] = Bishop('WHITE', 1)
        self.squares['d8'] = Queen('WHITE', 1)
        self.squares['e8'] = King('WHITE', 1)
        self.squares['f8'] = Bishop('WHITE', 2)
        self.squares['g8'] = Knight('WHITE', 2)
        self.squares['h8'] = Rook('WHITE', 2)

    def print_board(self):
        for row in range(1, 9):
            row_data = [
                self.squares[f"{chr(col)}{row}"]
                for col in range(ord('a'), ord('i'))
            ]
            print(row_data)


    def get_piece(self, square):
         return self.squares.get(square)

    def is_square_empty(self, square):
        return self.get_piece(square) is None

    def kill_piece(self, square):
        piece = self.get_piece(square)
        if piece:
            piece.die()
            self.squares[square] = None

    def find_piece(self, symbol: str, identifier: int, color: str):
        return [
            piece
            for piece in self.squares.values()
            if piece is not None
            and piece.symbol == symbol
            and piece.identifier == identifier
            and piece.color == color
        ]
    
def save_board(self):
    with open("board.txt", "a") as file:
        file.write(json.dumps({
            square: str(piece) if piece else None
            for square, piece in self.squares.items()
        }) + "\n")