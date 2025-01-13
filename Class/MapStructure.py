from head import *

class Platform(pygame.sprite.Sprite):
    def __init__(self,size,pos,color):
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
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
 
class Block(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        super().__init__()
        self.surf = pygame.Surface((80,80))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass