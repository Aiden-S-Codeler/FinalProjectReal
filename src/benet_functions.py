import pygame
import tkinter as tk
from faker import Faker

def lose():
    pygame.init()
    screen = pygame.display.set_mode((2550, 1375))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen = pygame.display.set_mode((2550, 1375))
    pygame.quit()

def hangman():
    root = tk.Tk()
    root.title("Hangman")
    root.minsize(2550, 1375)
    root.maxsize(2550, 1375)
    btn4 = tk.Button(root, text="4", command=lambda: decide(root, 4, [btn4, btn5, btn6, btn7, btn8]))
    btn5 = tk.Button(root, text="5", command=lambda: decide(root, 5, [btn4, btn5, btn6, btn7, btn8]))
    btn6 = tk.Button(root, text="6", command=lambda: decide(root, 6, [btn4, btn5, btn6, btn7, btn8]))
    btn7 = tk.Button(root, text="7", command=lambda: decide(root, 7, [btn4, btn5, btn6, btn7, btn8]))
    btn8 = tk.Button(root, text="8", command=lambda: decide(root, 8, [btn4, btn5, btn6, btn7, btn8]))
    btn4.grid(row=4, column=4)
    btn5.grid(row=4, column=6)
    btn6.grid(row=4, column=8)
    btn7.grid(row=4, column=10)
    btn8.grid(row=4, column=12)
    close = tk.Button(root, text="Close the program", command=root.destroy).grid(row=10,column=1)
    root.mainloop()

def choice(letter, btn, word, lbl, hangman_label, root):
    btn.destroy()
    hangman_art = [
        "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
    ]
    if letter in word:
        for let in word:
            if let == letter:
                blank_word = blank_word[:let] + letter + blank_word[let + 1:]
        lbl.config(text=blank_word)
        return blank_word
    else:
        mistakes = hangman_art.index(hangman_label.cget("text"))
        mistakes += 1
        if mistakes == 7:
            root.destroy
        hangman_label.config(text=hangman_art[mistakes])

def decide(root, num, buttons):
    fake = Faker()
    while True:
        word = fake.word()
        if len(word) == num:
            break
    delete(buttons)
    hangman_label = tk.Label(root, text="   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========")
    hangman_label.grid(row=0, column=0)
    text = "_" * len(word)
    lbl = tk.Label(root, text=text)
    lbl.grid(row=5, column=1, columnspan=2)
    guess_entry = tk.Entry(root, width=5)
    guess_entry.grid(row=6, column=1)
    guess_btn = tk.Button(root, text="Guess")
    guess_btn.grid(row=6, column=2)
    mistakes = 0
    a = tk.Button(root, text=" A ", command=lambda: choice("a", a, word, lbl, hangman_label, root))
    b = tk.Button(root, text=" B ", command=lambda: choice("b", b, word, lbl, hangman_label, root))
    c = tk.Button(root, text=" C ", command=lambda: choice("c", c, word, lbl, hangman_label, root))
    d = tk.Button(root, text=" D ", command=lambda: choice("d", d, word, lbl, hangman_label, root))
    e = tk.Button(root, text=" E ", command=lambda: choice("e", e, word, lbl, hangman_label, root))
    f = tk.Button(root, text=" F ", command=lambda: choice("f", f, word, lbl, hangman_label, root))
    g = tk.Button(root, text=" G ", command=lambda: choice("g", g, word, lbl, hangman_label, root))
    h = tk.Button(root, text=" H ", command=lambda: choice("h", h, word, lbl, hangman_label, root))
    i = tk.Button(root, text=" I ", command=lambda: choice("i", i, word, lbl, hangman_label, root))
    j = tk.Button(root, text=" J ", command=lambda: choice("j", j, word, lbl, hangman_label, root))
    k = tk.Button(root, text=" K ", command=lambda: choice("k", k, word, lbl, hangman_label, root))
    l = tk.Button(root, text=" L ", command=lambda: choice("l", l, word, lbl, hangman_label, root))
    m = tk.Button(root, text=" M ", command=lambda: choice("m", m, word, lbl, hangman_label, root))
    n = tk.Button(root, text=" N ", command=lambda: choice("n", n, word, lbl, hangman_label, root))
    o = tk.Button(root, text=" O ", command=lambda: choice("o", o, word, lbl, hangman_label, root))
    p = tk.Button(root, text=" P ", command=lambda: choice("p", p, word, lbl, hangman_label, root))
    q = tk.Button(root, text=" Q ", command=lambda: choice("q", q, word, lbl, hangman_label, root))
    r = tk.Button(root, text=" R ", command=lambda: choice("r", r, word, lbl, hangman_label, root))
    s = tk.Button(root, text=" S ", command=lambda: choice("s", s, word, lbl, hangman_label, root))
    t = tk.Button(root, text=" T ", command=lambda: choice("t", t, word, lbl, hangman_label, root))
    u = tk.Button(root, text=" U ", command=lambda: choice("u", u, word, lbl, hangman_label, root))
    v = tk.Button(root, text=" V ", command=lambda: choice("v", v, word, lbl, hangman_label, root))
    w = tk.Button(root, text=" W ", command=lambda: choice("w", w, word, lbl, hangman_label, root))
    x = tk.Button(root, text=" X ", command=lambda: choice("x", x, word, lbl, hangman_label, root))
    y = tk.Button(root, text=" Y ", command=lambda: choice("y", y, word, lbl, hangman_label, root))
    z = tk.Button(root, text=" Z ", command=lambda: choice("z", z, word, lbl, hangman_label, root))
    a.grid(row=10, column=10), root
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