from head import *

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

