#AS 2nd minesweeper functions

import random
import tkinter as tk

def board_maker(board_width, board_height, bomb_chance = 8, minbombs = 10, maxbombs = 15):

    board = []
    all_bomb = 0
    while all_bomb < minbombs or all_bomb > maxbombs:
        board = []
        all_bomb = 0
        for y in range(0, board_height):
            row = []
            for x in range(0, board_width):
                number = random.randint(1, bomb_chance)
                if number == bomb_chance:
                    row.append(1)
                else:
                    row.append(0)
            board.append(row)
    
        for line in board:
            for tile in line:
                if tile == 1:
                    all_bomb += 1
    
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
    
    for wa in detection:
        print(wa)

    #print("")

    #for wa in board:
    #    print(wa)

    return detection

def minesweeper(board_width, board_height, board):
    root = tk.Tk()

    root.title("Minesweeper")
    root.configure(background="#003f18")

    root.minsize(250,250)
    root.maxsize(1500,1500)
    root.geometry("600x600+100+100")

    visited = []

    def add(x, y):
        
        lbl['text'] = str(board[x][y])
        game_board[x][y]['text'] = f' {board[x][y]}  '

        visited.append(game_board[x][y])

        behind = True
        forward = True
        up = True
        down = True
        if y-1 < 0:
            behind = False
        if y+1 > board_width-1:
            forward = False
        if x-1 < 0:
            up = False
        if x+1 > board_height-1:
            down = False
                
        if '0' in game_board[x][y]['text'] and behind == True:
            if game_board[x][y-1] not in visited:
                add(x, y-1)
            if up == True:
                if game_board[x-1][y-1] not in visited:
                    add(x-1, y-1)
            if down == True:
                if game_board[x+1][y-1] not in visited:
                    add(x+1, y-1)
                
        if '0' in game_board[x][y]['text'] and forward == True:
            if game_board[x][y+1] not in visited:
                add(x, y+1)
            if up == True:
                if game_board[x-1][y+1] not in visited:
                    add(x-1, y+1)
            if down == True:
                if game_board[x+1][y+1] not in visited:
                    add(x+1, y+1)
        
        if '0' in game_board[x][y]['text'] and up == True:
            if game_board[x-1][y] not in visited:
                add(x-1, y)

        if '0' in game_board[x][y]['text'] and down == True:
            if game_board[x+1][y] not in visited:
                add(x+1, y)
    
    restart = tk.Button(root, text="RESTART", command=lambda: [root.destroy(), minesweeper(board_width, board_height, board_maker(board_width, board_height, 8, ((board_width*board_height)/100)*10, ((board_width*board_height)/100)*15))])
    restart.grid(row=1, column=0)
    
    game_board = []

    for x in range(0, board_width):
        game_row = []
        for y in range(0, board_height):
            btn = tk.Button(root, text=f'     ', command=lambda x=x, y=y: add(x, y))
            btn.grid(row=x+1, column=y+2)
            game_row.append(btn)
        game_board.append(game_row)

    lbl = tk.Label(root, text="0")
    lbl.grid(row=3, column=0)

    close = tk.Button(root, text="LEAVE", command=root.destroy)
    close.grid(row=0, column=0)

    root.mainloop()

x = 20
y = 20

minesweeper(x, y, board_maker(x, y, 8, ((x*y)/100)*12, ((x*y)/100)*20))