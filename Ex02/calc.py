import tkinter as tk
import tkinter.messagebox as tkm

#buttonに呼ばれる
#button_click関数
def button_click(event):
    btn = event.widget  #event引数から、呼んだボタンのインスタンスを特定
    txt = btn["text"]   #特定した buttonのtext をtxtに代入
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

#main関数
def main():
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x500")

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
            button.grid()
            #print(num)
            button.grid(row=i, column=j)

    root.mainloop()

if __name__ == "__main__":
    main()
