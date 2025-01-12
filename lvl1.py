from classiq import *

def lvl1():

    insignifiant_txt = Texte("Tu n'es pas si insignifiant Epsilon...",0, 100,(255, 255, 255))
    all_sprites.add(insignifiant_txt)

    PT01 = Platform((1000, 20),(0, 300))
    all_sprites.add(PT01)
    platforms.add(PT01)

    wall = InvisibleWall((510, 170))
    all_sprites.add(wall)
    invisible_walls.add(wall)

    wall2 = InvisibleWall((-510, 170))
    all_sprites.add(wall2)
    invisible_walls.add(wall2)

    P1 = Player()
    all_sprites.add(P1)
    P1.setPosnSpawn(-1000,0)

    safe_zone = Platform((1000, 20),(-1000, 150))
    all_sprites.add(safe_zone)
    platforms.add(safe_zone)

    spanw_txt = Texte("†",P1.spawn.x, P1.spawn.y,(255, 255, 255))
    all_sprites.add(spanw_txt)

    weapon = Texte("⌐",-700, 100,(0, 255, 255))
    all_sprites.add(weapon)

    for i in range(13):
        bot = Bot("psi")
        all_sprites.add(bot)
        enemies.add(bot)

    while 1:
        for event in pygame.event.get():
            P1.controllers(event)
        P1.check_collisions()

        for bot in enemies:
            bot.check_collisions()
            bot.action()

        hit = pygame.sprite.collide_rect(P1, weapon)
        if hit:
            P1.get_weapon()
            weapon.kill()

        screen.fill((0,0,0))
        screen.blit(background, (0,0))

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

        for bullet in bullets: 
            if (bullet.rect.x - camera.x) > WIDTH or (bullet.rect.x - camera.x) < 0:
                bullet.kill()

        pygame.display.update()
        FramePerSec.tick(FPS)