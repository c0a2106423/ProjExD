import pygame as pg
import random
import sys
import maze_maker
import math

class Screen:
    def __init__(self, title: str, wh: tuple, image: str) :
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.x_count = wh[0]//100
        self.y_count = wh[1]//100

        self.map_init(self.sfc, self.x_count, self.y_count, wh)

    def blit(self):
        self.sfc.fill((255,255,255))
        pass
        self.map_blit()

    def map_init(self, base_obj, x:int, y:int, wh:tuple) -> None:
        self.map_ary = maze_maker.make_maze(x, y)
        self.x_size = round(wh[0]/x)
        self.y_size = round(wh[1]/y)
        self.w_color = (255, 255, 255)
        self.b_color = (  0,   0,   0)
        self.block_lst = list()
        for i in self.map_ary:
            print(i)
        
        for i in range(len(self.map_ary)):
            for j in range(len(self.map_ary[i])):
                if self.map_ary[i][j]==1:
                    self.block_lst.append(Block(self.b_color, self.x_size, self.y_size, (j, i), self.sfc))
        pg.display.update()

    def map_blit(self):
        for i in self.block_lst:
            i.blit(self.sfc)


class Block:
    def __init__(self, color, x_size, y_size, xy, base_obj:Screen):
        self.x_size = x_size
        self.y_size = y_size
        #print(xy)

        self.sfc = pg.Surface((self.x_size, self.y_size)) 
        self.rct = self.sfc.get_rect()

        pg.draw.rect(self.sfc, color, (0,0,self.x_size, self.y_size))
        self.rct = self.sfc.get_rect() 
        self.rct.centerx = xy[0] * x_size + x_size/2
        self.rct.centery = xy[1] * y_size + y_size/2

    def blit(self, base_obj):
        base_obj.blit(self.sfc, self.rct)
        pass


class Bird:
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom_rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, base_obj: Screen):
        base_obj.sfc.blit(self.sfc, self.rct)
    
    def update(self, base_obj: Screen, map_ary):
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
        
class Enemy(Bird):
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        super().__init__(image, zoom_rate, xy)
    
    def update(self, base_obj: Screen, map_obj):
        #if
        pass


class main: # mainをクラスに。
    def __init__(self) -> None: #main の main。Javaでいうpublic static void main(String args[]){}なとこ。
        clock = pg.time.Clock()

        scr = Screen("戦え！こうかとん", (1500, 900), "fig/pg_bg.jpg")
        bird = Bird("fig/6.png", 1.5, (900, 400))
        enemy = Enemy("fig/s_exp.png", 1.5, (50,50))
        
        while True:
            scr.blit()
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    return
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: #Spaceキーを押したら
                        bomb.append(AdvancedBomb((255, 0, 0), 10, (1, 1), scr)) # 爆弾を追加
                    elif event.key == pg.K_r: # Rキーを押したら
                        attack.append(BombAttack((0, 0, 255), 10, (-1, 0), scr, 1000, bird.rct.center, True)) #自分に当たらない爆弾を撃ち落とす爆弾を追加"""
            bird.update(scr, scr.map_ary)
            enemy.update(scr, scr.map_ary)
            pg.display.update()
            clock.tick(1000)

    def game_over(self, base_obj: Screen): #接触時に実行
        font = pg.font.Font(None, 80)
        self.sfc = font.render(str("GAME OVER"), True, (255,0,0))
        self.rct = self.sfc.get_rect()
        self.rct.center = base_obj.rct.width/2,base_obj.rct.height/2
        base_obj.sfc.blit(self.sfc,self.rct) #文言を表示
        pg.display.update()
        while True: #バッテンが押されるまで無限ループ
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return



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