import tkinter as tk
# import tkinter.messagebox as tkm

calc =tk.Tk()
calc.geometry("300x500")

entry=tk.Entry(calc,justify="right", width=10, font=("",40))
entry.grid(columnspan=3)

def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=":
        fml = entry.get()
        res = eval(fml)
        entry.delete(0,tk.END)
        entry.insert(tk.END,res)
    else:
        entry.insert(tk.END, txt)


for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=2, font=("",30))
    btn.bind("<1>", btn_click)
    btn.grid(row=((9-n)//3)+1,column=(9-n)%3)

btn = tk.Button(calc, text=f"+", width=4, height=2, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=4,column=1)

btn = tk.Button(calc, text=f"=", width=4, height=2, font=("",30))
btn.bind("<1>", btn_click)
btn.grid(row=4,column=2)

calc.mainloop()