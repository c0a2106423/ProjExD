import pygame as pg
import random
import sys
import maze_maker
stage_count = 0

class Screen:
    def __init__(self, title: str, wh: tuple, image: str) :
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.x_count = wh[0]//100 #よこのブロック数
        self.y_count = wh[1]//100 #たてのブロック数

        self.map_init(self.sfc, self.x_count, self.y_count, wh)#迷路生成

    def blit(self):
        self.sfc.fill((255,255,255))#背景を白色に染める
        self.s_tile_blit()#特殊マスの描写
        pass
        self.map_blit()#黒ブロック描写(絶対にキャラがかぶらないならいらない)

    def map_init(self, base_obj, x:int, y:int, wh:tuple) -> None:
        self.map_ary = maze_maker.make_maze(x, y)
        self.x_size = round(wh[0]/x)
        self.y_size = round(wh[1]/y)
        for i in self.map_ary:
            print(i)

        self.map_ary[1][1] = 2
        goal_pos = self.goal_p()
        self.map_ary[goal_pos[1]][goal_pos[0]] = 3
        self.b_color = (100, 100, 100)
        self.s_color = (  0, 255,   0)
        self.g_color = (255,   0,   0)
        self.block_lst = list() #壁tileのリスト
        self.s_tile_lst = list() #superなtileのリスト
        
        for i in range(len(self.map_ary)):#マップ配列を回す。
            for j in range(len(self.map_ary[i])):
                if self.map_ary[i][j]==1: # 壁のマスならば、Blockクラスのインスタンスを生成し、block_lstリストに追加。
                    self.block_lst.append(Block(self.b_color, self.x_size, self.y_size, (j, i), self.sfc)) 
                #特殊な役割のtileならば、Blockクラスのインスタンスを生成し、s_tile_lstリストに追加。
                elif self.map_ary[i][j] == 2: #スタートなら
                    self.s_tile_lst.append(Block(self.s_color, self.x_size, self.y_size, (j, i), self.sfc)) 
                elif self.map_ary[i][j] == 3: #ゴールなら
                    self.s_tile_lst.append(Block(self.g_color, self.x_size, self.y_size, (j, i), self.sfc)) 
                    #print("fiz")
                    
        pg.display.update()#初期描写

    def map_blit(self):#（壁を描写）
        for i in self.block_lst: #(1つずつ)丁寧に描く。効率よいやり方求む。
            i.blit(self.sfc)
    
    def s_tile_blit(self):#特殊なタイルを描写.
        for i in self.s_tile_lst:
            i.blit(self.sfc)
    
    def goal_p(self):
        height = len(self.map_ary) #高さを取得
        end_p=[] #ゴール候補のy座標のリスト
        for i in range(0, height):
            if not self.map_ary[i][-2]: #そのマスが床なら
                if self.map_ary[i][-3] + self.map_ary[i-1][-2] + self.map_ary[i+1][-2] == 2: #かつ、右側を除く3方のうち、2方が壁なら
                    end_p.append(i) # 候補リストに追加
        #print(end_p)
        if len(end_p): #候補が一つでもあれば
            i = random.randint(0,len(end_p)-1) #リストのインデックスをランダムに選び
            #print(i)
            y = end_p[i] # y に代入
        else: #候補がない場合
            for i in range(height): #とりあえず右端から２列目の床のマスにゴールを設定
                if not self.map_ary[i][-2]:
                    y = i
        x = len(self.map_ary[-2])-2 #x座標を設定
        #print(x, y)
        return(x, y) #設定した座標を返す


class Block:
    def __init__(self, color, x_size, y_size, xy, base_obj:Screen):#
        self.x_size = x_size #念のため持たせてる。いらない
        self.y_size = y_size #同上
        #print(xy)

        self.sfc = pg.Surface((x_size, y_size)) #surfaceを1マス分の大きさに設定
        self.rct = self.sfc.get_rect() # surfaceの大きさでrectを作っておく

        pg.draw.rect(self.sfc, color, (0,0,x_size, y_size)) #
        self.rct = self.sfc.get_rect() #
        self.rct.centerx = xy[0] * x_size + x_size/2 #
        self.rct.centery = xy[1] * y_size + y_size/2 #
 
    def blit(self, base_obj):
        base_obj.blit(self.sfc, self.rct) #ブロックを背景に貼り付ける。
        pass


