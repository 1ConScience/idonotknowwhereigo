from classiq import *

def lvl1():
    P1 = Player()
    all_sprites.add(P1)

    for i in range(5):
        bot = Bot("psi")
        all_sprites.add(bot)
        enemies.add(bot)

    PT01 = Platform((1000, 20),(0, 300))
    all_sprites.add(PT01)
    platforms.add(PT01)

    while 1:
        for event in pygame.event.get():
            P1.controllers(event)
        P1.check_collisions()

        for bot in enemies:
            bot.check_collisions()
            bot.action()

        screen.fill((0,0,0))

        camera.x = P1.pos.x - WIDTH/2
        camera.y = P1.pos.y - HEIGHT/2
        
        for entity in all_sprites:
            entity.update()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        if (P1.rect.y - camera.y) > HEIGHT:
            P1.respawn()

        for bot in enemies: 
            if (bot.rect.y - camera.y) > HEIGHT:
                bot.kill()

        pygame.display.update()
        FramePerSec.tick(FPS)