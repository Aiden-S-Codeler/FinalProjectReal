#AS 2nd minesweeper functions

import random

def board_maker(board_width, board_height, minbombs = 10, maxbombs = 15):

    board = []
    
    for y in range(0, board_height):
        row = []
        for x in range(0, board_width):
            number = random.randint(1, 6)
            if number == 6:
                row.append(1)
            else:
                row.append(0)
        board.append(row)
    
    detection = board
    for line in detection:
        for tile in range(0, len(line)):
            line[tile] = 0

    for x in range(0, len(detection)):
        d_line = detection(x)
        for y in range(0, len(line)):
            if board[x][y] == 1:
                pass
            else:
                bomb_total = 0
                behind = False
                forward = False
                up = False
                down = False
                if y-1 < 0:
                    behind = True
                if y+1 < 0:
                    forward = True
                if y-1 < 0:
                    up = True
                if y-1 < 0:
                    down = True


    for line in detection:
        print(line)

board_maker(10, 10)