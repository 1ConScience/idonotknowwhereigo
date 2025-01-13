from Class.Character import *
from Class.Bullet import *

class Player(Character):
    def __init__(self):
        super().__init__()  

        self.surf_droite = epsilon_img
        self.surf_gauche = pygame.transform.flip(epsilon_img, True, False)

        self.surf = self.surf_droite
        self.rect = self.surf.get_rect()

        self.armed = False
        self.bullets_direction = 1

        self.zoom = 1

    def display_weapon(self):
        if self.armed:
            weapon_font = pygame.font.SysFont('Times New Roman', 30)
            weapon_surf_droite = weapon_font.render("⌐", False, (0,255,255))
            self.surf_droite.blit(weapon_surf_droite,(12,0))

            weapon_surf_gauche = weapon_font.render("¬", False, (0,255,255))
            self.surf_gauche.blit(weapon_surf_gauche,(0,0))
            

    def get_weapon(self):
        self.armed = True
        self.display_weapon()

    def shot(self):
        if self.armed:
            bullet = Bullet(self.pos.x, self.pos.y, self.bullets_direction)
            all_sprites.add(bullet)
            bullets.add(bullet)

            pygame.mixer.Sound.play(shot_sound)

    def check_collisions(self):
        super().check_collisions()  
        hits_enemies = pygame.sprite.spritecollide(self ,enemies, False)      
        if hits_enemies:
            self.respawn()

    def controllers(self,event):
        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.droite_gauche = -1
            elif axis_pos > deadzone:
                self.droite_gauche = 1
            else:
                self.droite_gauche = 0   

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1:
                self.shot()
            if event.button == 4:
                self.zoom += 0.01
            elif event.button == 5:
                self.zoom -= 0.01

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.droite_gauche = -1
                self.surf = self.surf_gauche
                self.bullets_direction = -1

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite_gauche = 1
                self.surf = self.surf_droite
                self.bullets_direction = 1

            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()

        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.droite_gauche = 0

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite_gauche = 0 

            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:    
            if  event.button == 0:
                self.jump()

        if event.type == pygame.JOYBUTTONUP:    
            if  event.button == 0:
                self.cancel_jump()

        self.display_weapon()

    def respawn(self):
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0, 0))
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.droite_gauche = 0