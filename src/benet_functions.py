import tkinter as tk
import faker

def hangman():
    root = tk.Tk()
    root.title("Hangman")
    root.minsize(2550, 1375)
    root.maxsize(2550, 1375)
    root.geometry("2550,1375+0+0")
    def decide(num):
        faker.word.sample(num)
        for i in [btn4, btn5, btn6, btn7, btn8]:
            i.delete()
    def a():
        root.count += 1
        lbl['text'] = str(root.count)
    def b():
        root.count -= 1
        lbl['text'] = str(root.count)

    btn = tk.Button(root, text="ADD", command=add).grid(row=4, column=0)
    btn2 = tk.Button(root, text="SUB", command=sub).grid(row=4,column=2)
    lbl = tk.Label(root, text="0")
    lbl.grid(row=5, column=1, columnspan=2)

    close = tk.Button(root, text="Bye", command=root.destroy).grid(row=6,column=1)

    root.mainloop()

