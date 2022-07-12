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

class AdvancedBomb(Bomb):#Bombを継承したクラス
    def __init__(self, color: tuple, size: int, speed: tuple, base_obj: Screen, live_time: int = random.randint(500, 5000)) -> None:
        super().__init__(color, size, speed, base_obj)
        self.live_time = live_time #生存時間の概念を追加
        self.death_monitor = False

    def update(self, base_obj: Screen, list_obj=None, index=None):
        self.live_time -= 1 #残り生存時間を減らす
        if self.live_time < 0: #0を切ったら
            self.explosion(list_obj, index) # 炸裂させる
        super().update(base_obj)
        return index
        
    def explosion(self, list_obj, index):#炸裂させる
        if self.death_monitor :
            return self.delete_obj(list_obj, index)
        rct_pos = self.rct.center
        self.death_monitor = True
        self.live_time = 100
        self.vx, self.vy = 0, 0
        if random.randint(0,10) < 6:
            self.sfc = pg.image.load("fig/s_exp.png")
        else:
            self.sfc = pg.image.load("fig/l_exp.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.8)
        self.rct = self.sfc.get_rect()
        self.rct.center = rct_pos
        return index

    def delete_obj(self, list_obj, index):#爆弾の削除
        if list_obj == None or index == None:
            return index
        else:
            del list_obj[index]
            index -= 1
            #print(" "+ str(index))
            return index


class Attack: #実装中
    def __init__(self, identify:bool, ) -> None:
        self.identify = identify
    

class BombAttack(AdvancedBomb, Attack): #発射された爆弾
    def __init__(self, color: tuple, size: int, speed: tuple, base_obj: Screen, live_time: int,  pos: tuple, identify: bool) -> None:
        super().__init__(color, size, speed, base_obj, live_time)
        self.identify = identify
        self.rct.center = pos
    

class Kuma(Bird): #実装中
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        super().__init__(image, zoom_rate, xy)
    
    def attack(self, base_obj, list_obj, bomb_num:int=1):
        if bomb_num > 0:
            for i in bomb_num:
                list_obj.append(BombAttack((0,255,0), 10, (1, 1), base_obj, 1600, self.rct.center, True))


class main: # mainをクラスに。
    def __init__(self) -> None: #main の main。Javaでいうpublic static void main(String args[]){}なとこ。
        clock = pg.time.Clock()

        scr = Screen("戦え！こうかとん", (1600, 900), "fig/pg_bg.jpg")
        bird = Bird("fig/6.png", 2.0, (900, 400))

        bomb = list()
        bomb.append(AdvancedBomb((255, 0, 0), 10, (1, 1), scr))
        attack = list()

        while True:
            scr.blit()
            for event in pg.event.get():
                if event.type == pg.QUIT: 
                    return
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE: #Spaceキーを押したら
                        bomb.append(AdvancedBomb((255, 0, 0), 10, (1, 1), scr)) # 爆弾を追加
                    elif event.key == pg.K_r: # Rキーを押したら
                        attack.append(BombAttack((0, 0, 255), 10, (-1, 0), scr, 1000, bird.rct.center, True)) #自分に当たらない爆弾を撃ち落とす爆弾を追加
            bird.update(scr)
            try: #try文は、実装が不適切なものを強引に動かすために追加した。
                if len(bomb)>0: 
                    for i in range(len(bomb)): # 敵味方両方に効く予定だったものを判定
                        #print(i)
                        if bird.rct.colliderect(bomb[i].rct): 
                            self.game_over(scr)
                            return 
                        i=bomb[i].update(scr, bomb, i)
                        #print("  "+str(i))
            except: #
                #print("err")
                pass
            try: #try文は、実装が不適切なものを強引に動かすために追加した。
                for i in range(len(attack)):# 攻撃のオブジェクト(敵味方の判定があるもの)を判定
                    if bird.rct.colliderect(attack[i].rct) and attack[i].identify == False:
                        self.game_over(scr)
                        return
                    for j in range(len(bomb)):
                        if attack[i].rct.colliderect(bomb[j].rct):
                            attack[i].explosion(attack, i)
                            bomb[j].explosion(bomb, j)
                    i=attack[i].update(scr, attack, i)
            except:
                pass
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