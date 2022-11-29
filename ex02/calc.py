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

def mk_btn(btn_txt,x,y):
    btn = tk.Button(calc, text=btn_txt, width=4, height=1, font=("",30))
    btn.bind("<1>", btn_click)
    btn.grid(row=x,column=y)

# 数字ボタン
for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=1, font=("",30))
    btn.bind("<1>", btn_click)
    if n==0:
        btn.grid(row=((9-n)//3)+2,column=1)
    else:
        btn.grid(row=((9-n)//3)+2,column=2-((9-n)%3))

# [←]ボタン
mk_btn("←",0,3)

# [x^y]ボタン
mk_btn("x^y",1,0)

# [CE]ボタン
mk_btn("CE",1,1)

# [C]ボタン
mk_btn("C",1,2)

# [+]ボタン
mk_btn("+",4,3)

# [-]ボタン
mk_btn("-",3,3)

# [×]ボタン
mk_btn("×",2,3)

# [÷]ボタン
mk_btn("÷",1,3)

# [00]ボタン
mk_btn("00",5,0)

# [.]ボタン
mk_btn(".",5,2)

# [=]ボタン
mk_btn("=",5,3)

calc.mainloop()