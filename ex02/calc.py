import tkinter as tk
# import tkinter.messagebox as tkm

calc =tk.Tk()
calc.geometry("400x420")

# テキスト入力欄
entry=tk.Entry(calc,justify="right", width=10, font=("",40))
entry.grid(columnspan=3)

# 計算のために書式を整えるところ([=]で呼び出す)
def fml_replace(fml):
    fml = fml.replace("^","**")
    fml = fml.replace("×","*")
    fml = fml.replace("÷","/")
    return fml

def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "CE":
        entry.delete(0,tk.END)
    elif txt == "C":
        entry.delete(len(entry.get())-2,tk.END)
    elif txt == "←":
        entry.delete(len(entry.get())-1,tk.END)
    elif txt == "=":
        fml = entry.get()
        fml = fml_replace(fml)
        res = eval(fml)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        if txt == "x^y":
            txt = "^"
        entry.insert(tk.END, txt)

# 数字ボタン
for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=1, font=("",30))
    btn.bind("<1>", btn_click)
    if n==0:
        btn.grid(row=((9-n)//3)+2,column=1)
    else:
        btn.grid(row=((9-n)//3)+2,column=2-((9-n)%3))

# [←]ボタン
btn = tk.Button(calc, text=f"←", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=0,column=3)

# [C]ボタン
btn = tk.Button(calc, text=f"C", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=1,column=2)

# [CE]ボタン
btn = tk.Button(calc, text=f"CE", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=1,column=1)

# [x^y]ボタン
btn = tk.Button(calc, text=f"x^y", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=1,column=0)

# [+]ボタン
btn = tk.Button(calc, text=f"+", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=4,column=3)

# [-]ボタン
btn = tk.Button(calc, text=f"-", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=3,column=3)

# [×]ボタン
btn = tk.Button(calc, text=f"×", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=2,column=3)

# [÷]ボタン
btn = tk.Button(calc, text=f"÷", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=1,column=3)

# [00]ボタン
btn = tk.Button(calc, text=f"00", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=5,column=0)

# [.]ボタン
btn = tk.Button(calc, text=f".", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=5,column=2)

# [=]ボタン
btn = tk.Button(calc, text=f"=", width=4, height=1, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=5,column=3)

calc.mainloop()