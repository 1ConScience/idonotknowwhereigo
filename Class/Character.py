from head import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
   
        self.spawn = vec((0,0))
        self.pos = vec((0,0))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False

        self.droite_gauche = 0

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