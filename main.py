#"Ралли"
import pygame as pg
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

SIZE = WIDTH, HEIGHT = 800, 600
GRAY = (128, 128, 128)


pg.init()
pg.display.set_caption('Rally')
screen = pg.display.set_mode(SIZE)

FPS = 120
clock = pg.time.Clock()
GREEN = (0, 128, 0)
WHITE = (200, 200, 200)

#bg_image = pg.image.load('Image/road.jpg')
#bg_image_rect = bg_image.get_rect(topleft = (0, 0))
#bg_image_2_rect = bg_image.get_rect(topleft = (0, -HEIGHT))
car1_image = pg.image.load('Image/car1.png')

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('Image/car4.png')
        self.rect = self.image.get_rect()

class Car(pg.sprite.Sprite):
    def __init__(self, x, y, img):
        pg.sprite.Sprite.__init__(self)
        
        self.image = pg.transform.flip(img, False, True)
        #self.w, self.h = self.image.get_width(), self.image.get_height()
        self.speed = random.randint(2, 3)
        self.rect = self.image.get_rect(center=(x, y))

class Road(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.Surface(screen.get_size())
        self.image.sill(GRAY)
        pg.draw.line(self.image, GREEN, (20,0), (20, 600), 40)
        pg.draw.line(self.image, GREEN, (780, 0), (780, 600), 40)
        for xx in range(10):
        for yy in range(10):
            pg.draw.line(
                self.image, WHITE,
                (40 + xx * 80, 0 if xx == 0 or xx == 9 else 10 + yy * 60),
                (40 + xx * 80, 600 if xx == 0 or xx == 9 else 50 + yy * 60), 5)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1


all_sprite = pg.sprite.Group()
for r in range(2):
    all_sprite.add(Road(0, 0 if r == 0 else -HEIGHT))
player = Player()
car1 = Car(WIDTH // 2 + 80, HEIGHT // 2, car1_image)
all_sprite.add(car1, player)

game = True
while game:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    screen.fill(GRAY)
    #bg()
    for i in range (2):
        screen.blit(bg_image, bg_image_rect if i == 0 else bg_image_2_rect)
    #screen.blit(bg_image, bg_image_2_rect)
    screen.blit(car1_image, car1.rect)
    screen.blit(play.image, (play.x, play.y))
    pg.display.update()
    clock.tick(FPS)
    pg.display.set_caption(f'Rally   FPS: {int(clock.get_fps())}')

#pg.image.save(screen, 'road.jpg')
