import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("../ex01/fig/pg_bg.jpg")
    bg_img_flip = pg.transform.flip(bg_img,True,False)
    kokaton_img = pg.image.load("fig/3.png")
    kokaton_img_flip = pg.transform.flip(kokaton_img,True,False)
    kokaton_img_grad_10 = pg.transform.rotozoom(kokaton_img_flip,10,1.0)
    kokaton_list = [kokaton_img_flip,kokaton_img_grad_10]
    tmr = 0
    
    
    kokaton_grad = True
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
         

        bg_pos = -(tmr % (1600)) 
        
        #ずっと1600にしててうまくいかなかった
        if (bg_pos + 1599) == 0:
            bg_pos = 0
            #bg_img_flip = pg.transform.flip(bg_img_flip,True,True)
            #bg_img = pg.transform.flip(bg_img,True,True)
            #flip
            img_buff = bg_img_flip
            bg_img_flip = bg_img
            bg_img =  img_buff
            print("pic move")
        print("\r"+str(bg_pos))
        
    
    
        
        
        screen.blit(bg_img, [bg_pos, 0])
        screen.blit(bg_img_flip,[bg_pos + 1600, 0])
        

        #small window
        #screen.blit(pg.transform.rotozoom(bg_img_flip,0,0.125),[(bg_pos + 1610) * 0.125 + 100, 100])
        #screen.blit(pg.transform.rotozoom(bg_img,0,0.125),[(bg_pos) * 0.125 + 100, 100])
        
        #screen.blit(pg.transform.rotozoom(bg_img_flip,0,0.0625),[(0) * 0.125 + 100, 200])

        if tmr % 50 == 0:
            kokaton_grad = not kokaton_grad 
        screen.blit(kokaton_list[kokaton_grad],[300,200])
        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
