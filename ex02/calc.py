import tkinter as tk
# import tkinter.messagebox as tkm

calc =tk.Tk()
calc.geometry("400x420")

# テキスト入力欄
entry=tk.Entry(calc,justify="right", width=10, font=("",40))
entry.grid(columnspan=3)

def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        fml = entry.get()
        fml = fml.replace("^","**")
        res = eval(fml)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END, txt)

# 数字ボタン
for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=1, font=("",30))
    btn.bind("<1>", btn_click)
    if n==0:
        btn.grid(row=((9-n)//3)+2,column=((9-n)%3))
    else:
        btn.grid(row=((9-n)//3)+2,column=2-((9-n)%3))



# [^]ボタン
btn = tk.Button(calc, text=f"x^y", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=1,column=0)

# [+]ボタン
btn = tk.Button(calc, text=f"+", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=5,column=1)

# [=]ボタン
btn = tk.Button(calc, text=f"=", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=5,column=2)

calc.mainloop()