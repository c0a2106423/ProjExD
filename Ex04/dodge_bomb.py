import pygame as pg
import sys
from random import randint as rnd
class Game():
    def __init__(self) -> None:
        pg.init()
        self.main()
        pg.quit()
        sys.exit()

    def main(self):
        r = 10 #爆弾の半径
        global clock, height, width
        height = 900 #ウィンドウの縦幅
        width = 1600 #ウィンドウの横幅
        clock = pg.time.Clock() 
        self.bg_img = None  #動作を軽くしようとした悪足掻き
        self.bomb_x, self.bomb_y = None, None #同上
        self.bomb=list()    #爆弾を複数出すためにリスト管理する

        #ウィンドウの初期設定
        pg.display.set_caption("逃げろ！こうかとん")
        screen = self.set_screen(height, width)
        #鳥の画像を読み込み
        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
        #ゲームオーバー時の文言を設定
        font = pg.font.Font(None, 80)
        txt = font.render(str("GAME OVER"), True, (255,0,0))
        txt_rect = txt.get_rect()
        txt_rect.center = width/2,height/2
        #1個目の爆弾を設定/鳥を設定
        self.bomb.append(Bomb(screen, r, height, width, self.bomb_x, self.bomb_y))
        self.tori01=Obj(screen, tori_img, 900, 400)

        while True: #繰り返し部
            for event in pg.event.get(): #爆弾追加・終了処理など、押される度に1回だけ行う処理の判定
                if event.type == pg.QUIT: return
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.bomb.append(Bomb(screen, r, height, width, self.bomb_x, self.bomb_y))
            #鳥を動かすためのキー判定
            key_dict = pg.key.get_pressed()
            diff = [0, 0]
            if key_dict[pg.K_UP]==True:
                diff[1] -= 1
            if key_dict[pg.K_DOWN]==True:
                diff[1] += 1
            if key_dict[pg.K_LEFT]==True:
                diff[0] -= 1
            if key_dict[pg.K_RIGHT]==True:
                diff[0] += 1
            self.draw(height, width, diff)
            screen[0].blit(screen[0], screen[1])
            #print(self.tori01.rect.center, self.bomb.rect.center)
            #爆弾の接触判定
            for i in range(len(self.bomb)):
                if self.tori01.rect.colliderect(self.bomb[i].rect):#接触しているならば
                    game_over = screen[0].blit(txt,txt_rect) #文言を表示
                    pg.display.update()
                    while True: #バッテンが押されるまで無限ループ
                        for event in pg.event.get():
                            if event.type == pg.QUIT: return
            pg.display.update()
            clock.tick(1000)

    def set_screen(self, height, width): #背景の設定・描写
        screen_sfc = pg.display.set_mode((width, height))
        screen_rct = screen_sfc.get_rect()
        if self.bg_img == None:
            self.bg_img  = pg.image.load("fig/pg_bg.jpg")
        bg_rct = self.bg_img.get_rect()
        screen_sfc.blit(self.bg_img, bg_rct)
        return screen_sfc, screen_rct

    def draw(self, height, width, diff): #繰り返しごとの描写
        self.set_screen(height, width)
        for i in range(len(self.bomb)):
            self.bomb[i].move()
        self.tori01.move(diff)

class Bomb():
    def __init__(self, screen, r, w_height, w_width, x, y): #初期値設定
        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.vx, self.vy = 1, 1
        if self.x == None:
            self.x, self.y = rnd(1,w_height-2), rnd(1,w_width-2)
        self.image = pg.Surface((2*self.r,2*self.r))
        pg.draw.circle(self.image, (255, 0, 0), (self.r, self.r), self.r)
        self.image.set_colorkey((0, 0, 0))
        self.draw()

    def draw(self): # 爆弾の描写
        self.rect = self.screen[0].blit(self.image, (self.x, self.y))

    def move(self): #爆弾の移動
        self.x += self.vx
        self.y += self.vy
        self.bound()
        self.draw()
    
    # def get_pos(self): #実装しようとした機能の残骸
    #     return self.x, self.y
    
    def bound(self): #枠外判定
        if 0 < self.x < width and 0 < self.y < height:
            pass
        elif self.x > width: 
            self.x = width-1
            self.vx *= -1
            #print(1)
        elif self.x < 0: 
            self.x = 0
            self.vx *= -1
            #print(2)
        elif self.y > height: 
            self.y = height-1
            self.vy *= -1
            #print(3)
        elif self.y < 0: 
            self.y = 0
            self.vy *= -1
            #print(4)
    
class Obj(): #オブジェクト用のクラス。Bombクラスはこのサブクラスになる予定でした。
    def __init__(self, screen, img, x=0, y=0) -> None: #初期化・初回描写
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = self.x, self.y
        self.screen[0].blit(img, self.rect)
    
    def move(self, diff=[0,0]): #オブジェクトを動かす
        self.x += diff[0]
        self.y += diff[1]
        self.rect.center = (self.x, self.y)
        self.chk_pos()
        self.screen[0].blit(self.img, self.rect)

    def chk_pos(self): #枠外チェック
        if self.x > width: self.x = width
        elif self.x < 0: self.x = 0
        elif self.y > height: self.y = height
        elif self.y < 0: self.y = 0

if __name__ == "__main__":
    Game()

