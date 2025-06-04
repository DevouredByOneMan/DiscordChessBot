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

    table = [
        ["♣ |  A   B   C  D   E   F   G   H"],
        ["--|------------------------"],
        [" 1 | ", BR.value, BN.value, BB.value, BQ.value, BK.value, BB.value, BN.value,  BR.value],
        ["2 | ", BP.value, BP.value, BP.value, BP.value, BP.value, BP.value, BP.value, BP.value],
        ["3 | ", WS.value, BS.value, WS.value, BS.value, WS.value, BS.value, WS.value, BS.value],
        ["4 | ", BS.value, WS.value, BS.value, WS.value, BS.value, WS.value, BS.value, WS.value],
        ["5 | ", WS.value, BS.value, WS.value, BS.value, WS.value, BS.value, WS.value, BS.value],
        ["6 | ", BS.value, WS.value, BS.value, WS.value, BS.value, WS.value, BS.value, WS.value],
        ["7 | ", WP.value, WP.value, WP.value, WP.value, WP.value, WP.value, WP.value, WP.value],
        ["8 | ", WR.value, WN.value, WB.value, WQ.value, WK.value, WB.value, WN.value, WR.value],
        ["--|------------------------"],
        ["    |  A   B   C  D   E   F   G   H"]
    ]

    def __str__(self):
        result = '\n'.join(' '.join(item for item in innerlist) for innerlist in self.table)
        return result