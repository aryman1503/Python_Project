from Tkinter import *
#from Tkinter import filedialog

window = Tk()

def callback(event):
    print(event.x,event.y)
    c.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="#558835")

def draw(event):
    print(event.x, event.y)
    c.create_oval(event.x - 5, event.y - 5, event.x + 5, event.y + 5, fill="#000000")



window.title("Paint")

c = Canvas(window, width=400, height=400)
c.pack()
c.bind("<Button-1>",callback)
c.bind("<B1-Motion>",draw)



window.mainloop()