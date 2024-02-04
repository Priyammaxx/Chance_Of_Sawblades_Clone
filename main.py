import pygame as pg 
import sys
from player import Player

pg.init()

WIDTH, HEIGHT = 600, 600
Screen = pg.display.set_mode((WIDTH, HEIGHT))

clock = pg.time.Clock()
FPS = 60

GRAY = (150, 150, 150)
player_size = 50
Box = pg.Rect(WIDTH/2, HEIGHT/2, player_size, player_size)

player = Player(Box, 10, 210)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    key = pg.key.get_pressed()
    if key[pg.K_LEFT] and player.sprite.x > 0:
        player.move_left()
    elif key[pg.K_RIGHT] and player.sprite.x < WIDTH - player_size:
        player.move_right()

    if key[pg.K_UP] and player.current_height < player.jump_height:
        player.jump(20)
    elif player.sprite.y + player_size < HEIGHT:
        player.fall(10)

    if player.sprite.y + 50 >= 600:
        player.current_height = 0

    Screen.fill(GRAY)

    pg.draw.rect(Screen, 'red', player.sprite, 0)
    pg.display.update()
    clock.tick(FPS)

