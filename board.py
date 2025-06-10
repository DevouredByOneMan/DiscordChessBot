#Each x,y coord on the Board will be a 'piece'
#standard chess board configuration, alternating black and white squares, 8x8 2D piece type
from chess_pieces import Black_Square, Black_Rook, Black_Knight, Black_Bishop, Black_Queen, Black_King, Black_Pawn
from chess_pieces import White_Square, White_Rook, White_Knight, White_Bishop, White_Queen, White_King, White_Pawn

class Board:
    BS = Black_Square()
    BR = Black_Rook()
    BN = Black_Knight()
    BB = Black_Bishop()
    BQ = Black_Queen()
    BK = Black_King()
    BP = Black_Pawn()

    WS = White_Square()
    WR = White_Rook()
    WN = White_Knight()
    WB = White_Bishop()
    WQ = White_Queen()
    WK = White_King()
    WP = White_Pawn()

    table = [[BR, BN, BB, BQ, BK, BB, BN, BR],
        [BP, BP, BP, BP, BP, BP, BP, BP],
        [WS, BS, WS, BS, WS, BS, WS, BS],
        [BS, WS, BS, WS, BS, WS, BS, WS],
        [WS, BS, WS, BS, WS, BS, WS, BS],
        [BS, WS, BS, WS, BS, WS, BS, WS],
        [WP, WP, WP, WP, WP, WP, WP, WP],
        [WR, WN, WB, WQ, WK, WB, WN, WR]]

    def move(self, xi, yi, xo, yo):
        #replace with respective square
        self.table[yo][xo] = self.table[yi][xi]
        self.place_square(xi, yi)

    def place_square(self, x, y):
        if x % 2 == 0 and y % 2 == 0:
            self.table[y][x] = self.WS
        elif x % 2 == 1 and y % 2 == 0:
            self.table[y][x] = self.BS
        elif x % 2 == 0 and y % 2 == 1:
            self.table[y][x] = self.BS
        elif x % 2 == 1 and y % 2 == 1:
            self.table[y][x] = self.WS
    def printTable(self):
        #return a string that displays on discord
        top_border = [
            ["♣ |  A   B   C  D   E   F   G   H"],
            ["--|------------------------"]
        ]
        bot_border = [
            ["--|------------------------"],
            ["    |  A   B   C  D   E   F   G   H"]
        ]
        sid_border = [ "8 | ", "7 | " , "6 | ", "5 | ", "4 | ", "3 | ","2 | "," 1 | "]

        parts = []

        for tb in top_border:
            parts.append(tb)

        c = 0
        for i in self.table:
            temp = []
            temp.append(sid_border[c])
            for j in i:
                temp.append(j.value)
            parts.append(temp)
            c += 1


        for bb in bot_border:
            parts.append(bb)

        return '\n'.join(' '.join(item for item in innerlist) for innerlist in parts)

    def __str__(self):
        return self.printTable()