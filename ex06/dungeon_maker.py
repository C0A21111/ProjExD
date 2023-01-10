import random
import pygame as pg

def make_dungeon(yoko, tate,sub,n):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = [[1 for i in range(tate)] for j in range(yoko)]  #大きさがtate*yokoの「1」の2次元リスト
    for maze_yoko in range(1, len(maze_lst)-1): #壁ではない部分を0にする
        for cell in range(1, len(maze_lst[0])-1):
            maze_lst[maze_yoko][cell] = 0
    for y in range(2, tate-2, 2): #迷路を作る
        for x in range(2, yoko-2, 2):
            maze_lst[x][y] = 1
            if x > 2:
                rnd = random.randint(0, 2)
            else:
                rnd = random.randint(0, 3)
            maze_lst[x+YP[rnd]][y+XP[rnd]] = 1

    if n == 0:
        stairs = 0
        while (stairs<sub):
            x,y = random.randint(0,yoko-1),random.randint(0,tate-1)
            if x!=1 and y!=1:
                if  x!=(yoko-2) and y!=tate-2:
                    if maze_lst[x][y] == 0 or maze_lst[x][y] == 2:
                        maze_lst[x][y] = 2
                        stairs += 1

    return maze_lst

def print_dungeon(maze_lst):
    maze_lst = [list(x) for x in zip(*maze_lst)]
    for i in maze_lst:
        for j in i:
            if j == 1:
                j = "■"
            elif j == 2:
                j = "O"
            else:
                j = "□"
            print(j,end="")
        print()
