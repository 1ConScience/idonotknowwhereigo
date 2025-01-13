from Class.Bot import *
from Class.Bullet import *
from Class.Platform_Wall import *
from Class.Player import *
from Class.Text import *

def generateHellZone(x_offet, y_offset):
    hell_zone = Platform((1000, 20),(1200+x_offet, 300+y_offset),(255, 255, 255))
    all_sprites.add(hell_zone)
    platforms.add(hell_zone)

    wall = InvisibleWall((510+1200+x_offet, 170+y_offset))
    all_sprites.add(wall)
    invisible_walls.add(wall)

    wall2 = InvisibleWall((-510+1200+x_offet, 170+y_offset))
    all_sprites.add(wall2)
    invisible_walls.add(wall2)

    for i in range(21):
        bot = Bot("psi",vec((1200+x_offet,0+y_offset)))
        all_sprites.add(bot)
        enemies.add(bot)

def level_blue_basic_camera_test():

    insignifiant_txt = Text("Tu n'es pas si insignifiant Epsilon...",0, 100,(255, 255, 255))
    all_sprites.add(insignifiant_txt)

    butterfly_txt = ButterflyText(1900, -50,(255, 255, 255))
    all_sprites.add(butterfly_txt)

    PT01 = Platform((1000, 20),(0, 300),(255, 255, 255))
    all_sprites.add(PT01)
    platforms.add(PT01)

    P1 = Player()
    all_sprites.add(P1)

    safe_zone = Platform((500, 20),(-750, 150),(0, 0, 0))
    all_sprites.add(safe_zone)
    platforms.add(safe_zone)

    spanw_txt = Text("†",P1.spawn.x, P1.spawn.y,(255, 255, 255))
    all_sprites.add(spanw_txt)

    weapon = Text("⌐",-700, 100,(0, 255, 255))
    all_sprites.add(weapon)

    for i in range(1):
        generateHellZone(1200*i, 150*i-150)

    while 1:
        for event in pygame.event.get():
            P1.controllers(event)
        P1.check_collisions()

        for bot in enemies:
            bot.check_collisions()
            bot.action()

        if not P1.armed:
            hit = pygame.sprite.collide_rect(P1, weapon)
            if hit:
                P1.get_weapon()
                weapon.kill()

        screen.fill((0,0,72))

        camera.x = P1.pos.x - WIDTH/2
        camera.y = P1.pos.y - HEIGHT/2
        
        for entity in all_sprites:
            entity.update()
            screen.blit(entity.surf, (entity.rect.x - camera.x, entity.rect.y - camera.y))

        if (P1.rect.y - camera.y) > HEIGHT:
            P1.respawn()

        for bot in enemies: 
            if (bot.rect.y - camera.y) > HEIGHT:
                #bot.kill()
                pass

        for bullet in bullets: 
            if (bullet.rect.x - camera.x) > WIDTH or (bullet.rect.x - camera.x) < 0:
                bullet.kill()

        pygame.display.update()
        FramePerSec.tick(FPS)