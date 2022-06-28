
import random
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker

def main(): #メイン部分の中身
    global root, canvas, koukaton, mx, my, cx, cy, key, map, goal_pos
    width = 1500
    height = 900
    key = ""
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    #initialization() #未完成なので未実装

    canvas = tk.Canvas(
                       root,
                       width=width,
                       height=height,
                       bg="black"
                      )
    canvas.pack()

    map = maze_maker.make_maze(width//100, height//100) #一マス100pxになるように調整
    maze_maker.show_maze(canvas, map) 

    goal_pos = goal_p() # ゴール座標を設定しそのマスを赤く上書きする関数を呼ぶ  戻り値はゴール座標
    #print(goal_pos)

    koukaton = tk.PhotoImage(file = "fig/5.png")
    mx, my = 1,1

    start_p(mx, my) #スタート座標をmx, myから設定し、ライム色で上書きする関数を呼ぶ 引数はmx,my

    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    root.after(10, main_proc)
    root.mainloop() #main()終わり

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

def start_p(x, y): #渡された座標から
    canvas.create_rectangle(y*100, x*100, y*100+100, x*100+100, 
                            fill="lime") #その座標をライム色の四角形で上書きする

def goal_p(): #
    global map, canvas
    height = len(map) #高さを取得
    #width = len(map[-2])
    end_p=[] #ゴール候補のy座標のリスト
    for i in range(0, height):
        #print(map[i][-2])
        if not map[i][-2]: #そのマスが床なら
            if map[i][-3] + map[i-1][-2] + map[i+1][-2] == 2: #かつ、右側を除く3方のうち、2方が壁なら
                end_p.append(i) # 候補リストに追加
    #print(end_p)
    if len(end_p): #候補が一つでもあれば
        i = random.randint(0,len(end_p)-1) #リストのインデックスをランダムに選び
        #print(i)
        y = end_p[i] # y に代入
    else: #候補がない場合
        for i in range(height): #とりあえず右端から２列目の床のマスにゴールを設定
            if not map[i][-2]:
                y = i
    x = len(map[-2])-2 #x座標を設定
    #print(x, y)
    canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                            fill="red") #ゴールマスを赤色にする
    return(x, y) #設定した座標を返す

def goal(): #ゴールマスに付いたら
    global root
    tkm.showinfo("通知", "ゴールです！おめでとう！\nOKボタンを押してプログラムを終了")
    root.destroy() #rootのmainroopを殺してプログラムを最後まで終える

def main_proc():
    global canvas, mx, my, cx, cy, key, map, goal_pos
    if key == "Up"    and map[my-1][mx]==0: my-=1
    if key == "Down"  and map[my+1][mx]==0: my+=1
    if key == "Left"  and map[my][mx-1]==0: mx-=1
    if key == "Right" and map[my][mx+1]==0: mx+=1
    cx = mx*100 + 50
    cy = my*100 + 50
    canvas.coords("koukaton", cx, cy)
    if (mx, my) == goal_pos: #現在座標がゴール座標と同一ならば
        goal() #ゴール時の処理をする関数を呼ぶ
    root.after(100, main_proc)

"""
def initialization(): # 各種設定値を変更できるよう試みた残骸
    global init, init_width, init_height, init_w_cell, init_h_cell
    init = tk.Tk()
    init.title("設定")
    label = tk.Label(root,
                    text = "横幅"
                    )
    label.grid(row=0,column=0)
    width_box = tk.Entry()
    width_box.grid(row=0, column=1, columnspan=2)
    btn = tk.Button(init, text="確定", command=init_enter())
    btn.grid(row=2, column=2, columnspan=3)
    init.mainloop()

def init_enter():
    global init
    #init.destroy()
"""

if __name__ == "__main__":
    main()
