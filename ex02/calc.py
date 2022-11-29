import tkinter as tk

calc =tk.Tk()
calc.geometry("300x500")

r=3
c=3
for n in range(9,-1,-1):
    btn = tk.Button(calc, text=f"{n}", width=4, height=2, font=("",30))
    btn.grid(row=(9-n)//3,column=(9-n)%3)
calc.mainloop()