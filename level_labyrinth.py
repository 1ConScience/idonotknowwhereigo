from Class.Bot import *
from Class.Bullet import *
from Class.MapStructure import *
from Class.Player import *
from Class.Text import *

def gen_labyrinth_createdbycopilot(x,y):
    for i in range(10):
        block_horizontal_col = BlockHorizontalCol((x, y+i*20),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+100, y+i*20),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x-100, y+i*20),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y+100),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y-100),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y+200),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y-200),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+200, y+i*20),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x-200, y+i*20),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    randdir = random.randint(0,3)
    if randdir == 0:
        for i in range(10):
            block_horizontal_col = BlockHorizontalCol((x, y+i*20),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
            
            block_horizontal_col = BlockHorizontalCol((x+100, y+i*20),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
    elif randdir == 1:
        for i in range(10):
            block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
            
            block_horizontal_col = BlockHorizontalCol((x+i*20, y+100),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
    elif randdir == 2:
        for i in range(10):
            block_horizontal_col = BlockHorizontalCol((x, y+i*20),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
            
            block_horizontal_col = BlockHorizontalCol((x-100, y+i*20),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
    elif randdir == 3:
        for i in range(10):
            block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)
            
            block_horizontal_col = BlockHorizontalCol((x+i*20, y-100),(255, 255, 255))
            all_sprites.add(block_horizontal_col)
            blocks_horizontal_col.add(block_horizontal_col)


    for i in range(10):
        block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
        
        block_horizontal_col = BlockHorizontalCol((x+i*20, y-100),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)









#╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗╔═╗   ╔ ═ ╗ ╚═╗ ╔═╗ ╔═╗
def gen_coin_hautdroite(x,y):
    for i in range(5):   
        block_vertical_col = BlockVerticalCol((x, y+i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x-i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)

def gen_coin_hautgauche(x,y):
    for i in range(5):   
        block_vertical_col = BlockVerticalCol((x, y+i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)

def gen_coin_basgauche(x,y):
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x+i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x, y-i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)

def gen_coin_basdroite(x,y):
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x-i*20, y),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x, y-i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)


def gen_mur_vertical(x,y):
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x-50, y-i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x+50, y-i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x-50, y+i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)
    for i in range(5):
        block_vertical_col = BlockVerticalCol((x+50, y+i*20),(255, 255, 255))
        all_sprites.add(block_vertical_col)
        blocks_vertical_col.add(block_vertical_col)

def gen_mur_horizontal(x,y):
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x-i*20, y+50),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x-i*20, y-50),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x+i*20, y+50),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)
    for i in range(5):
        block_horizontal_col = BlockHorizontalCol((x+i*20, y-50),(255, 255, 255))
        all_sprites.add(block_horizontal_col)
        blocks_horizontal_col.add(block_horizontal_col)


def gen_labyrinthLOLPRISON(x,y):
    gen_coin_basdroite(x+200,y+200) 
    gen_coin_basgauche(x-200,y+200)
    gen_coin_hautdroite(x+200,y-200)
    gen_coin_hautgauche(x-200,y-200)
    gen_mur_horizontal(x,y)
    gen_mur_vertical(x,y)

def gen_labyrinth(x,y):

    gen_mur_horizontal( x,                      y)
    gen_coin_hautdroite(x+180,                  y-50) 
    gen_mur_vertical(   x+180-50,               y-50+180)
    gen_coin_basgauche( x+180-50-50,            y-50+180+180)
    gen_mur_horizontal( x+180-50-50+180,        y-50+180+180-50)
    gen_coin_basdroite( x+180-50-50+180+180,    y-50+180+180-50+50)
    gen_mur_vertical(   x+180-50-50+180+180-50, y-50+180+180-50+50-180)




def level_labyrinth():

    PT01 = Platform((100, 20),(0, 300),(0, 0, 0))
    all_sprites.add(PT01)
    platforms.add(PT01)

    #gen_labyrinth_createdbycopilot(50,50)

    gen_labyrinth(125,250)

    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Text("†",P1.spawn.x, P1.spawn.y,(255, 255, 255))
    all_sprites.add(spanw_txt)

    blood_txt = Text("+200... +200... Toujours plus de...",0, +150,(255, 255, 255))
    all_sprites.add(blood_txt)

    while 1:
        for event in pygame.event.get():
            P1.controllers(event)
        P1.check_collisions()

        screen.fill((127,0,0))

        camera.x = P1.pos.x*P1.zoom - WIDTH/2
        camera.y = P1.pos.y*P1.zoom - HEIGHT/2
        
        for entity in all_sprites:
            entity.update()

            surf_entity_scaled = pygame.transform.scale(entity.surf, (int(entity.rect.width*P1.zoom), int(entity.rect.height*P1.zoom)))
            
            screen.blit(surf_entity_scaled, (entity.rect.x*P1.zoom - camera.x, entity.rect.y*P1.zoom - camera.y))

        if (P1.rect.y*P1.zoom - camera.y) > HEIGHT:
            P1.respawn()

        pygame.display.update()
        FramePerSec.tick(FPS)