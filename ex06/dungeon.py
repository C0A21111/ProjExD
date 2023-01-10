
import sys
import time
from pprint import pprint 

import pygame as pg

import dungeon_maker as dm

MAIN_FLOOR_LEN = 3
SUB_FLOOR_LEN = 3
SCREEN_W = 1550
SCREEN_H = 950
MAZE_W = 31
MAZE_H = 19
CELL_SIZE = 50
PLAYER_RATIO = 0.5


class Screen:
    def __init__(self, title, wh):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        # 背景画像を貼り付ける場合のコード
        # self.bgi_sfc = pg.image.load(image_path)
        # self.bgi_rct = self.sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Player:
    key_delta = {
        pg.K_UP:    ([0, -1], 6),
        pg.K_DOWN:  ([0, +1], 3),
        pg.K_LEFT:  ([-1, 0], 5),
        pg.K_RIGHT: ([+1, 0], 2),
    }

    def __init__(self, image_path, ratio, xy):
        self.pos_xy = [1,1]
        self.sfc = pg.image.load(image_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, screen):
        screen.sfc.blit(self.sfc, self.rct)

    def update(self, screen, maze_lst):
        key_dct = pg.key.get_pressed()
        for key, delta in Player.key_delta.items():
            if key_dct[key]:
                kari_x = self.pos_xy[0] + delta[0][0]
                kari_y = self.pos_xy[1] + delta[0][1]
                if check_wall(kari_x, kari_y, maze_lst):
                    self.pos_xy[0] = kari_x
                    self.pos_xy[1] = kari_y
                    self.rct.center = (self.pos_xy[0]*CELL_SIZE+(CELL_SIZE/2), self.pos_xy[1]*CELL_SIZE+(CELL_SIZE/2))
                self.sfc = pg.image.load(f"fig/{delta[1]}.png")
                self.sfc = pg.transform.rotozoom(self.sfc, 0, PLAYER_RATIO)
        self.blit(screen)
    pass


def show_dungeon(screen, maze_lst, clr):
    color = [clr[0], clr[1],"#765c47"]
    for x in range(len(maze_lst)):
        for y in range(len(maze_lst[x])):
            if x==1 and y==1:
                pg.draw.rect(screen, "#a0d8ef", [x*CELL_SIZE, y*CELL_SIZE, (x+1)*CELL_SIZE, (y+1)*CELL_SIZE])
            elif x==(len(maze_lst)-2) and y==(len(maze_lst[x])-2):
                pg.draw.rect(screen, "#f4b3c2", [x*CELL_SIZE, y*CELL_SIZE, (x+1)*CELL_SIZE, (y+1)*CELL_SIZE])
            else:
                pg.draw.rect(screen, color[maze_lst[x][y]], [x*CELL_SIZE, y*CELL_SIZE, (x+1)*CELL_SIZE, (y+1)*CELL_SIZE])


def check_wall(x, y, maze_lst):
    return (not maze_lst[x][y]==1)


def game_play_sub(floor, sub_lst, screen):
    clock = pg.time.Clock()
    sub_player = Player(f"fig/0.png", PLAYER_RATIO, (CELL_SIZE*1.5,CELL_SIZE*1.5))
    sub_player.blit(screen)
    mount_floor_map = sub_lst.pop()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        show_dungeon(screen.sfc, mount_floor_map, ("#3f312b","#765c47"))
        sub_player.update(screen, mount_floor_map)

        fonto = pg.font.Font(None,58)
        txt = fonto.render(f"Floor: {floor}-UnderGround", True, "#fff1cf")
        screen.sfc.blit(txt, (30, 6))

        pg.display.update()

        if sub_player.pos_xy == [MAZE_W-2, MAZE_H-2]:
            fonto = pg.font.Font(None,120)
            txt = fonto.render(f"back main", True, "#fff1cf")
            screen.sfc.blit(txt, (450, 450))
            pg.display.update()
            time.sleep(1)
            return

        clock.tick(10)


def game_play_main(floor, maze_lst):
    clock = pg.time.Clock()
    screen = Screen("duneon", (SCREEN_W,SCREEN_H))
    player = Player(f"fig/0.png", PLAYER_RATIO, (CELL_SIZE*1.5,CELL_SIZE*1.5))
    player.blit(screen)
    playing = True
    mount_floor_map = maze_lst[0]

    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        
        show_dungeon(screen.sfc, mount_floor_map, ("#fff1cf", "#b0ca71"))
        player.update(screen, mount_floor_map)

        fonto = pg.font.Font(None,58)
        txt = fonto.render(f"Floor: {floor}", True, "#3f312b")
        screen.sfc.blit(txt, (30, 6))

        pg.display.update()

        if player.pos_xy == [MAZE_W-2, MAZE_H-2]:
            playing = False
            fonto = pg.font.Font(None,120)
            if floor == MAIN_FLOOR_LEN:
                txt = fonto.render(f"STAGE ALL CLEAR!!", True, "RED")
                t = 7
                screen.sfc.blit(txt, (400, 450))
            else:
                txt = fonto.render(f"STAGE {floor} CLEAR!!", True, "RED")
                t = 3
                screen.sfc.blit(txt, (450, 450))
            pg.display.update()
            time.sleep(t)
            return
        if mount_floor_map[player.pos_xy[0]][player.pos_xy[1]] == 2:
            mount_floor_map[player.pos_xy[0]][player.pos_xy[1]] = 0
            fonto = pg.font.Font(None,120)
            txt = fonto.render(f"to sub", True, "#3f312b")
            screen.sfc.blit(txt, (450, 450))
            pg.display.update()
            time.sleep(1)
            game_play_sub(floor, (maze_lst[1:]), screen)

        clock.tick(10)


def main():
    global all_maze_lst

    all_maze_lst = [[dm.make_dungeon(MAZE_W,MAZE_H,SUB_FLOOR_LEN, i) for i in range(SUB_FLOOR_LEN+1)] for j in range(MAIN_FLOOR_LEN)]

    for i in range(MAIN_FLOOR_LEN):
        floor = i+1
        game_play_main(floor, all_maze_lst[i])


if __name__ == "__main__":
    pg.init()
    
    main()

    pg.quit()
    sys.exit()