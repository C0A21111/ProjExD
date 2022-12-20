# 標準ライブラリ
import random
import sys

# 拡張モジュール
import pygame as pg


R = 120     # こうかとんの爆弾消去範囲の半径

def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def check_around(kkt, bomb_lst):
    print("called")
    kx, ky = kkt.rct.center
    for bmb in bomb_lst:
        bx, by = bmb.rct.center
        if (bx-kx)**2 + (by-ky)**2 <= R**2:
            bomb_lst.remove(bmb)
            print("poped")
    return bomb_lst

def game_quit(text_obj,scr):
    text_obj.blit(scr, (550, 400))


class TextMessage:  # 表示するテキストを扱うクラス
    def __init__(self, text, size, color):
        fonto = pg.font.Font(None,size)
        self.txt = fonto.render(text, True, color)

    def blit(self,scr, xy):
        scr.sfc.blit(self.txt, xy)


class Screen:
    def __init__(self, title, wh, image_path):
        # 練習１
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(image_path)
        self.bgi_rct = self.sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Clowd:    # 雨雲を扱うクラス
    def __init__(self, xy, vxy,scr:Screen):
        # 雲をつくる
        x, y = xy
        self.sfc = pg.Surface((x,y))
        self.sfc.set_colorkey((0,0,0))
        (285,185)
        cd_lst = [(x-185,y-120),(x-110,y-120),(x-235,y-85),(x-50,y-85),(x-170,y-50),(x-95,y-50)]
        for cd in cd_lst:
            pg.draw.circle(self.sfc, (150,150,150), cd, 50)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(150,scr.rct.width-150)
        self.rct.centery = 150
        self.vx, self.vy= vxy
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko_cd, _ = check_bound(self.rct,scr.rct)
        self.vx *= yoko_cd
        self.blit(scr)


class Bird:
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, image_path, ratio, xy):
        self.sfc = pg.image.load(image_path)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, ratio)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, scr.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb:
    def __init__(self,color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((2*rad, 2*rad))
        self.sfc.set_colorkey((0, 0, 0))
        pg.draw.circle(self.sfc, color, (rad, rad), rad)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy

    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc, self.rct) 

    def update(self, scr:Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


def main():
    clock =pg.time.Clock()
    clock.tick(1000)
    in_game = True

    # スクリーンを作成
    scr = Screen("逃げろ！こうかとん", (1600,900), "fig/pg_bg.jpg")

    # こうかとんを作成
    kkt = Bird("fig/6.png", 2.0, (900,400))

    # 雲を作成
    cwd = Clowd((285,185),(+1,+0),scr)

    # 爆弾を作成
    bomb_lst = []
    for i in range(5):
        bomb = Bomb((255, 0, 0), 10, (+1,+1), scr)
        bomb_lst.append(bomb)

    # テキストメッセージを作成
    text_in_game_quit = TextMessage("q: QUIT", 30, "WHITE")
    text_in_game_space = TextMessage("space: defuse bombs around U",30, "WHITE")
    text_game_quit = {"s":TextMessage("GAME OVER", 120, "LIMEGREEN"), "f":TextMessage("GAME OVER", 120, "LIMEGREEN")}


    # ゲーム中
    while True:
        scr.blit()
        # q: QUIT の案内表示
        text_in_game_space.blit(scr,(20,840))
        text_in_game_quit.blit(scr, (20,870))

        # ✕で終了
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                return
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                bomb_lst =  check_around(kkt, bomb_lst)
        
        # 爆弾がすべて消えたら
        if not bomb_lst:
            # ゲーム終了
            game_quit(text_game_quit["s"], scr)            

        if in_game:
            # こうかとんの座標を更新
            kkt.update(scr)

            # 爆弾の座標を更新
            for i in range(len(bomb_lst)):
                bomb_lst[i].update(scr)
                if kkt.rct.colliderect(bomb_lst[i].rct):
                    in_game = False

            # 雲の座標を更新
            cwd.update(scr)
            if kkt.rct.colliderect(cwd.rct):
                in_game = False

        else:
            kkt = Bird("fig/8.png", 2.0, (kkt.rct.center))
            kkt.update(scr)

            if bomb_lst:
                game_quit(text_game_quit["f"], scr)
            
        # 画面を更新
        pg.display.update()


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
