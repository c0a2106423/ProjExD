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
        bg_img  = pg.image.load("fig/pg_bg.jpg")
        pg.display.set_caption("逃げろ！こうかとん")
        screen = pg.display.set_mode((height, width))
        bg = obj(screen, bg_img, height//2, width//2)

        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)

        tori01 = obj(screen, tori_img, 600, 400)
        clock.tick(0.2)

class obj():
    def __init__(self, screen, img, x=0, y=0) -> None:
        rect = img.get_rect()
        rect.center = x, y
        screen.blit(img, rect)
        pg.display.update()

if __name__ == "__main__":
    game()

