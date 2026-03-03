class BoardMovement:

    @staticmethod
    def forward(position, color):
        column = position[0]
        row = int(position[1])

        if color == "WHITE":
            new_row = row - 1
        else:
            new_row = row + 1

        if new_row < 1 or new_row > 8:
            return position  # block movement at edge

        return f"{column}{new_row}"