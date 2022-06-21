import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

def main():
    root = tk.Tk()
    root.title("tk")
    root.geometry("300x500")

    for i in range(4):
        for j in range(3):
            num = 9-(3*i)-(j)
            if num<0 :
                break
            button = tk.Button(root,
                            text=num, 
                            font=("Times New Roman", 30),
                            command=button_click
                            )
            button.bind("<1>", button_click)
            button.grid()
            #print(num)
            button.grid(row=i,column=j)

    root.mainloop()

if __name__ == "__main__":
    main()
