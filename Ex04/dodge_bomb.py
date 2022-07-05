from operator import truediv
from turtle import width
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

        pg.display.set_caption("逃げろ！こうかとん")
        screen = self.setScreen(height, width)
        

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: return
                elif event.type == pg.KEYDOWN:
                    pass
            pg.display.update()
            clock.tick(1000)

        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
        #tori01 = obj(screen, tori_img, 600, 400)
    
    def setScreen(self, height, width):
        screen = pg.display.set_mode((height, width))
        screen_rect = screen.get_rect()
        bg_img  = pg.image.load("fig/pg_bg.jpg")
        bg_rect = bg_img.get_rect()
        screen.blit(bg_img, bg_rect)
        return screen


class obj():
    def __init__(self, screen, img, x=0, y=0) -> None:
        rect = img.get_rect()
        rect.center = x, y
        screen.blit(img, rect)
        pg.display.update()

if __name__ == "__main__":
    game()

