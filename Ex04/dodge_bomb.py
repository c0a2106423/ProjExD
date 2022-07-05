from tkinter import CENTER
import pygame as pg
import sys
from random import randint as rnd
class game():
    def __init__(self) -> None:
        pg.init()
        self.main()

        pg.quit()
        sys.exit()

    def main(self):
        r = 10
        global clock, height, width
        height = 900
        width = 1600
        clock = pg.time.Clock()
        self.bg_img = None
        self.bomb_x, self.bomb_y = None, None

        pg.display.set_caption("逃げろ！こうかとん")
        screen = self.setScreen(height, width)
        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
        #print(id(screen))
        self.bomb = Bomb(screen, r, height, width, self.bomb_x, self.bomb_y)
        self.tori01=obj(screen, tori_img, 900, 400)

        while True:
            #clock.tick(0.3)
            for event in pg.event.get():
                if event.type == pg.QUIT: return
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
            if diff[0] != 0 or diff[1] != 0: 
                #tori01.move(diff)
                self. draw(screen, r, height, width, diff)
            else:
                self.bomb.move()
            screen[0].blit(screen[0], screen[1])
            pg.display.update()
            clock.tick(1000)

    def setScreen(self, height, width):
        screen_sfc = pg.display.set_mode((width, height))
        screen_rct = screen_sfc.get_rect()
        if self.bg_img == None:
            self.bg_img  = pg.image.load("fig/pg_bg.jpg")
        bg_rct = self.bg_img.get_rect()
        screen_sfc.blit(self.bg_img, bg_rct)
        return screen_sfc, screen_rct

    def draw(self, screen, r, height, width, diff):
        
        self.setScreen(height, width)
        self.bomb.draw()
        self.tori01.move(diff)

class Bomb():
    def __init__(self, screen, r, w_height, w_width, x, y):
        self.screen = screen
        self.bomb_x = x
        self.bomb_y = y
        self.r = r
        self.vx, self.vy = 0, 0
        if self.bomb_x == None:
            self.bomb_x, self.bomb_y = rnd(0,w_height), rnd(0,w_width)
        self.image = pg.Surface((2*self.r,2*self.r))
        pg.draw.circle(self.image, (255, 0, 0), (self.r, self.r), self.r)
        self.image.set_colorkey((0, 0, 0))
        self.draw()

    def draw(self):
        #self.image = pg.Surface((2*self.r,2*self.r))
        #pg.draw.circle(self.image, (255, 0, 0), (self.r, self.r), self.r)
        #self.image.set_colorkey((0, 0, 0))
        self.screen[0].blit(self.image, (self.bomb_x, self.bomb_y))

    def move(self):
        self.vx+=1
        self.vy+=1
        #self.image = pg.Surface((2*self.r,2*self.r))
        #pg.draw.circle(self.image, (255, 0, 0), (self.r, self.r), self.r)
        #self.image.set_colorkey((0, 0, 0))
        self.bomb_x += self.vx
        self.bomb_y += self.vy
        self.draw() 
    
class obj():
    def __init__(self, screen, img, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = self.x, self.y
        self.screen[0].blit(img, self.rect)
        #print(id(self.screen),id(screen))
        #pg.display.update()
    
    def move(self, diff=[0,0]):
        self.x += diff[0]
        self.y += diff[1]
        #print(self.x, self.y)
        self.rect.center = (self.x, self.y)
        self.screen[0].blit(self.img, self.rect)
        #print(id(self.screen))
        #pg.display.update()

    """def move(self, x_diff, y_diff):
        self.x += x_diff
        self.y += y_diff
        rect.center = self.x, self.y
        screen.blit(self.img, rect)
        pg.display.update()"""

if __name__ == "__main__":
    game()

