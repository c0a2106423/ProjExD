import pygame as pg
import sys
import random as rd


def main():

    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    bg_img = pg.image.load(
        "fig/pg_bg.jpg"
    )
    bg_rect = bg_img.get_rect()

    kokaton_img = pg.image.load(
        "fig/6.png"
    )
    kokaton_img = pg.transform.rotozoom(kokaton_img, 0, 2.0)

    kokaton_rect = kokaton_img.get_rect()
    kokaton_rect.center = 900, 400

    bomb = pg.Surface((20, 20))
    bomb.set_colorkey((0, 0, 0))
    bomb_rect = bomb.get_rect()

    x = rd.randint(0, 1600)
    y = rd.randint(0, 900)

    dx = 1
    dy = 1

    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)

    while True:

        screen.blit(bg_img, bg_rect)
        screen.blit(kokaton_img, kokaton_rect)
        screen.blit(bomb, bomb_rect)

        if x < 0 or 1600 < x:
            dx *= -1
        if y < 0 or 900 < y:
            dy *= -1

        print(bomb_rect.centerx, bomb_rect.centery)
        key_status = pg.key.get_pressed()
        print(key_status[pg.K_UP])
        if key_status[pg.K_UP]:
            kokaton_rect.move_ip(0, -1)
        if key_status[pg.K_DOWN]:
            kokaton_rect.move_ip(0, 1)
        if key_status[pg.K_RIGHT]:
            kokaton_rect.move_ip(1, 0)
        if key_status[pg.K_LEFT]:
            kokaton_rect.move_ip(-1, 0)

        if kokaton_rect.colliderect(bomb_rect) == True:
            return

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        pg.display.update()

        x += dx
        y += dy

        bomb_rect.center = (x, y)

        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()