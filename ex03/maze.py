import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm

def reset(event):
    global mx,my,jid,goal
    goal = False
    mx = 1
    my = 1
    tkm.showinfo("リセット", f"位置をリセット:\n初期位置に戻ります。")
    mk_img(img_dic["r"])
    canvas.coords("kktn0",mx*100+50,my*100+50)
    print("reset")
    canvas.pack()
    print("jid:",jid, "\ngoal:",goal)
    if not jid:
        main_proc()

def key_down(event):
    global key
    key = event.keysym
    
def key_up(event):
    global key
    key = ""

def mk_img(kktn_num): #kktn_num --> こうかとんの画像名の番号
    global image
    image = tk.PhotoImage(file=f"fig/{kktn_num}.png")
    canvas.create_image(mx*100+50,my*100+50,image=image,tag="kktn0")

def game_goal():
    global jid,goal
    if not goal:
        goal = True
        res = tkm.askquestion(title="goal!!", message="ゴールしました。リセットしますか？")
        if res=="yes":
            reset("dummy")
        if res=="no":
            tkm.showinfo(title="infomation",message="[r]キーでいつでもリセットできます")

def main_proc():
    global mx,my,image,jid,goal
    print(mx,my)
    if mx==13 and my==7:
        root.after_cancel(jid)
        jid = None
        game_goal()
    if not key=="":
        if key=="Up"    and maze_lst[mx][my-1]==0: my -= 1
        if key=="Down"  and maze_lst[mx][my+1]==0: my += 1
        if key=="Left"  and maze_lst[mx-1][my]==0: mx -= 1
        if key=="Right" and maze_lst[mx+1][my]==0: mx += 1
        mk_img(img_dic[key])
    canvas.coords("kktn0",mx*100+50,my*100+50)
    jid = root.after(100,main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    img_dic = {"r":0,"Up":6,"Down":3,"Left":5,"Right":2}
    goal = False

    canvas = tk.Canvas(width=1500,height=900,bg="#000000")
    mx = 1
    my = 1
    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)
    mk_img(0)
    canvas.pack()

    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    root.bind("r",reset)

    jid = None
    main_proc()

    root.mainloop()