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
    color = 'BS'

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
    def move(self, xi, yi, xo, yo, board):
        pass
    # if pawn starts at X7, pawn can move down 1 or 2 squares
        # if piece is in the way, invalid move
        # if piece can attack, take that square
        # if en passant is possible, take that square

    # else pawn move down 1
        #if piece is in the way, invalid move
        #if piece can attack, take that square
        #if piece reaches the end, promote

class White_Square(Piece):
    value = ' '
    color = 'WS'

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
    def move(self, xi, xo, yi, yo, board):
        #if pawn starts at X2, pawn can move up 1 or 2 squares
        if yi == 2 and (yo - yi) < 3:
            #if piece is in the way
            if board.returnPieceColor(xo, yo) == 'W' or board.returnPieceColor(xo, yo) == 'B':
                print("invalid move")
            #if piece can attack
            #if en passant is possible

        #else pawn move up 1
            #if piece is in the way
            #if piece can attack