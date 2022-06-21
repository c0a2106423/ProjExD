import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning(txt, f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

label = tk.Label(root,
                text = "らべるを書いてみた件",
                font = ("Helvetica", 20)
                )
label.grid(row=0,column=0)

#button = tk.Button(root, text="押すな")
#button.pack()

#canvas = tk.Canvas(root,
#                    width=400,
#                    height=100,
#                    bg="black"
#                    )
#canvas.create_line(0,0,100,100,fill="red",width=1)
#canvas.create_rectangle(102,102,200,0,fill="green",outline="white",width=2)
#canvas.create_polygon(210,0,310,100,fill="blue",outline="green",width=6)
#canvas.pack()

entry = tk.Entry(width=30)
entry.insert(tk.END, "fugofugo")
entry.grid(row=2,column=0)
button = tk.Button(root, text="押すな")
button.bind("<1>", button_click)
button.grid(row=3,column=0)

root.mainloop()