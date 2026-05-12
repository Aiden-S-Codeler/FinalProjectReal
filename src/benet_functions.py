import tkinter as tk
from faker import Faker

def end(root, win_or_loss="loss", word=""):
    root.destroy()
    root = tk.Tk()
    root.minsize(425, 375)
    root.configure(bg="black")
    message = "You win!" if win_or_loss == "win" else "You lose!"
    time = 3000 if win_or_loss == "win" else 10000
    tk.Label(root, text=message, fg="white", bg="black", font=("Arial", 40)).pack(pady=20)
    tk.Label(root, text=f"The word was: {word}", fg="white", bg="black", font=("Arial", 20)).pack(pady=20)
    root.update_idletasks()
    root.after(time, lambda: root.destroy())

def hangman():
    root = tk.Tk()
    root.title("Hangman")
    root.minsize(425, 375)
    lbl = tk.Label(root, text="Choose the word size: ", font=743)
    btn4 = tk.Button(root, text="4", width=4, height=4, font=743, command=lambda: decide(root, 4, [btn4, btn5, btn6, btn7, btn8, lbl]))
    btn5 = tk.Button(root, text="5", width=4, height=4, font=743, command=lambda: decide(root, 5, [btn4, btn5, btn6, btn7, btn8, lbl]))
    btn6 = tk.Button(root, text="6", width=4, height=4, font=743, command=lambda: decide(root, 6, [btn4, btn5, btn6, btn7, btn8, lbl]))
    btn7 = tk.Button(root, text="7", width=4, height=4, font=743, command=lambda: decide(root, 7, [btn4, btn5, btn6, btn7, btn8, lbl]))
    btn8 = tk.Button(root, text="8", width=4, height=4, font=743, command=lambda: decide(root, 8, [btn4, btn5, btn6, btn7, btn8, lbl]))
    btn4.grid(row=4, column=4)
    btn5.grid(row=4, column=6)
    btn6.grid(row=4, column=8)
    btn7.grid(row=4, column=10)
    btn8.grid(row=4, column=12)
    lbl.grid(row=3, column=8)
    close = tk.Button(root, text="Close the program", font=743, width=16, height=3, command=root.destroy)
    close.grid(row=10,column=1)
    root.mainloop()

def finish(root):
    root.destroy()
    hangman()

def choice(root, letter, btn, word, lbl, hangman_label, hangman_art):
    btn.destroy()
    blank_word = lbl.cget("text")
    if letter in word:
        word_list = list(blank_word)
        for index, char in enumerate(word):
            if char == letter:
                word_list[index] = letter
        blank_word = "".join(word_list)
        lbl.config(text=blank_word)
    else:
        mistakes = hangman_art.index(hangman_label.cget("text"))
        mistakes += 1
        if hangman_art.index(hangman_label.cget("text")) == 5:
            end(root, "loss", word)
        else:
            hangman_label.config(text=hangman_art[mistakes])

def guess(root, word, hangman_label, guess_entry, hangman_art):
    if guess_entry.get() == word:
        end(root, "win", word)
    else:
        mistakes = hangman_art.index(hangman_label.cget("text"))
        mistakes += 1
        if hangman_art.index(hangman_label.cget("text")) == 5:
            end(root, "loss", word)
        hangman_label.config(text=hangman_art[mistakes])

