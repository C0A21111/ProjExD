import pygame as pg
import sys
import random

def check_bound(obj_rct, scr_rct):
    # 第１引数：こうかとんrectまたは爆弾rect
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
    tori_sfc.blit(tori_sfc, tori_rct) # こうかとん画像blit

    bomb_sfc = pg.Surface((20,20)) # 正方形の空Surface
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc, (255,0,0), (10,10),10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0,scrn_rct.width)
    bomb_rct.centery = random.randint(0,scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) # 爆弾画像blit
    vx,vy = +1,+1

    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) # 背景画像blit
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_dct = pg.key.get_pressed()
        if key_dct[pg.K_UP]:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN]:
            tori_rct.centery += 1
        if key_dct[pg.K_RIGHT]:
            tori_rct.centerx += 1
        if key_dct[pg.K_LEFT]:
            tori_rct.centerx -= 1
        if check_bound(tori_rct,scrn_rct) != (+1,+1):
            if key_dct[pg.K_UP]:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN]:
                tori_rct.centery -= 1
            if key_dct[pg.K_RIGHT]:
                tori_rct.centerx -= 1
            if key_dct[pg.K_LEFT]:
                tori_rct.centerx += 1
        scrn_sfc.blit(tori_sfc, tori_rct) # こうかとん画像blit

        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx *= yoko
        vy *= tate
        bomb_rct.move_ip(vx,vy)

        scrn_sfc.blit(bomb_sfc, bomb_rct) # 爆弾画像blit

        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()

    main()

    pg.quit()
    sys.exit()