from board import Board

board = Board()
board.print_board()

print("\n--- Moving BLACK Pawn at a2 ---\n")

pawn = board.squares["a2"]
pawn.move()

board.print_board()