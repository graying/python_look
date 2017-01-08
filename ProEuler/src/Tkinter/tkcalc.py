import Tkinter


def frame(root, side):
    w = Tkinter.Frame(root)
    w.pack(side=side, expand="yes", fill="both")

    return w


def button(root, side, text, command=None):
    button = Tkinter.Button(root, text=text, command=command)
    button.pack(side=side, expand="yes", fill="both")

    return button


class Calculator(Tkinter.Frame):
    def __init__(self):
        Tkinter.Frame.__init__(self)

        self.pack(expand="yes", fill="both")
        self.master.title("Calc")
        self.master.iconname("Calc")

        display = Tkinter.StringVar()

        entry = Tkinter.Entry(self, relief="sunken", textvariable=display)
        entry.pack(side="top", expand="yes", fill="both")

        for key in ["123", "456", "789", "-0."]:
            keyF = frame(self, "top")
            for char in key:
                but = button(keyF, "left", char, lambda w=display, s="%s" % char: w.set(w.get() + s))

        osp = frame(self, "top")
        for char in "+-*/=":
            if "=" == char:
                btn = button(osp, "left", char)
                btn.bind("<ButtonRelease-1>", lambda e, s=self, w=display: s.calc(w), "+")

            else:
                btn = button(osp, "left", char, lambda w=display, c=char: w.set(w.get() + " " + c + " "))

        clearF = frame(self, "bottom")
        button(clearF, "left", "Clear", lambda w=display: w.set(""))

    def calc(self, display):
        try:
            v = eval(display.get())
            display.set(v)
        except ValueError:
            display.set("ERROR")


if "__main__" == __name__:
    Calculator().mainloop()
