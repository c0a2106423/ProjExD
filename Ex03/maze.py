import tkinter as tk
import tkinter.messagebox as tkm

def main():
    global root, koukaton, cx, cy
    root = tk.Tk()
    root.title("迷えるこうかとん")
    root.geometry("1500x900")
    koukaton = tk.PhotoImage(file="5.png")
    cx, cy = 300, 400
    tk.Canvas.create_image(cx, cy, image=koukaton, tag="koukaton")
    root.mainloop()    

if __name__ == "__main__":
    main()
