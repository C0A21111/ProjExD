import random
from datetime import datetime

def quiz(n,m):
    alp_lst = [chr(s) for s in range(65,91)]
    chr_q = random.sample(alp_lst,k=n)
    print("対象文字：\n"+" ".join(chr_q))
    lost_q = random.sample(chr_q,k=m)
# 欠損文字テスト
    # print("欠損文字：\n"+" ".join(lost_q))
    for l in lost_q:
        chr_q.remove(l)
    print("表示文字：\n"+" ".join(chr_q))
    return lost_q

def ans(play):
    chr_c_a =input("欠損文字はいくつあるでしょうか？：")

    if chr_c_a == "やめる":
        play = False
        return play
    chr_c_a = int(chr_c_a)

    if not chr_c_a == lostchr_c_q:
        print("不正解です。またチャレンジしてください\n","-"*30)
        return play 




    print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
    lost_a = ["",""]
    for i in range(1,3):
        lost_a[i] = input(f"{i}つ目の文字を入力してください")
        if lost_a[i] == "やめる":
            play = False
            return play

    try:
        for l in lost_a:
            lost_q.remove(l)
    except ValueError:
        print("不正解です。またチャレンジしてください\n","-"*30)
    
    print("正解です。おわり。\n", "-"*30)
    return False
  
if __name__ == "__main__":
    st = datetime.now()

    chr_c = 10
    lostchr_c_q = 2
    maxplay = 5
    play = True

    for i in range(maxplay):
        lost_q = quiz(chr_c,lostchr_c_q)
        play = ans(play)
        if not play:
            print("ゲームを中止しました。\n","-"*30)
            break
    
    ed = datetime.now()
    print(f"【所要時間: {(ed-st).seconds}秒】")