def decide(root, num, buttons):
    fake = Faker()
    while True:
        word = fake.word()
        if len(word) == num:
            break
    delete(buttons)
    hangman_art = [
        "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
    ]
    hangman_label = tk.Label(root, text="   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========", font=743)
    hangman_label.grid(row=0, column=0)
    text = "_" * len(word)
    lbl = tk.Label(root, text=text, font=1500)
    lbl.grid(row=5, column=1, columnspan=2)
    guess_entry = tk.Entry(root, font=743)
    guess_entry.grid(row=6, column=1)
    guess_btn = tk.Button(root, text="Guess", width=5, height=4, command=lambda: guess(root, word, hangman_label, guess_entry, hangman_art))
    guess_btn.grid(row=6, column=2)
    a = tk.Button(root, text=" A ", font=743, width=8, height=4, command=lambda: choice(root, "a", a, word, lbl, hangman_label, hangman_art))
    b = tk.Button(root, text=" B ", font=743, width=8, height=4, command=lambda: choice(root, "b", b, word, lbl, hangman_label, hangman_art))
    c = tk.Button(root, text=" C ", font=743, width=8, height=4, command=lambda: choice(root, "c", c, word, lbl, hangman_label, hangman_art))
    d = tk.Button(root, text=" D ", font=743, width=8, height=4, command=lambda: choice(root, "d", d, word, lbl, hangman_label, hangman_art))
    e = tk.Button(root, text=" E ", font=743, width=8, height=4, command=lambda: choice(root, "e", e, word, lbl, hangman_label, hangman_art))
    f = tk.Button(root, text=" F ", font=743, width=8, height=4, command=lambda: choice(root, "f", f, word, lbl, hangman_label, hangman_art))
    g = tk.Button(root, text=" G ", font=743, width=8, height=4, command=lambda: choice(root, "g", g, word, lbl, hangman_label, hangman_art))
    h = tk.Button(root, text=" H ", font=743, width=8, height=4, command=lambda: choice(root, "h", h, word, lbl, hangman_label, hangman_art))
    i = tk.Button(root, text=" I ", font=743, width=8, height=4, command=lambda: choice(root, "i", i, word, lbl, hangman_label, hangman_art))
    j = tk.Button(root, text=" J ", font=743, width=8, height=4, command=lambda: choice(root, "j", j, word, lbl, hangman_label, hangman_art))
    k = tk.Button(root, text=" K ", font=743, width=8, height=4, command=lambda: choice(root, "k", k, word, lbl, hangman_label, hangman_art))
    l = tk.Button(root, text=" L ", font=743, width=8, height=4, command=lambda: choice(root, "l", l, word, lbl, hangman_label, hangman_art))
    m = tk.Button(root, text=" M ", font=743, width=8, height=4, command=lambda: choice(root, "m", m, word, lbl, hangman_label, hangman_art))
    n = tk.Button(root, text=" N ", font=743, width=8, height=4, command=lambda: choice(root, "n", n, word, lbl, hangman_label, hangman_art))
    o = tk.Button(root, text=" O ", font=743, width=8, height=4, command=lambda: choice(root, "o", o, word, lbl, hangman_label, hangman_art))
    p = tk.Button(root, text=" P ", font=743, width=8, height=4, command=lambda: choice(root, "p", p, word, lbl, hangman_label, hangman_art))
    q = tk.Button(root, text=" Q ", font=743, width=8, height=4, command=lambda: choice(root, "q", q, word, lbl, hangman_label, hangman_art))
    r = tk.Button(root, text=" R ", font=743, width=8, height=4, command=lambda: choice(root, "r", r, word, lbl, hangman_label, hangman_art))
    s = tk.Button(root, text=" S ", font=743, width=8, height=4, command=lambda: choice(root, "s", s, word, lbl, hangman_label, hangman_art))
    t = tk.Button(root, text=" T ", font=743, width=8, height=4, command=lambda: choice(root, "t", t, word, lbl, hangman_label, hangman_art))
    u = tk.Button(root, text=" U ", font=743, width=8, height=4, command=lambda: choice(root, "u", u, word, lbl, hangman_label, hangman_art))
    v = tk.Button(root, text=" V ", font=743, width=8, height=4, command=lambda: choice(root, "v", v, word, lbl, hangman_label, hangman_art))
    w = tk.Button(root, text=" W ", font=743, width=8, height=4, command=lambda: choice(root, "w", w, word, lbl, hangman_label, hangman_art))
    x = tk.Button(root, text=" X ", font=743, width=8, height=4, command=lambda: choice(root, "x", x, word, lbl, hangman_label, hangman_art))
    y = tk.Button(root, text=" Y ", font=743, width=8, height=4, command=lambda: choice(root, "y", y, word, lbl, hangman_label, hangman_art))
    z = tk.Button(root, text=" Z ", font=743, width=8, height=4, command=lambda: choice(root, "z", z, word, lbl, hangman_label, hangman_art))
    a.grid(row=10, column=10)
    b.grid(row=10, column=12)
    c.grid(row=10, column=14)
    d.grid(row=10, column=16)
    e.grid(row=10, column=18)
    f.grid(row=12, column=10)
    g.grid(row=12, column=12)
    h.grid(row=12, column=14)
    i.grid(row=12, column=16)
    j.grid(row=12, column=18)
    k.grid(row=14, column=10)
    l.grid(row=14, column=12)
    m.grid(row=14, column=14)
    n.grid(row=14, column=16)
    o.grid(row=14, column=18)
    p.grid(row=16, column=10)
    q.grid(row=16, column=12)
    r.grid(row=16, column=14)
    s.grid(row=16, column=16)
    t.grid(row=16, column=18)
    u.grid(row=18, column=10)
    v.grid(row=18, column=12)
    w.grid(row=18, column=14)
    x.grid(row=18, column=16)
    y.grid(row=18, column=18)
    z.grid(row=20, column=14)
    return word, lbl

def delete(buttons):
    for btn in buttons:
        btn.destroy()

hangman()