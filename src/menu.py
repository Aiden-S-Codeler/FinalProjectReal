from aiden_functions import difficulty
from benet_functions import hangman
from snake import snake_game as snake
import tkinter as tk

def main():

    root = tk.Tk()

    root.title("Main Menu")

    root.minsize(250,250)
    root.geometry("600x600+100+100")

    root.attributes("-fullscreen", True)

    minesweeper = tk.Button(root, text="MINESWEEPER", width=90, height=20, command=lambda: [root.destroy(), difficulty()])
    minesweeper.place(relx=0.35, rely=0.25, anchor=tk.CENTER)
    minesweeper['bg'] = "#c2c2c2"

    hangman_btn = tk.Button(root, text="HANGMAN", width=90, height=20, command=lambda: [root.destroy(), hangman()])
    hangman_btn.place(relx=0.65, rely=0.25, anchor=tk.CENTER)
    hangman_btn['bg'] = '#ffffff'

    snake_btn = tk.Button(root, text="SNAKE", width=90, height=20, command=lambda: [root.destroy(), snake()])
    snake_btn.place(relx=0.35, rely=0.55, anchor=tk.CENTER)
    snake_btn['bg'] = "#b1dab3"

    leave = tk.Button(root, text="LEAVE", width=90, height=20, command=lambda: root.destroy())
    leave.place(relx=0.65, rely=0.55, anchor=tk.CENTER)
    leave['bg'] = "#ffd0d0"


    root.mainloop()