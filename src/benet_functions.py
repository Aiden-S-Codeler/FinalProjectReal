import tkinter as tk
import faker

def hangman():
    root = tk.Tk()
    root.title("Hangman")
    root.minsize(2550, 1375)
    root.maxsize(2550, 1375)
    def decide(num):
        fake = Faker()
        while True:
            word = fake.word()
            if len(word) == num:
                break
        for i in [btn4, btn5, btn6, btn7, btn8]:
            i.delete()
        a = tk.Button(root, text="A", command=choice("a", a, word)).grid(row=4, column=0)
        b = tk.Button(root, text="B", command=choice("b", b, word)).grid(row=4, column=0)
        c = tk.Button(root, text="C", command=choice("c", c, word)).grid(row=4, column=0)
        d = tk.Button(root, text="D", command=choice("d", d, word)).grid(row=4, column=0)
        e = tk.Button(root, text="E", command=choice("e", e, word)).grid(row=4, column=0)
        f = tk.Button(root, text="F", command=choice("f", f, word)).grid(row=4, column=0)
        g = tk.Button(root, text="G", command=choice("g", g, word)).grid(row=4, column=0)
        h = tk.Button(root, text="H", command=choice("h", h, word)).grid(row=4, column=0)
        i = tk.Button(root, text="I", command=choice("i", i, word)).grid(row=4, column=0)
        j = tk.Button(root, text="J", command=choice("j", j, word)).grid(row=4, column=0)
        k = tk.Button(root, text="K", command=choice("k", k, word)).grid(row=4, column=0)
        l = tk.Button(root, text="L", command=choice("l", l, word)).grid(row=4, column=0)
        m = tk.Button(root, text="M", command=choice("m", m, word)).grid(row=4, column=0)
        n = tk.Button(root, text="N", command=choice("n", n, word)).grid(row=4, column=0)
        o = tk.Button(root, text="O", command=choice("o", o, word)).grid(row=4, column=0)
        p = tk.Button(root, text="P", command=choice("p", p, word)).grid(row=4, column=0)
        q = tk.Button(root, text="Q", command=choice("q", q, word)).grid(row=4, column=0)
        r = tk.Button(root, text="R", command=choice("r", r, word)).grid(row=4, column=0)
        s = tk.Button(root, text="S", command=choice("s", s, word)).grid(row=4, column=0)
        t = tk.Button(root, text="T", command=choice("t", t, word)).grid(row=4, column=0)
        u = tk.Button(root, text="U", command=choice("u", u, word)).grid(row=4, column=0)
        v = tk.Button(root, text="V", command=choice("v", v, word)).grid(row=4, column=0)
        w = tk.Button(root, text="W", command=choice("w", w, word)).grid(row=4, column=0)
        x = tk.Button(root, text="X", command=choice("x", x, word)).grid(row=4, column=0)
        y = tk.Button(root, text="Y", command=choice("y", y, word)).grid(row=4, column=0)
        z = tk.Button(root, text="Z", command=choice("z", z, word)).grid(row=4, column=0)
        return word
    def choice(letter, btn, word):
        btn.destroy()
        if letter in word:
            pass
    btn4 = tk.Button(root, text="4", command=decide(4)).grid(row=4, column=0)
    btn5 = tk.Button(root, text="5", command=decide(5)).grid(row=4,column=2)
    btn6 = tk.Button(root, text="6", command=decide(6)).grid(row=4,column=4)
    btn7 = tk.Button(root, text="7", command=decide(7)).grid(row=4,column=6)
    btn8 = tk.Button(root, text="8", command=decide(8)).grid(row=4,column=8)
    lbl = tk.Label(root, text="0")
    lbl.grid(row=5, column=1, columnspan=2)
    close = tk.Button(root, text="Close the program", command=root.destroy).grid(row=10,column=1)
    root.mainloop()

hangman()
