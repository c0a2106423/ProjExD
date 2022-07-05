import pygame as pg
import sys

class game():
    def __init__(self) -> None:
        pg.init()
        self.main()

        pg.quit()
        sys.exit()

    def main(self):
        global clock
        clock = pg.time.Clock()
        tori_img = pg.image.load("fig/6.png")
        tori_img = pg.transform.rotozoom(tori_img, 0, 2.0)
        pg.display.set_caption("new game")
        screen = pg.display.set_mode((800, 600))
        tori_rect = tori_img.get_rect()
        tori_rect.center = 900, 400
        screen.blit(tori_img, tori_rect)
        #self.tori(screen, tori_img)

        
        pg.display.update()
        clock.tick(0.2)
        

    def tori(self, screen, img):
        tori_rect = img.get_rect()
        tori_rect.center = 900, 400
        screen.blit(img, tori_rect)

if __name__ == "__main__":
    game()

