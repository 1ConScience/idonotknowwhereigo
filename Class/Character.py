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
        hits_platforms = pygame.sprite.spritecollide(self, platforms, False)
        hits_blocks = pygame.sprite.spritecollide(self, blocks, False)
        if (hits_platforms or hits_blocks) and not self.jumping:
            self.jumping = True
            self.vel.y = -15
 
    def cancel_jump(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3
 
    def check_collisions(self):
        #platforms collisions
        hits_platforms = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits_platforms:
                if self.pos.y < hits_platforms[0].rect.bottom:               
                    self.pos.y = hits_platforms[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False

        #blocks collisions
        hits_blocks = pygame.sprite.spritecollide(self ,blocks, False)
        if hits_blocks:
            if self.rect.bottom < hits_blocks[0].rect.centery: 
                if self.vel.y > 0:         
                    self.pos.y = hits_blocks[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False
            if self.rect.top > hits_blocks[0].rect.centery:  
                if self.vel.y < 0:         
                    self.cancel_jump()


            if self.rect.right < hits_blocks[0].rect.centerx and self.pos.y != hits_blocks[0].rect.top+1: 
                if self.vel.x > 0:         
                    self.vel.x = 0
            if self.rect.left > hits_blocks[0].rect.centerx and self.pos.y != hits_blocks[0].rect.top+1:  
                if self.vel.x < 0:         
                    self.vel.x = 0
