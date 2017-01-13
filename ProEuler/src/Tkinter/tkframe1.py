from Tkinter import *

root = Tk()
top = Frame(root)
top.pack(side='top')

def quit(event=None):
    root.destroy()

quit_button = Button(top, text='Goodbye, GUI World!', command=quit,background='yellow', foreground='blue')
quit_button.pack(side='top', pady=5, fill='x')

root.mainloop()
