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
    
    #for wa in detection:
    #    print(wa)

    #print("")

    #for wa in board:
    #    print(wa)

    return detection

def minesweeper():
    root = tk.Tk()

    root.title("Minesweeper")
    root.configure(background="#f3cc1d")

    root.minsize(250,250)
    root.maxsize(1500,1500)
    root.geometry("600x600+100+100")

    root.count = 0

    def add():
        root.count += 1
        lbl['text'] = str(root.count)

    def sub():
        root.count -= 1
        lbl['text'] = str(root.count)

    btn1 = tk.Button(root, text='       ', command=add)
    btn1.grid(row=4, column=1)

    btn2 = tk.Button(root, text='       ', command=sub)
    btn2.grid(row=4, column=2)

    lbl = tk.Label(root, text="0")
    lbl.grid(row=5, column=1, columnspan=2)

    close = tk.Button(root, text="LEAVE", command=root.destroy)
    close.grid(row=0, column=0)

    root.mainloop()

minesweeper()