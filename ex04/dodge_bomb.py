import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん") # タイトルバー
    scrn_sfc = pg.display.set_mode((1600,900)) # 1600x900のSurface

    pgbg_sfc = pg.image.load("fig/pg_bg.jpg") # Surface
    pgbg_rct = pgbg_sfc.get_rect() # Rect
    pgbg_rct.center = 800, 450

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) # blit
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()

    main()

    pg.quit()
    sys.exit()