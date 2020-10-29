import pygame as pg

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)

pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    screen.fill(GRAY)
    pg.display.update()

