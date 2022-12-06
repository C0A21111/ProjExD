import tkinter as tk

def key_down(event):
    global key
    key = event.keysym
    
def key_up():
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    image = tk.PhotoImage(file="fig/0.png")

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    cx = 300
    cy = 400
    canvas.create_image(cx,cy,image=image,tag="kktn0")
    canvas.pack()

    key = ""

    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    root.mainloop()