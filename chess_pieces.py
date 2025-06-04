#Each x,y coord on the Board will be a 'piece'
#Chess pieces:
#             ■ ♜ ♞ ♝ ♛ ♚ ♟︎
#             □ ♖ ♘ ♗ ♕ ♔ ♙
class Piece: #parent class
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.value} is the current piece"

#children classes
class Black_Square(Piece('B', '■')):
    pass

class White_Square(Piece('W', '□')):
    pass