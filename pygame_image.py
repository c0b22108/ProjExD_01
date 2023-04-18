import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("../ex01/fig/pg_bg.jpg")
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img_flip = pg.transform.flip(kokaton_img,True,False)
    kokaton_img_grad_10 = pg.transform.rotate(kokaton_img_flip,10)
    kokaton_list = [kokaton_img_flip,kokaton_img_grad_10]
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        bg_pos = 1599 - tmr 
        bg_pos = -tmr
        screen.blit(bg_img, [bg_pos, 0])
        screen.blit(kokaton_list[tmr % 2],[300,200])
        #screen.blit(kokaton_img_grad_10,[300,400])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