class Bird:
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        self.sfc = pg.image.load(image)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom_rate)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
    
    def blit(self, base_obj: Screen):
        base_obj.sfc.blit(self.sfc, self.rct)
    
    def update(self, base_obj: Screen):
        self.dx = base_obj.x_size
        self.dy = base_obj.y_size
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] : 
            self.rct.centery -= self.dy
        if key_states[pg.K_DOWN] : 
            self.rct.centery += self.dy
        if key_states[pg.K_LEFT] : 
            self.rct.centerx -= self.dx
        if key_states[pg.K_RIGHT] : 
            self.rct.centerx += self.dx
        
        if collision_detect(self.rct, base_obj.block_lst) or check_bound(self.rct, base_obj.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]    == True: self.rct.centery += self.dy
            if key_states[pg.K_DOWN]  == True: self.rct.centery -= self.dy
            if key_states[pg.K_LEFT]  == True: self.rct.centerx += self.dx
            if key_states[pg.K_RIGHT] == True: self.rct.centerx -= self.dx
        self.blit(base_obj)
        
class Enemy(Bird):
    def __init__(self, image: str, zoom_rate: float, xy: tuple) -> None:
        super().__init__(image, zoom_rate, xy)
        self.now_dir = 0
        self.count = 0
    
    def update(self, base_obj: Screen, map_ary):
        self.count += 1
        if self.count > 20:
            self.dx = base_obj.x_size
            self.dy = base_obj.y_size
            self.now_dir, x, y = self.search_left(map_ary)
            self.rct.center = x*self.dx+self.dx//2, y*self.dy+self.dy//2
            
            if check_bound(self.rct, base_obj.rct) != (1, 1): # 領域外だったら
                if self.now_dir == 1: self.rct.centery += self.dy
                if self.now_dir == 3: self.rct.centery -= self.dy
                if self.now_dir == 2: self.rct.centerx += self.dx
                if self.now_dir == 0: self.rct.centerx -= self.dx
            self.count = 0
        self.blit(base_obj)
        
        
        #print(self.rct.center)
        pass

    def search_left(self, map_ary):
        print("")
        for i in map_ary:
            print(i)
        dif = ((0,1), (1,0), (0,-1),(-1,0))
        for i in range(4):
            dir = (self.now_dir+3+i)%4
            x = (self.rct.centerx//self.dx + dif[dir][0])
            y = (self.rct.centery//self.dy + dif[dir][1])
            print(x,y)
            if map_ary[y][x] == 0:
                print("d")
                break
            else:
                print("f")
        #print(dir, x, y)
        return dir,x,y


class Text:
    def __init__(self, content, base_obj:Screen, x_size, y_size) -> None:
        font = pg.font.Font(None, 60)
        self.sfc = font.render(content, True, (255,0,0))
        self.rct = self.sfc.get_rect()
        self.rct.center = x_size//2, y_size//2
        base_obj.sfc.blit(self.sfc,self.rct) #文言を表示
    
    def blit(self, base_obj:Screen):
        base_obj.sfc.blit(self.sfc, self.rct)

class main: # mainをクラスに。
    def __init__(self) -> None: #main の main。Javaでいうpublic static void main(String args[]){}なとこ。
        global stage_count
        stage_count += 1
        clock = pg.time.Clock()
        height = 900
        width = 1500

        scr = Screen("戦え！こうかとん", (width, height), "fig/pg_bg.jpg")
        bird = Bird("fig/6.png", 1.5, (scr.x_size+scr.y_size//2, scr.y_size+scr.y_size//2))
        enemy = Enemy("fig/s_exp.png", 0.8, (scr.s_tile_lst[1].rct.centerx, scr.s_tile_lst[1].rct.centery))
        text = Text(str(stage_count), scr, scr.x_size, scr.y_size)
        
        while True:
            #enemy.blit(scr)
            bird.blit(scr)
            text.blit(scr)
            for event in pg.event.get():
                if event.type == pg.QUIT: #右上のXが押されたら
                    return                  #mainから抜けてプログラムを終了させる
                if event.type == pg.KEYDOWN: #キーが押下されたならば、
                    #方向キーならば、
                    if event.key == pg.K_DOWN or event.key == pg.K_UP or event.key == pg.K_LEFT or event.key==pg.K_RIGHT:
                        bird.update(scr) #鳥を移動させ、描写しなおす
            enemy.update(scr, scr.map_ary)
            if bird.rct.colliderect(scr.s_tile_lst[1].rct):
                main()
                return
            if bird.rct.colliderect(enemy.rct):
                pg.display.update()
                enemy.update(scr, scr.map_ary)
                bird.blit(scr)
                text.blit(scr)
                self.game_over(scr)
                return
            pg.display.update()
            clock.tick(100)
            scr.blit()

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

def collision_detect(rct, block_rct):
    bool = False #初期値を設定
    if type(block_rct)==list:#もしリスト型で渡されたら、要素ごとに判定。
        for b in block_rct:
            if rct.colliderect(b.rct) == True:
                #print("True")
                bool = True
                break
            else :
                #print("False")
                continue
    else: #違うなら、引数をそのまま判定
        try: #一応try文つき。
            if rct.colliderect(block_rct) == True:
                #print("True")
                bool = True
        except:
            print("ここに来たらおかしい。")
    return bool
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