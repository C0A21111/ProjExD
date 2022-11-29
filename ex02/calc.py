import tkinter as tk
import tkinter.messagebox as tkm

calc =tk.Tk()
calc.geometry("300x500")

def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}のボタンが押されました")

for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=2, font=("",30))
    btn.bind("<1>", btn_click)
    btn.grid(row=(9-n)//3,column=(9-n)%3)
calc.mainloop()