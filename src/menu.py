# tknter menu that displays the two option: scored and unscored games, then within each it calls the file for each game
import tkinter as tk
from snake import *
from aiden_functions import *
from benet_functions import *
def tk_menu():
    root = tk.Tk()
    root.title("Game Menu")

    def start_snake():
        root.destroy()  
        main2()  


    def start_aiden():
        root.destroy()  
        board_maker()  

    def start_benet():
        root.destroy()  
        #bennets game func when made ()  
    tk.Label(root, text="pick from tweegames", font=("Arial", 16)).pack (pady=20)

    tk.Button(root, text="Snake Game (Scored)", command=start_snake, width=20).pack(pady=10)
    tk.Button(root, text="minesweeper (scored)", command=start_aiden, width=20).pack(pady=10)
    tk.Button(root, text="hangman (Unscored)", command=start_benet, width=20).pack(pady=10)

    root.mainloop()