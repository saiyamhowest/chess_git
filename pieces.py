from abc import ABC, abstractmethod


class BaseChessPiece(ABC):

    def __init__(self, color, name, symbol, identifier):
        self.color = color
        self.name = name
        self.symbol = symbol
        self.identifier = identifier
        self.position = None
        self.is_alive = True
        self.board = None

    @abstractmethod
    def move(self):
        pass

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
        print("Pawn moves forward 1 square")


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