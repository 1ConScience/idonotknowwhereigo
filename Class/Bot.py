from Class.Character import *

class Bot(Character):
    def __init__(self, model, pos):
        super().__init__() 
        if model == "psi":
            self.surf = psi_img  
        self.rect = self.surf.get_rect()

        self.pos = pos

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
