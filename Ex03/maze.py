import tkinter as tk
import tkinter.messagebox as tkm
from turtle import width
import maze_maker

def main():
    global root, canvas, koukaton, mx, my, key, map
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
    mx, my = 1,1
    cx, cy = mx*100+50, my*100+50
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
    global canvas, mx, my, cx, cy, key, map
    if key == "Up":
        my -= 1
    if key == "Down":
        my += 1
    if key == "Left":
        mx -= 1
    if key == "Right":
        mx += 1
    cx = mx*100 + 50
    cy = my*100 + 50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    main()
