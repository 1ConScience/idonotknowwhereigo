from head import *

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.gauche = False
        self.droite = False

    def update(self):
        self.acc = vec(0,0.5)
                
        if self.gauche:
            self.acc.x = -ACC
        if self.droite:
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
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                if self.pos.y < hits[0].rect.bottom:               
                    self.pos.y = hits[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

class Bot(Personnage):
    def __init__(self, model):
        super().__init__() 
        if model == "psi":
            self.surf = psi_img  
        self.rect = self.surf.get_rect()

    def action(self):
        status= random.randint(1, 5)
        match status:
            case 1:
                self.droite = True 
                self.gauche = False 
                self.surf = psi_img 
            case 2:
                self.gauche = True
                self.droite = False
                self.surf = pygame.transform.flip(psi_img, True, False)
            case 3:
                self.droite = False
                self.gauche = False
            case 4:
                self.jump()
            case 5:
                self.cancel_jump()

class Player(Personnage):
    def __init__(self):
        super().__init__()  
        self.surf = epsilon_img
        self.rect = self.surf.get_rect()

    def check_collisions(self):
        super().check_collisions()  
        hits = pygame.sprite.spritecollide(self ,enemies, False)      
        if hits:
            self.respawn()

    def controllers(self,event):
        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.gauche = True
            elif axis_pos > deadzone:
                self.droite = True  
            else:
                self.gauche = False
                self.droite = False     

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = True
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = True  
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.gauche = False
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.droite = False 
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:      
            if  event.button == 4:
                self.gauche = True
            if  event.button == 5:
                self.droite = True  
            if  event.button == 0:
                self.jump()
        if event.type == pygame.JOYBUTTONUP:      
            if  event.button == 4:
                self.gauche = False
            if  event.button == 5:
                self.droite = False 
            if  event.button == 0:
                self.cancel_jump()

        if self.gauche:
            self.surf = pygame.transform.flip(epsilon_img, True, False)
        if self.droite:
            self.surf = epsilon_img

    def respawn(self):
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.gauche = False
        self.droite = False     
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
