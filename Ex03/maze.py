from itertools import groupby
import re
import tkinter as tk
import tkinter.messagebox as tkm
from tokenize import group

def main():
    global root, canvas, koukaton, cx, cy, key
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(
                       root,
                       width=1500,
                       height=900,
                       bg="black"
                      )
    canvas.pack()

    koukaton = tk.PhotoImage(file = "fig/5.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(10, main_proc)
    root.mainloop()

def key_down(event):
    global key
    key = event.keysym
    #print(key)
    return

def key_up(event):
    global key
    key = ""
    #print(key)
    return

def main_proc():
    global canvas, cx, cy, key
    if key == "Up":
        cy -= 20
    elif key == "Down":
        cy += 20
    elif key == "Left":
        cx -= 20
    elif key == "Right":
        cx += 20
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    main()
