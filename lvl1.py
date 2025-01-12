from classiq import *

def lvl1():
    P1 = Player()
    all_sprites.add(P1)

    PT01 = Platform((500, 20),(0, 300))
    all_sprites.add(PT01)
    platforms.add(PT01)

    while 1:

        #quand P1 entre en collision avec platforms
        P1.update()

        for event in pygame.event.get():
            P1.controls(event)

        P1.joystick()

        #fond noir
        screen.fill((255,255,255))

        #ajust camera
        camera.x = P1.pos.x - WIDTH/2
        camera.y = P1.pos.y - HEIGHT/2
        
        #deplacer les sprites 
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        if (P1.rect.y - camera.y) > HEIGHT:
            P1.into_the_void()

        pygame.display.update()
        FramePerSec.tick(FPS)