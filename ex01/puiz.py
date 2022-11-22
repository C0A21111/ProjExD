import random
import datetime

def shutudai():
    print("問題：")
    quiz = random.choice(qa_lst)
    print(quiz["q"])
    return quiz
    

def kaitou(quiz):
    st = datetime.datetime.now()
    user_ans = input("答えるんだ：")
    ed = datetime.datetime.now()
    if user_ans in quiz["a"]:
        print("正解！！！")
    else:
        print("出直してこい")
    print(f"所要時間: {(ed-st).seconds}秒")


if __name__ == "__main__":
    qa_lst = [{"q":"サザエの旦那の名前は？","a":["マスオ","ますお"]},
            {"q":"カツオの妹の名前は？","a":["ワカメ","わかめ"]},
            {"q":"タラオはカツオから見てどんな関係？","a":["甥","おい","甥っ子","おいっこ"],}]

    quiz = shutudai()
    kaitou(quiz)
