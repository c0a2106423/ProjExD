import re
import tkinter as tk
import tkinter.messagebox as tkm

def main():
    global root, koukaton, cx, cy, key
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
    root.mainloop()    

def key_down(event):
    global key
    key = event.keysym
    print(key)
    return

def key_up(event):
    global key
    key = ""
    print(key)
    return



if __name__ == "__main__":
    main()
