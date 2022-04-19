import pygame
from random import randint
pygame.init()

white = (255,255,255)
base_values = [1,2,4]
colors = {1:(255,255,255),2:(253,232,93),4:(255,118,0),8:(255,100,100),16:(255,118,0),32:(255,255,0),64:(255,0,128),128:(255,128,0)}

class Tile:
    '''Описание как работает 1 клеточка'''
    def __init__(self,x,y,value):
        tiles.append(self)
        self.rect = pygame.Rect(x*50,y*50,50,50)
        self.color = colors[value]
        self.value = value
        self.value_txt = tile_font.render(str(self.value),False,(0,0,0))

    def draw(self):
        pygame.draw.rect(win,self.color,self.rect)
        win.blit(self.value_txt,(self.rect.x+10,self.rect.y))

    def move(self,horizontal,verticle):
        if horizontal == 1:
            while self.rect.x < 450:
                self.rect.x += horizontal*50
                if self.check_collide():
                    self.rect.x -= horizontal*50
                    break

        if horizontal == -1:
            while self.rect.x > 0:
                self.rect.x += horizontal*50
                if self.check_collide():
                    self.rect.x -= horizontal*50
                    break

        if verticle == 1:
            while self.rect.y < 450:
                
                self.rect.y += verticle*50
                if self.check_collide():
                    self.rect.y -= verticle*50
                    break

        if verticle == -1:
            while self.rect.y > 0:
                self.rect.y += verticle*50
                if self.check_collide():
                    self.rect.y -= verticle*50
                    break

        if self.rect.x < 0: self.rect.x = 0
        if self.rect.x > 450: self.rect.x = 450
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.y > 450: self.rect.y = 450

    def check_collide(self):
        for tile in tiles:
            if tile is self: continue
            if self.rect.x == tile.rect.x:
                if self.rect.y == tile.rect.y:
                    if self.value == tile.value:
                        summ_two_tile(self,tile)
                    else:
                        return 1
        return 0

def summ_two_tile(tile1,tile2):
    tile1.value += tile2.value
    tile1.color = colors[tile1.value]
    tile1.value_txt = tile_font.render(str(tile1.value),False,(0,0,0))
    tiles.remove(tile2)

    if len(tiles) < 20:
        spawn_new()

def spawn_new():
    might = 0
    while not might:
        new_x = randint(0,10)
        new_y = randint(0,10)
        might = 1
        for tile in tiles:
            if tile.rect.x == new_x%50 and tile.rect.y == new_y%50:
                might = 0

    tiles.append(Tile(new_x,new_y,base_values[randint(0,2)]))

win = pygame.display.set_mode((500,500))

timer = pygame.time.Clock()
pygame.font.init()
tile_font = pygame.font.Font(None,72)

tiles = []
for i in range(7):
    spawn_new()


def move_tiles_right():
    for tile in tiles:
        tile.move(1,0)

def move_tiles_left():
    for tile in tiles:
        tile.move(-1,0)

def move_tiles_up():
    for tile in tiles:
        tile.move(0,-1)

def move_tiles_down():
    for tile in tiles:
        tile.move(0,1)

while True:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d or e.key == pygame.K_RIGHT:
                move_tiles_right()
            if e.key == pygame.K_a or e.key == pygame.K_LEFT:
                move_tiles_left()

            if e.key == pygame.K_w or e.key == pygame.K_UP:
                move_tiles_up()

            if e.key == pygame.K_s or e.key == pygame.K_DOWN:
                move_tiles_down()

    win.fill(white)
    for tile in tiles:
        tile.draw()

    win.update()
    timer.tick(30)
