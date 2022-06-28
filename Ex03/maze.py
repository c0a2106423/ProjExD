import tkinter as tk
import tkinter.messagebox as tkm
from turtle import width
import maze_maker

def main():
    global root, canvas, koukaton, cx, cy, key
    width = 1500
    height = 900
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(
                       root,
                       width=width,
                       height=height,
                       bg="black"
                      )
    canvas.pack()

    map = maze_maker.make_maze(width//100, height//100)
    maze_maker.show_maze(canvas, map)

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
    if key == "Down":
        cy += 20
    if key == "Left":
        cx -= 20
    if key == "Right":
        cx += 20
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    main()
