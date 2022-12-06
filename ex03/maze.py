import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""

def main_proc():
    global mx,my
    if key=="Up":
        my -= 1
    if key=="Down":
        my += 1
    if key=="Left":
        mx -= 1
    if key=="Right":
        mx += 1
    canvas.coords("kktn0",mx*100+50,my*100+50)
    root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    image = tk.PhotoImage(file="fig/0.png")
    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    mx = 1
    my = 1
    cx = mx*100
    cy = my*100
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)
    canvas.create_image(cx+50,cy+50,image=image,tag="kktn0")
    canvas.pack()

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()