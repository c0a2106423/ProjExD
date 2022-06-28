from cProfile import label
from http.client import ImproperConnectionState
from time import sleep
import tkinter as tk
import tkinter.messagebox as tkm

from setuptools import Command

def count_up():
    global tmr , jid
    tmr += 1
    label["text"] = tmr
    jid = root.after(1000, count_up)

def key_down(event):
    global jid
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    #Key = event.keysym
    #tkm.showinfo("検知",F"{Key}キーが押されました")
    root.after(1000, count_up())

if __name__ == "__main__":
    root = tk.Tk()
    label = tk.Label(
                     root,
                     font=("Times New Roman", 80),
                     text="Hello!",             
                    )
    tmr = 0
    jid = None
    label.pack()
    
    #root.after(100, count_up())
    root.bind("<KeyPress>", key_down)
    root.mainloop()
