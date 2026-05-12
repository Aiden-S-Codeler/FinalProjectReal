from aiden_functions import difficulty
from benet_functions import hangman
from snake import main2 as snake
import tkinter as tk

def main():

    root = tk.Tk()

    root.title("Main Menu")

    root.minsize(250,250)
    root.geometry("600x600+100+100")

    root.attributes("-fullscreen", True)

    minesweeper = tk.Button(root, text="MINESWEEPER", width=30, height=6, command=lambda: [root.destroy(), difficulty()])
    minesweeper.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    hangman_btn = tk.Button(root, text="HANGMAN", width=30, height=6, command=lambda: [root.destroy(), hangman()])
    hangman_btn.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    snake_btn = tk.Button(root, text="SNAKE", width=30, height=6, command=lambda: [root.destroy(), snake()])
    snake_btn.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    leave = tk.Button(root, text="LEAVE", width=30, height=6, command=lambda: root.destroy())
    leave.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


    root.mainloop()