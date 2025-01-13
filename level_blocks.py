from Class.Bot import *
from Class.Bullet import *
from Class.MapStructure import *
from Class.Player import *
from Class.Text import *

def level_blocks():

    PT01 = Platform((3000, 20),(0, 300),(255, 255, 255))
    all_sprites.add(PT01)
    platforms.add(PT01)

    for i in range(10):
        block = Block((i*80, 140),(255, 0, 0))
        all_sprites.add(block)
        blocks.add(block)

    for i in range(2):
        block = Block((4*81, 00-i*80),(255, 0, 0))
        all_sprites.add(block)
        blocks.add(block)

    P1 = Player()
    all_sprites.add(P1)

    spanw_txt = Text("†",P1.spawn.x, P1.spawn.y,(255, 255, 255))
    all_sprites.add(spanw_txt)

    while 1:
        for event in pygame.event.get():
            P1.controllers(event)
        P1.check_collisions()

        screen.fill((0,0,72))

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