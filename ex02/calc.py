import tkinter as tk

# ウィンドウインスタンス生成
calc =tk.Tk()
calc.geometry("400x420")

# 計算のために書式を整えるところ([=]で呼び出す)
def fml_replace(fml):
    fml = fml.replace("^","**")
    fml = fml.replace("×","*")
    fml = fml.replace("÷","/")
    return fml

# ボタンクリック時のイベント
def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "CE":
        entry.delete(0,tk.END)
    elif txt == "C":
        entry.delete(len(entry.get())-3,tk.END)
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

# ボタンを実装する関数
def mk_btn(btn_txt,x,y):
    btn = tk.Button(calc, text=btn_txt, width=4, height=1, font=("",30))
    btn.bind("<1>", btn_click)
    btn.grid(row=x,column=y)

# ボタンのリスト（配列）
btn_txts = [["entry", None, None,"←"],
            ["x^y", "CE", "C", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["00", "0", ".", "="]]

# ボタンの作成
for i in range(6):
    for j in range(4):
        if btn_txts[i][j]=="entry":
            # テキスト入力欄
            entry=tk.Entry(calc,justify="right", width=10, font=("",40))
            entry.grid(columnspan=3)
        elif not btn_txts[i][j]:
            continue
        else:
            mk_btn(btn_txts[i][j],i,j)

calc.mainloop()