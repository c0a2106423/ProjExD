from operator import not_
import tkinter as tk
import tkinter.messagebox as tkm
import math
import re


#buttonに呼ばれる
#button_click関数
def button_click(event):
    #print(event)
    btn = event.widget  #event引数から、呼んだボタンを特定
    txt = btn["text"]   #特定した buttonのtext をtxtに代入
    if txt=="=":    #=が押されたら
        result=eval(entry.get())    #枠内の値を計算した文字列を生成し
        entry.delete(0, tk.END)     #すでに入力されている文字列を消してから
        entry.insert(tk.END, result)    #作った文字列を入れる
    elif txt =="%": #%ボタンが押されたら    
        result=str(eval(entry.get())*100)+"%"   #枠内の値を100倍して%を末尾に足した文字列を作り
        entry.delete(0, tk.END) #すでに入力されている文字列を消してから
        entry.insert(tk.END, result)    #作った文字列を入れる
    elif txt =="CE":       #CEボタンが押されたら
        entry.delete(0, tk.END) #枠内の文字を全て消す
    elif txt =="C": #未実装につき、未完成
        string=entry.get()
        i = len(string)
        while True:
            i-=1
            if not re.match('(\d+).',string[int('-'+str(i))]):
                entry.delete(i,i+1)
                break 
            else:
                entry.delete(i,i+1) 
    
    elif txt =="BG":    #BGボタンが押されたら、
        string=entry.get()  #文字列を取得し、
        i = len(string)     #文字列の長さを得て
        entry.delete(i-1,tk.END)#最後の文字を消す
    else:   #それ以外の場合（数字ボタンが押された場合）は
        """if txt=="0" or txt=="00":
            check=entry.get()
            if not re.match('(\d+).',check[-1]):
                print("SKIP!")
                return"""
        entry.insert(tk.END,txt)    #文字列の末尾に押されたボタンの値を追加する

def cursor_enter_cell(event):   #セルにカーソルが入ったとき
    cell = event.widget #セルを指定して
    cell["bg"] = "red"  #地色を赤にして
    cell["fg"] = "white"    #文字を白色にする

def cursor_leave_cell(event):   #セルからカーソルが出たとき 
    cell = event.widget #セルを指定して
    cell["bg"] = "#EEE" #地色をうすい灰色にして
    cell["fg"] = "black"    #文字を黒色にする

def button_array(start_r, start_c, max_c, list): #ボタンを追加する関数
    r = start_r
    c = start_c
    for i in list:  #授業内で使われていたfor文そのもの
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
        button.bind("<Enter>", cursor_enter_cell, "+")#セルにカーソルが入ったときcursor_enter_cell関数を呼ぶ
        button.bind("<Leave>", cursor_leave_cell, "+")#セルからカーソルが出たときcursor_leave_cell関数を呼ぶ
        button.grid(row=r, column=c)#ボタンを追加
        c+=1

if __name__ == "__main__":
    button_width = 4    #ボタンの幅
    button_height = 1   #ボタンの高さ
    root = tk.Tk()
    root.title("tk")
    #root.geometry("300x580")
    
    entry = tk.Entry(root,                      #最上部の表示窓の追加
                     justify="right",
                     width=10,
                     font=("Times New Roman",40)
                    )
    #entry.bind()
    entry.grid(row=0, column=0, columnspan=button_width)

    button_top_list = ("%", "CE", "BG", "=")    #上部に追加するボタンのリスト
    button_left_list = ("/","*","-","+")        #左部に追加するボタンのリスト
    start_row=1
    add_row = math.ceil(len(button_top_list)/4) #top_listで追加された分、他のリストの開始行数をずらす
    button_main_list = [i for i in range(9,-1,-1)] 
    button_main_list.append("00")
    button_main_list.append(".")

    r = start_row
    c = 0
    max_c = 4 #許される最大列数
    button_array(r,c,max_c,button_top_list)#上部追加ボタンの追加

    r = start_row+add_row
    max_c=3 #許される最大列数
    button_array(r,c,max_c,button_main_list)#数字ボタン他の追加

    r -=1   #
    c = 3   #
    button_array(r,c,max_c,button_left_list)#左側追加ボタンの追加

    root.mainloop()
