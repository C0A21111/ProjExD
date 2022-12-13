import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん") # タイトルバー
    scrn_sfc = pg.display.set_mode((1600,900)) # 1600x900のSurface

    tori_sfc = pg.image.load("fig/pg_bg.jpg") # Surface
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 1.0)
    tori_rct = tori_sfc.get_rect() # Rect
    tori_rct.center = 800, 450
    scrn_sfc.blit(tori_sfc, tori_rct) # blit

    pg.display.update()

    clock.tick(0.5)

if __name__ == "__main__":
    pg.init()

    main()

    pg.quit()
    sys.exit()