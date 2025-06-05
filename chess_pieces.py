#Chess pieces:
#             ◼ ♜ ♞ ♝ ♛ ♚ ♟​
#             ◻ ♖ ♘ ♗ ♕ ♔ ♙
# all the functions within the pieces are validation functions
class Piece: #parent class
    pos = "X9" #default value
    value = 'X'
    color = 'X'
    x = -1
    y = -1
    def __str__(self):
        return f"{self.value} is the current piece"

#children classes
class Black_Square(Piece):
    value = ' '
    color = 'B'
    #SWAP

class Black_Rook(Piece):
    value = '♜'
    color = 'B'

class Black_Knight(Piece):
    value = '♞'
    color = 'B'

class Black_Bishop(Piece):
    value = '♝'
    color = 'B'

class Black_Queen(Piece):
    value = '♛'
    color = 'B'

class Black_King(Piece):
    value = '♚'
    color = 'B'

class Black_Pawn(Piece):
    value = '♟​'
    color = 'B'
    def move(self, xi, yi, xo, yo):
        pass


class White_Square(Piece):
    value = ' '
    color = 'W'

class White_Rook(Piece):
    value = '♖'
    color = 'W'

class White_Knight(Piece):
    value = '♘'
    color = 'W'

class White_Bishop(Piece):
    value = '♗'
    color = 'W'

class White_Queen(Piece):
    value = '♕'
    color = 'W'

class White_King(Piece):
    value = '♔'
    color = 'W'

class White_Pawn(Piece):
    value = '♙'
    color = 'W'