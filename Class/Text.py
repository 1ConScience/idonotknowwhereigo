from head import *

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,x,y,color):
        super().__init__()
        my_font = pygame.font.SysFont('Times New Roman', 30)
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self):
        pass