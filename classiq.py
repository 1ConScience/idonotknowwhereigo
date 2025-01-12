from head import *

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.droite_gauche = 0

    def setPosnSpawn(self,x,y):
        self.pos = vec((x,y))
        self.spawn = vec((x,y))
        self.rect.midbottom = vec((x,y))

    def update(self):
        self.acc = vec(0,0.5)
                
        if self.droite_gauche == -1:
            self.acc.x = -ACC
        if self.droite_gauche == 1:
            self.acc.x = ACC
                 
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
 
    def jump(self): 
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -15
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def check_collisions(self):
        hits_platforms = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits_platforms:
                if self.pos.y < hits_platforms[0].rect.bottom:               
                    self.pos.y = hits_platforms[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

class Bot(Personnage):
    def __init__(self, model):
        super().__init__() 
        if model == "psi":
            self.surf = psi_img  
        self.rect = self.surf.get_rect()

    def check_collisions(self):
        super().check_collisions()  
        hits_invisible_walls = pygame.sprite.spritecollide(self ,invisible_walls, False)      
        if self.vel.x > 0:        
            if hits_invisible_walls:
                if self.pos.x < hits_invisible_walls[0].rect.right:               
                    self.pos.x = hits_invisible_walls[0].rect.left -1
                    self.vel.x = 0
                    self.jumping = False
                    self.droite_gauche = -1
        if self.vel.x < 0:        
            if hits_invisible_walls:
                if self.pos.x > hits_invisible_walls[0].rect.left:               
                    self.pos.x = hits_invisible_walls[0].rect.right +1
                    self.vel.x = 0
                    self.jumping = False
                    self.droite_gauche = 1

        hits_bullets = pygame.sprite.spritecollide(self ,bullets, False)      
        if hits_bullets:
            self.kill()
            hits_bullets[0].kill()
            pass

    def action(self):
        status= random.randint(1, 5)
        match status:
            case 1:
                self.droite_gauche = 1
                self.surf = psi_img 
            case 2:
                self.droite_gauche = -1
                self.surf = pygame.transform.flip(psi_img, True, False)
            case 3:
                self.droite_gauche = 0
            case 4:
                self.jump()
            case 5:
                self.cancel_jump()

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullets_direction):
        super().__init__()  

        my_font = pygame.font.SysFont('Times New Roman', 15)
        col = pygame.Color(0, 0, 0)
        col.hsva = (random.randrange(0, 360), 100, 100, 100)

        self.surf = my_font.render(str(random.randrange(0, 9)), False, col)
        self.rect = self.surf.get_rect()

        self.direction = bullets_direction

        y = y - 25
        if self.direction == -1: 
            x = x - 15
        if self.direction == 1: 
            x = x + 15

        self.pos = vec((x, y))

    def update(self):
        if self.direction == -1:
            self.pos.x += -20
        if self.direction == 1:
            self.pos.x += 20

        self.rect.center = self.pos

class Player(Personnage):
    def __init__(self):
        super().__init__()  
        self.surf = epsilon_img
        self.rect = self.surf.get_rect()

        self.armed = False
        self.bullets_direction = 1
        self.shooting = False

    def display_weapon(self):
        if self.armed:
            weapon_font = pygame.font.SysFont('Times New Roman', 30)
            weapon_surf = weapon_font.render("⌐", False, (0,255,255))
            self.surf.blit(weapon_surf,(20,0))

    def get_weapon(self):
        self.armed = True
        self.display_weapon()

    def shot(self):
        if self.armed and self.shooting:
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
            self.shooting = True
        if event.type == pygame.MOUSEBUTTONUP :
            self.shooting = False

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.droite_gauche = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite_gauche = 1
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

        if self.droite_gauche == -1:
            self.surf = pygame.transform.flip(epsilon_img, True, False)
            self.bullets_direction = -1
        if self.droite_gauche == 1:
            self.surf = epsilon_img
            self.bullets_direction = 1

    def respawn(self):
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0, 0))
        self.pos = vec((0, 0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.droite_gauche = 0
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
 
class InvisibleWall(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        image = pygame.Surface([20,240], pygame.SRCALPHA, 32)
        self.surf = image.convert_alpha()
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
    
class Texte(pygame.sprite.Sprite):
    def __init__(self,txt,x,y,color):
        super().__init__()
        my_font = pygame.font.SysFont('Times New Roman', 30)
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self):
        pass