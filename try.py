import tkinter as tk
import tkinter.messagebox as tkm

root=tk.Tk()
root.title("tk")

def button_click(event):
    btn=event.widget
    num=btn["text"]
    if num=="=":
        res=entry.get()
        ans=eval(res)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans) 
    #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    else:
        entry.insert(tk.END, num)

entry=tk.Entry(root,
                width=10,justify="right",
                font=("Times New Roman",40))
entry.grid(row=0,column=0,columnspan=3)
    
r=1
c=0
for i,num in enumerate([9,8,7,6,5,4,3,2,1,0,"=","+","-","*","/","**"]):
    button=tk.Button(root,text=f"{num}",
                    font=("Times New Roman", 30),
                    width=4,height=2)
    button.bind("<1>", button_click)
    button.grid(row=r,column=c)
    c+=1
    if (i+1)%4==0:
        r+=1
        c=0
root.mainloop()