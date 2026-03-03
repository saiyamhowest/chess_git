from abc import ABC, abstractmethod
from movement import BoardMovement


class BaseChessPiece(ABC):

    def __init__(self, color, name, symbol, identifier):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = None
        self.is_alive = True
        self.board = None

    def move(self, new_position):

        if self.board is None:
            print("Error: Piece is not on a board")
            return

        target_piece = self.board.squares.get(new_position)

    # If square occupied by same color → block
        if target_piece and target_piece.color == self.color:
            print("Move blocked by same color piece")
            return

    # If enemy → kill
        if target_piece and target_piece.color != self.color:
            target_piece.die()

    # Clear old square
        self.board.squares[self.position] = None

    # Move piece
        self.position = new_position
        self.board.squares[new_position] = self

    def die(self):
        self.is_alive = False

    def set_initial_position(self, position):
        self.position = position

    def define_board(self, board):
        self.board = board

    def __str__(self):
        return f"{self.color} {self.name} {self.identifier}"

    __repr__ = __str__


class Pawn(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Pawn", "-", identifier)

    def move(self):
        new_position = BoardMovement.forward(self.position, self.color)
        super().move(new_position)


class Rook(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Rook", "R", identifier)

    def move(self):
        print("Rook moves straight")


class Bishop(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Bishop", "B", identifier)

    def move(self):
        print("Bishop moves diagonally")


class Knight(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Knight", "N", identifier)

    def move(self):
        print("Knight moves in L shape")


class Queen(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "Queen", "Q", identifier)

    def move(self):
        print("Queen moves everywhere")


class King(BaseChessPiece):
    def __init__(self, color, identifier):
        super().__init__(color, "King", "K", identifier)

    def move(self):
        print("King moves one square any direction")