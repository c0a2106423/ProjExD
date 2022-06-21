from operator import not_
import tkinter as tk
import tkinter.messagebox as tkm
import math
import re

button_width = 4
button_height = 1
#buttonに呼ばれる
#button_click関数
def button_click(event):
    print(event)
    btn = event.widget  #event引数から、呼んだボタンのインスタンスを特定
    txt = btn["text"]   #特定した buttonのtext をtxtに代入
    if txt=="=":
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif txt =="%":
        result=str(eval(entry.get())*100)+"%"
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif txt =="CE":
        entry.delete(0, tk.END)
    
    elif txt =="C":
        string=entry.get()
        i = len(string)
        while True:
            i-=1
            if not re.match('(\d+).',string[int('-'+str(i))]):
                entry.delete(i,i+1)
                break 
            else:
                entry.delete(i,i+1)
    
    elif txt =="BG":
        string=entry.get()
        i = len(string)-1
        entry.delete(i,i+1)
    else:
        """if txt=="0" or txt=="00":
            check=entry.get()
            if not re.match('(\d+).',check[-1]):
                print("SKIP!")
                return"""
        entry.insert(tk.END,txt)

def cursor_enter_cell(event):
    cell = event.widget
    cell["bg"] = "red"
    cell["fg"] = "white"

def cursor_leave_cell(event):
    cell = event.widget
    cell["bg"] = "#EEE"
    cell["fg"] = "black"

def button_array(start_r, start_c, max_c, list):
    r = start_r
    c = start_c
    for i in list:
        if c >= max_c:
            c = start_c
            r +=1
        button = tk.Button(root,
                           text=str(i), 
                           width=button_width,
                           height=button_height,
                           font=("Times New Roman", 30),
                           command=button_click
                          )
        button.bind("<1>", button_click) #左クリック時にbutton_click関数を呼ぶ
        button.bind("<Enter>", cursor_enter_cell, "+")
        button.bind("<Leave>", cursor_leave_cell, "+")
        button.grid(row=r, column=c)
        c+=1

if __name__ == "__main__":
    root = tk.Tk()
    root.title("tk")
    #root.geometry("300x580")
    
    entry = tk.Entry(root,
                       justify="right",
                       width=10,
                       font=("Times New Roman",40)
                      )
    entry.bind()
    entry.grid(row=0, column=0, columnspan=3)

    button_top_list = ("%", "CE", "BG", "=")
    button_left_list = ("/","*","-","+")
    start_row=1
    add_row = math.ceil(len(button_top_list)/4)
    button_main_list = [i for i in range(9,-1,-1)]
    button_main_list.append("00")
    button_main_list.append(".")

    r = start_row
    c = 0
    max_c = 4
    button_array(r,c,max_c,button_top_list)

    r = start_row+add_row
    max_c=3
    button_array(r,c,max_c,button_main_list)

    r -=1
    c = 3
    button_array(r,c,max_c,button_left_list)

    root.mainloop()
