#AS 2nd minesweeper functions

from logging import root
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

    for line in detection:
        print(line)

    return detection

def minesweeper(board_width, board_height, board):

    root = tk.Tk()

    root.title("Minesweeper")
    root.configure(background="#003f18")

    root.minsize(250,250)
    root.geometry("600x600+100+100")
    root.attributes("-fullscreen", True)

    visited = []

    all_bombs = []
    

    def add(x, y):

        if lbl['text'] == "GAME OVER" or lbl['text'] == "YOU WIN!":
            return
        elif game_board[x][y]['bg'] == '#0000ff':
            return
        elif game_board[x][y] in visited:
            return
        else:
            lbl['text'] = str(board[x][y])
            game_board[x][y]['text'] = f' {board[x][y]}  '

            visited.append(game_board[x][y])

            behind = True
            forward = True
            up = True
            down = True
            if y-1 < 0:
                behind = False
            if y+1 > board_height-1:
                forward = False
            if x-1 < 0:
                up = False
            if x+1 > board_width-1:
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
            
            if '1' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#34ff00"
            
            if '2' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#82e800"
            
            if '3' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#aad000"
            
            if '4' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#c5b700"
            
            if '5' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#db9b00"
            
            if '6' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#ed7b00"
            
            if '7' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#fa5100"
            
            if '8' in game_board[x][y]['text']:
                    game_board[x][y]['bg'] = "#ff0000"

            if board[x][y] == 'B':
                for u in range(0, board_width):
                    for d in range(0, board_height):
                        if board[u][d] == 'B':
                            game_board[u][d]['text'] = '     '
                            game_board[u][d]['bg'] = 'black'
                lbl['text'] = "GAME OVER"
                return
            
            if len(visited) == (board_width*board_height)-len(all_bombs):
                lbl['text'] = "YOU WIN!"
                return
        
    def flag(x, y):
        if lbl['text'] == "GAME OVER" or lbl['text'] == "YOU WIN!":
            return
        elif game_board[x][y]['text'] != '     ':
            return
        else:
            if game_board[x][y]['bg'] == '#ffffff':
                game_board[x][y]['bg'] = '#0000ff'
            elif game_board[x][y]['bg'] == '#0000ff':
                game_board[x][y]['bg'] = '#ffffff'
    
    def auto_win():
        for x in range(board_width):
            for y in range(board_height):
                if board[x][y] != 'B' and game_board[x][y]['bg'] == '#ffffff':
                    add(x, y)
    
    def auto_flag():
        for x in range(board_width):
            for y in range(board_height):
                if board[x][y] == 'B' and game_board[x][y]['bg'] == '#ffffff':
                    flag(x, y)
    
    def auto_lose():
        for x in range(board_width):
            for y in range(board_height):
                if board[x][y] == 'B' and game_board[x][y]['bg'] == '#ffffff':
                    add(x, y)
    
    def auto_unflag():
        for x in range(board_width):
            for y in range(board_height):
                if board[x][y] == 'B' and game_board[x][y]['bg'] == '#0000ff':
                    flag(x, y)
    
    game_board = []

    for x in range(0, board_width):
        game_row = []
        for y in range(0, board_height):
            btn = tk.Button(root, text=f'     ', command=lambda x=x, y=y: add(x, y))
            btn.grid(row=x+1, column=y+2)
            btn['bg'] = '#ffffff'
            btn.bind("<Button-3>", lambda event, x=x, y=y: flag(x, y))
            game_row.append(btn)
        game_board.append(game_row)

    for x in range(board_width):
        for y in range(board_height):
            if board[x][y] == 'B':
                all_bombs.append(game_board[x][y])

    lbl = tk.Label(root)
    lbl.grid(row=7, column=0)

    separator = tk.Label(root, text="       ")
    separator.grid(row=0, column=1)
    separator['bg'] = "#003f18"

    close = tk.Button(root, text="LEAVE", command=lambda: [root.destroy(), difficulty()])
    close.grid(row=0, column=0)

    restart = tk.Button(root, text="RESTART", command=lambda: [root.destroy(), minesweeper(board_width, board_height, board_maker(board_width, board_height, 8, ((board_width*board_height)/100)*10, ((board_width*board_height)/100)*15))])
    restart.grid(row=1, column=0)

    win = tk.Button(root, text="AUTO WIN", command=auto_win)
    win.grid(row=2, column=0)

    lose = tk.Button(root, text="AUTO LOSE", command=auto_lose)
    lose.grid(row=3, column=0)

    flagger = tk.Button(root, text="AUTO FLAG", command=auto_flag)
    flagger.grid(row=4, column=0)

    unflagger = tk.Button(root, text="AUTO UNFLAG", command=auto_unflag)
    unflagger.grid(row=5, column=0)

    root.mainloop()

def difficulty():
    root = tk.Tk()

    root.title("Minesweeper Difficulty Select")

    root.minsize(250,250)
    root.geometry("600x600+100+100")
    root.attributes("-fullscreen", True)

    def choice(x, y):
        root.destroy()
        minesweeper(x, y, board_maker(x, y, 8, ((x*y)/100)*12, ((x*y)/100)*20))

    easy = tk.Button(root, text="EASY 10x10", width=30, height=6, command=lambda: choice(10, 10))
    easy.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    medium = tk.Button(root, text="MEDIUM 25x25", width=30, height=6, command=lambda: choice(25, 25))
    medium.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    hard = tk.Button(root, text="HARD 40x40", width=30, height=6, command=lambda: choice(40, 40))
    hard.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def go_back():
        root.destroy()
        from main import main
        main()

    back = tk.Button(root, text="BACK", width=10, height=2, command=go_back)
    back.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    root.mainloop()