import tkinter as tk
import tkinter.messagebox as tkm

def main():
    global root, koukaton, cx, cy
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

    root.mainloop()    

if __name__ == "__main__":
    main()
