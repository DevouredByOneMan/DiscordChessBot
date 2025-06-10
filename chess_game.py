#handles all the logic and returns the board to main.py
#takes in user input from main.py, and verifies the input
#returns if the input is wrong
#main.py handles all the messages to be printed to discord

from board import Board
from chess_pieces import Black_Square, Black_Rook, Black_Knight, Black_Bishop, Black_Queen, Black_King, Black_Pawn
from chess_pieces import White_Square, White_Rook, White_Knight, White_Bishop, White_Queen, White_King, White_Pawn

def position_verification(msg, board):
    temp = msg.split(" ")
    s_pos = temp[0]
    e_pos = temp[1]
    s_list = list(s_pos)
    e_list = list(e_pos)
    #check if the length of the list is 2
    if len(e_list) != 2 or len(s_list) != 2:
        return False
    #convert the inputs to coord inputs
    xi = letter_converter(s_list[0])
    xo = letter_converter(e_list[0])
    yi = abs(int(s_list[1]) - 8)
    yo = abs(int(e_list[1]) - 8)

    #overall invalid inputs
    if xi == -1 or xo == -1 or yi > 7 or yo > 7:
        return False
    print(xi, xo, yi, yo)
    #passes verification step 1
    board.move(xi, yi, xo, yo)
    return True

def letter_converter(char):
    if char == 'a':
        return 0
    elif char == 'b':
        return 1
    elif char == 'c':
        return 2
    elif char == 'd':
        return 3
    elif char == 'e':
        return 4
    elif char == 'f':
        return 5
    elif char == 'g':
        return 6
    elif char == 'h':
        return 7
    #else
    return -1