#AS 2nd minesweeper functions

import random

def board_maker(board_width, board_height, minbombs = 10, maxbombs = 15):
    row = []
    for x in range(0, board_width):
        row.append(0)

    board = [

    ]
    for y in range(0, board_height):
        board.append(row)
    
    for x in range(0, len(board)):
        for y in range(0, len(board[x])):
            number = random.randint(1, 6)
            if number == 6:
                print(x)
                board[x][y] = 1
            else:
                pass
#    
#    for each tile on board
#        if the tile is a bomb
#            move on
#        otherwise
#            check all nearby tiles for bombs
#                if the 

    for line in board:
        print(line)

board_maker(10, 10)