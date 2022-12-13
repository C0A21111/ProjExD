import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん") # タイトルバー
    scrn_sfc = pg.display.set_mode((1600,900)) # 1600x900のSurface

    # 背景画像
    pgbg_sfc = pg.image.load("fig/pg_bg.jpg")
    pgbg_rct = pgbg_sfc.get_rect() 
    pgbg_rct.center = 800, 450
    # こうかとん画像
    kktn_sfc = pg.image.load("fig/3.png")
    kktn_sfc = pg.transform.rotozoom(kktn_sfc, 0, 2.0)
    kktn_rct = kktn_sfc.get_rect()
    kktn_rct.center = 900, 400
    kktn_sfc.blit(kktn_sfc, kktn_rct) # こうかとん画像blit

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) # 背景画像blit
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()

    main()

    pg.quit()
    sys.exit()