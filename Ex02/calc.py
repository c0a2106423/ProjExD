import tkinter as tk
import tkinter.messagebox as tkm


#buttonに呼ばれる
#button_click関数
def button_click(event):
    btn = event.widget  #event引数から、呼んだボタンのインスタンスを特定
    txt = btn["text"]   #特定した buttonのtext をtxtに代入
    if txt=="=":
        result=eval(entry.get())
        print(result)
    else:
        entry.insert(tk.END,txt)

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

    start_row=1
    button_list = [i for i in range(9,-1,-1)]
    button_list.append("+")
    button_list.append("=")

    r = start_row
    c = 0
    max_c = 3

    for i in button_list:
        if c >= max_c:
            c = 0
            r +=1
        button = tk.Button(root,
                           text=str(i), 
                           width=4,
                           height=2,
                           font=("Times New Roman", 30),
                           command=button_click
                          )
        button.bind("<1>", button_click) #左クリック時にbutton_click関数を呼ぶ
        button.grid(row=r, column=c)
        c+=1

    """
    #縦4列
    for i in range(4):
        #横3列
        for j in range(3):
            #ボタンの値
            num = 9-(3*i)-(j)
            #値が0未満の場合、ループを終了
            if num<0 :
                break
            button = tk.Button(root,
                            text=num, 
                            width=4,
                            height=2,
                            font=("Times New Roman", 30),
                            command=button_click
                            )
            button.bind("<1>", button_click) #左クリック時にbutton_click関数を呼ぶ
            #button.grid()
            #print(num)
            button.grid(row=i+start_row, column=j)
    """

    root.mainloop()
