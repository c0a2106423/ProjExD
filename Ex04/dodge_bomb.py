import pygame as pg
import sys

class game():
    def __init__(self) -> None:
        pg.init()
        self.main()

        pg.quit()
        sys.exit()

    def main(self):
        height = 1600
        width = 900
        global clock
        clock = pg.time.Clock()
        self.bg_img = None

        pg.display.set_caption("逃げろ！こうかとん")
        screen = self.setScreen(height, width)
        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
        #print(id(screen))
        tori01=obj(screen, tori_img, 900, 400)

        while True:
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
                self.setScreen(height, width)
                tori01.move(diff)
            pg.display.update()
            clock.tick(1000)

    def setScreen(self, height, width):
        screen = pg.display.set_mode((height, width))
        if self.bg_img == None:
            self.bg_img  = pg.image.load("fig/pg_bg.jpg")
        bg_rect = self.bg_img.get_rect()
        screen.blit(self.bg_img, bg_rect)
        return screen


class obj():
    def __init__(self, screen, img, x=0, y=0) -> None:
        self.x = x
        self.y = y
        self.screen = screen
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.center = self.x, self.y
        self.screen.blit(img, self.rect)
        #print(id(self.screen),id(screen))
        #pg.display.update()
    
    def move(self, diff=[0,0]):
        self.x += diff[0]
        self.y += diff[1]
        #print(self.x, self.y)
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.img, self.rect)
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

