from head import *

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.DroiteGauche = 0

    def update(self):
        self.acc = vec(0,0.5)
                
        if self.DroiteGauche == -1:
            self.acc.x = -ACC
        if self.DroiteGauche == 1:
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

    def check_collisions(self):
        super().check_collisions()  
        hits = pygame.sprite.spritecollide(self ,InvisibleWalls, False)      
        if self.vel.x > 0:        
            if hits:
                if self.pos.x < hits[0].rect.right:               
                    self.pos.x = hits[0].rect.left -1
                    self.vel.x = 0
                    self.jumping = False
                    self.DroiteGauche = -1
        if self.vel.x < 0:        
            if hits:
                if self.pos.x > hits[0].rect.left:               
                    self.pos.x = hits[0].rect.right +1
                    self.vel.x = 0
                    self.jumping = False
                    self.DroiteGauche = 1

    def action(self):
        status= random.randint(1, 5)
        match status:
            case 1:
                self.DroiteGauche = 1
                self.surf = psi_img 
            case 2:
                self.DroiteGauche = -1
                self.surf = pygame.transform.flip(psi_img, True, False)
            case 3:
                self.DroiteGauche = 0
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
            #self.respawn()
            pass

    def controllers(self,event):
        if pygame.joystick.get_count()>0:
            axis_pos = joysticks[0].get_axis(0)

            if axis_pos < -1 * deadzone:
                self.DroiteGauche = -1
            elif axis_pos > deadzone:
                self.DroiteGauche = 1
            else:
                self.DroiteGauche = 0   

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.DroiteGauche = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.DroiteGauche = 1
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.jump()
        if event.type == pygame.KEYUP:   
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.DroiteGauche = 0
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.DroiteGauche = 0 
            if event.key == pygame.K_SPACE or event.key == pygame.K_z or event.key == pygame.K_UP:
                self.cancel_jump()

        if event.type == pygame.JOYBUTTONDOWN:    
            if  event.button == 0:
                self.jump()
        if event.type == pygame.JOYBUTTONUP:    
            if  event.button == 0:
                self.cancel_jump()

        if self.DroiteGauche == -1:
            self.surf = pygame.transform.flip(epsilon_img, True, False)
        if self.DroiteGauche == 1:
            self.surf = epsilon_img

    def respawn(self):
        self.rect = self.surf.get_rect()
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.DroiteGauche = 0    
 
class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
 
class InvisibleWall(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.surf = pygame.Surface(size)
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