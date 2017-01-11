#!/usr/bin/python3

import os
from Tkinter import *

print os.getcwd()

myroot = Tk()
logo = PhotoImage(file="icon.gif")
w1 = Label(myroot, image=logo)
w1.pack(side="top")
explanation = '''At present, only gif and PPM/PGM
formats are supported, but an interface exists
to allow additional image files formats
to be added easily'''

w2 = Label(myroot,
           justify=CENTER,
           padx=10,
           text=explanation)
w2.pack(side="bottom")

myroot.mainloop()
