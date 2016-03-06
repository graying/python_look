import tkinter as tk
    
master = tk.Tk()
whateveryoudo = '''Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)'''

msg = tk.Message(master, text = whateveryoudo)
msg.config(bg='light green', font = 'times 48 italic')
msg.pack()

x=800
def expand_msg():
    global msg
    global master
    global x
    x += 15
    XY='{0}x500'.format(x)
    master.geometry(XY)
    msg.config(bg="blue")
    msg.pack()

btn = tk.Button(master, text="Expand", command=expand_msg).pack()

master.mainloop()