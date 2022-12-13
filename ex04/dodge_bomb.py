import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    # 第１引数：こうかとんrectまたは爆弾rectまたは雲rect
    # 第２引数：スクリーンrect
    # 範囲内: +1  /  範囲外： -1
    yoko,tate = +1,+1
    if obj_rct.left < scr_rct.left or obj_rct.right > scr_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or obj_rct.bottom > scr_rct.bottom:
        tate = -1
    return yoko,tate

def main():
    clock = pg.time.Clock()
    clock.tick(1000)
    in_game = True

    pg.display.set_caption("逃げろ！こうかとん") # タイトルバー
    scrn_sfc = pg.display.set_mode((1600,900)) # 1600x900のSurface
    scrn_rct = scrn_sfc.get_rect()

    # 背景画像
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect() 
    
    # こうかとん画像
    tori_sfc = pg.image.load("fig/3.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    scrn_sfc.blit(tori_sfc, tori_rct) # こうかとん画像blit

    # 爆弾を作る
    bomb_sfc = pg.Surface((20,20)) # 正方形の空Surface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255,0,0), (10,10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(10,scrn_rct.width-10)
    bomb_rct.centery = random.randint(10,scrn_rct.height-10)
    scrn_sfc.blit(bomb_sfc, bomb_rct) # 爆弾 blit
    vx_bb,vy_bb = +1,+1

    # 雲をつくる
    crwd_sfc = pg.Surface((285,185))
    crwd_sfc.set_colorkey((0,0,0))
    pg.draw.circle(crwd_sfc, (150,150,150), (100,65), 50)
    pg.draw.circle(crwd_sfc, (150,150,150), (175,65), 50)
    pg.draw.circle(crwd_sfc, (150,150,150), (50,100), 50)
    pg.draw.circle(crwd_sfc, (150,150,150), (235,100), 50)
    pg.draw.circle(crwd_sfc, (150,150,150), (115,135), 50)
    pg.draw.circle(crwd_sfc, (150,150,150), (190,135), 50)
    crwd_rct = crwd_sfc.get_rect()
    crwd_rct.centerx = random.randint(150,scrn_rct.width-150)
    crwd_rct.centery = 150
    scrn_sfc.blit(crwd_sfc, crwd_rct)
    vx_cd,vy_cd = +1, +0

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) # 背景画像blit
        for event in pg.event.get():
            if event.type == pg.QUIT: return
            if event.type == pg.K_q:  return
            
        if in_game: #  ゲーム中
            # こうかとん座標
            key_dct = pg.key.get_pressed()
            if key_dct[pg.K_UP]:    tori_rct.centery -= 1
            if key_dct[pg.K_DOWN]:  tori_rct.centery += 1
            if key_dct[pg.K_RIGHT]: tori_rct.centerx += 1
            if key_dct[pg.K_LEFT]:  tori_rct.centerx -= 1
            if check_bound(tori_rct,scrn_rct) != (+1,+1):
                if key_dct[pg.K_UP]:    tori_rct.centery += 1
                if key_dct[pg.K_DOWN]:  tori_rct.centery -= 1
                if key_dct[pg.K_RIGHT]: tori_rct.centerx -= 1
                if key_dct[pg.K_LEFT]:  tori_rct.centerx += 1

            # 爆弾座標
            yoko_bb,tate_bb = check_bound(bomb_rct,scrn_rct)
            vx_bb *= yoko_bb
            vy_bb *= tate_bb
            bomb_rct.move_ip(vx_bb,vy_bb)

            # 雲座標
            yoko_cd, _ = check_bound(crwd_rct,scrn_rct)
            vx_cd *= yoko_cd
            crwd_rct.move_ip(vx_cd,vy_cd)

        # 各オブジェクトblit
        scrn_sfc.blit(tori_sfc, tori_rct) # こうかとん
        scrn_sfc.blit(bomb_sfc, bomb_rct) # 爆弾
        scrn_sfc.blit(crwd_sfc, crwd_rct) # 雲

        # こうかとんと爆弾あるいは雲がぶつかったら
        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(crwd_rct): 
            tori_sfc = pg.image.load("fig/8.png")
            tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
            scrn_sfc.blit(tori_sfc, tori_rct) # こうかとん画像blit

            fonto = pg.font.Font(None,120)
            txt = fonto.render("GAME OVER", True, "LIMEGREEN")
            scrn_sfc.blit(txt, (550, 400))
            fonto = pg.font.Font(None,60)
            txt = fonto.render("q:  QUIT", True, "WHITE")
            scrn_sfc.blit(txt, (720, 500))

            in_game = False

        pg.display.update()

if __name__ == "__main__":
    pg.init()

    main()
    
    pg.quit()
    sys.exit()