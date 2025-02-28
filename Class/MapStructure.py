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
 
class BlockHorizontalCol(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        super().__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass
 
class BlockVerticalCol(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        super().__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((0,255,255))
        self.rect = self.surf.get_rect(center = pos)

    def update(self):
        pass