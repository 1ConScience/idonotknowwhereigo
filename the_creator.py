from Class.MapStructure import *


def gen_level_by_the_creator(x_offset,y_offset):

    image = pygame.image.load("assets/lvldesign.jpg")

    image_width = image.get_width()
    image_height = image.get_height()

    x_len = image_width
    y_len = image_height

    matrice = [[0 for x in range(x_len)] for y in range(y_len)]

    for y in range(y_len):
        for x in range(x_len):
            color = image.get_at((x,y))
            if color == (0,0,0,255):
                matrice[y][x] = 1
                
                bl = BlockHorizontalCol((x_offset+x*20, y_offset+y*20),(0, 255, 255))
                all_sprites.add(bl)
                blocks_horizontal_col.add(bl)

            if color == (255,255,255,255):
                matrice[y][x] = 0



