from itertools import count
import random
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def main():
    global root, canvas, koukaton, mx, my, cx, cy, key, map
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

    goal_p = goal_p()

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

def goal_p():
    global map, canvas
    height = len(map)
    #width = len(map[-2])
    end_p=[]
    for i in range(0, height):
        #print(map[i][-2])
        if not map[i][-2]:
            if map[i][-3] + map[i-1][-2] + map[i+1][-2] == 2:
                end_p.append(i)
    #print(end_p)
    if end_p:
        i = random.randint(0,len(end_p))
        x = end_p[i]
    else:
        for i in range(len(map)):
            if not map[i][-2]:
                x = i
        else:
            for i in range(len(map)):
                if not map[i][-3]:
                    x = i
    y = len(map[-2])-2
    #print(x, y)
    canvas.create_rectangle(y*100, x*100, y*100+100, x*100+100, 
                            fill="red")
    return(x, y)

def goal():
    global root
    root.destroy

def main_proc():
    global canvas, mx, my, cx, cy, key, map
    if key == "Up":
        my -= 1
        tag = [0, 1]
    if key == "Down":
        my += 1
        tag = [0, -1]
    if key == "Left":
        mx -= 1
        tag = [1, 0]
    if key == "Right":
        mx += 1
        tag = [-1, 0]
    cx = mx*100 + 50
    cy = my*100 + 50
    if not map[my][mx]:
        canvas.coords("koukaton", cx, cy)
    else:
        mx += tag[0]
        my += tag[1]
    root.after(100, main_proc)

if __name__ == "__main__":
    main()
