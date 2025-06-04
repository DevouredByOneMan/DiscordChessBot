#Each x,y coord on the Board will be a 'piece'
#Chess pieces:
#             ■ ♜ ♞ ♝ ♛ ♚ ♟︎
#             □ ♖ ♘ ♗ ♕ ♔ ♙
class Piece: #parent class
    pos = "X9" #default value
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f"{self.value} is the current piece"

#children classes
class Black_Square(Piece('■', 'B')):
    pass

class Black_Rook(Piece('♜', 'B')):


class White_Square(Piece('□', 'W')):
    pass

