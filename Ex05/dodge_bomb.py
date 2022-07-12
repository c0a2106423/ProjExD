import pygame as pg
import sys
import random


class Screen:
    def __init__(self, title: str, wh: tuple, image: str) :
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)
    

class Bird:
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom_rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, base_obj: Screen):
        base_obj.sfc.blit(self.sfc, self.rct)
    
    def update(self, base_obj: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] : 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN] : 
            self.rct.centery += 1
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += 1
        
        if check_bound(self.rct, base_obj.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: self.rct.centery += 1
            if key_states[pg.K_DOWN]  == True: self.rct.centery -= 1
            if key_states[pg.K_LEFT]  == True: self.rct.centerx += 1
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= 1
        self.blit(base_obj)
        

class Bomb:
    def __init__(self, color: tuple, size: int, speed: tuple, base_obj: Screen) -> None:
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, base_obj.rct.width)
        self.rct.centery = random.randint(0, base_obj.rct.height)
        self.vx, self.vy = speed
    
    def blit(self, base_obj: Screen):
        base_obj.sfc.blit(self.sfc, self.rct)
    
    def update(self, base_obj:Screen):
        self.rct.move_ip(self.vx, self.vy)
        base_obj.sfc.blit(self.sfc, self.rct)
        yoko, tate = check_bound(self.rct, base_obj.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(base_obj)


def main():
    clock = pg.time.Clock()

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    bird = Bird("fig/6.png", 2.0, (900, 400))

    # bomb = list()
    # bomb.append(Bomb((255, 0, 0), 10, (1, 1), scr))
    bomb = Bomb((255, 0, 0), 10, (1, 1), scr)

    while True:
        #screen_sfc.blit(bgimg_sfc, bgimg_rct)
        scr.blit()

        # 練習2
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            # if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            #     bomb.append(Bomb((255, 0, 0), 10, (1, 1), scr))
        bird.update(scr)
        # for i in range(len(bomb)):
        #     bomb[i].update(scr)
        #     if bird.rct.colliderect(bomb[i].rct): 
        # return 
        bomb.update(scr)
        if bird.rct.colliderect(bomb.rct): 
            return 
        #pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()