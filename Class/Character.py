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
        hits_blocks_horizontal_col = pygame.sprite.spritecollide(self, blocks_horizontal_col, False)
        if (hits_platforms or hits_blocks_horizontal_col) and not self.jumping:
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


        #blocks_horizontal_col collisions
        hits_blocks_horizontal_col = pygame.sprite.spritecollide(self ,blocks_horizontal_col, False)
        if hits_blocks_horizontal_col:

            #si on est en train de sauter
            if self.vel.y < 0:   
                #si on touche le bas d'un block avec sa tête
                if self.rect.top > hits_blocks_horizontal_col[0].rect.top: 
                    #on annule le saut
                    self.cancel_jump() 

            #si on est en train de tomber
            if self.vel.y > 0:        
                #si on touche le haut d'un block avec ses pieds	
                if self.rect.bottom < hits_blocks_horizontal_col[0].rect.bottom: 
                    #on annule la chute
                    self.pos.y = hits_blocks_horizontal_col[0].rect.top +1
                    self.vel.y = 0
                    self.jumping = False


        #BlockHorizontalCol collisions
        hits_blocks_vertical_col = pygame.sprite.spritecollide(self ,blocks_vertical_col, False)
        '''if self.vel.x > 0:        
            if hits_blocks_vertical_col:
                if self.rect.right < hits_blocks_vertical_col[0].rect.right:    
                    self.vel.x = 0
        if self.vel.x < 0:        
            if hits_blocks_vertical_col:
                if self.rect.left > hits_blocks_vertical_col[0].rect.left:    
                    self.vel.x = 0'''


        if self.vel.x > 0:        
            if hits_blocks_vertical_col:
                if self.pos.x < hits_blocks_vertical_col[0].rect.right:               
                    self.pos.x = hits_blocks_vertical_col[0].rect.left -1
                    self.vel.x = 0
        if self.vel.x < 0:        
            if hits_blocks_vertical_col:
                if self.pos.x > hits_blocks_vertical_col[0].rect.left:               
                    self.pos.x = hits_blocks_vertical_col[0].rect.right +1
                    self.vel.x = 0

