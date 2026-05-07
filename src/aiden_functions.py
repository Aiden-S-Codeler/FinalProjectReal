#AS 2nd minesweeper functions

import random
import pygame

def board_maker(board_width, board_height, minbombs = 10, maxbombs = 15):

    board = []
    all_bomb = 0
    while all_bomb < minbombs or all_bomb > maxbombs:
        all_bomb = 0
        for y in range(0, board_height):
            row = []
            for x in range(0, board_width):
                number = random.randint(1, 8)
                if number == 8:
                    row.append(1)
                else:
                    row.append(0)
            board.append(row)
    
        for line in board:
            for tile in line:
                if tile == 1:
                    all_bomb += 1
    
    for wa in board:
        print(wa)
    
    print("")
    
    detection = []

    for line in board:
        detection.append(line[:])

    for line in detection:
        for tile in range(0, len(line)):
            line[tile] = 0

    for x in range(0, len(detection)):
        
        d_line = detection[x]

        for y in range(0, len(d_line)):
            if board[x][y] == 1:
                d_line[y] = "B"
            else:
                bomb_total = 0
                behind = True
                forward = True
                up = True
                down = True
                if y-1 < 0:
                    behind = False
                if y+1 > len(d_line)-1:
                    forward = False
                if x-1 < 0:
                    up = False
                if x+1 > len(detection)-1:
                    down = False
                
                if behind == True:
                    if board[x][y-1] == 1:
                        bomb_total += 1
                    if up == True:
                        if board[x-1][y-1] == 1:
                            bomb_total += 1
                    if down == True:
                        if board[x+1][y-1] == 1:
                            bomb_total += 1
                
                if forward == True:
                    if board[x][y+1] == 1:
                        bomb_total += 1
                    if up == True:
                        if board[x-1][y+1] == 1:
                            bomb_total += 1
                    if down == True:
                        if board[x+1][y+1] == 1:
                            bomb_total += 1
                
                if up == True:
                    if board[x-1][y] == 1:
                        bomb_total += 1

                if down == True:
                    if board[x+1][y] == 1:
                        bomb_total += 1

                d_line[y] = str(bomb_total)
        
        detection[x] = d_line
    
    print("end")

    for wa in board:
        print(wa)

board_maker(10, 10)