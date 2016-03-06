#!/usr/bin/python3

from tkinter import *

myroot = Tk()
Label(myroot, text="Red Text in Times font",
      fg="red",
      font = "times").pack()
      
Label(myroot, text = "green text Helvetica font",
      fg = "light green",
      bg = "dark green",
      font = "Helvetica 12 bold italic").pack()

Label(myroot, text = "Blue text in Verdana bold",
      fg = "blue",
      bg = "yellow",
      font = "Verdana 12 bold").pack()

myroot.mainloop()