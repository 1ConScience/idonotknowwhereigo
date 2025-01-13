from head import *

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,x,y,color):
        super().__init__()
        my_font = pygame.font.SysFont('Times New Roman', 30)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = (x, y))
    def move(self):
        pass

class ButterflyText(pygame.sprite.Sprite):
    def __init__(self,x,y,color):
        super().__init__()
        
        image = pygame.Surface([520,360], pygame.SRCALPHA, 32)
        self.surf = image.convert_alpha()
        self.rect = self.surf.get_rect(center = (x, y))

        list_of_text = []
        list_of_text.append("                `         '                ")
        list_of_text.append(";,,,             `       '             ,,,;")
        list_of_text.append("`YESXXXXbo.       :     :       .od8888YES'")
        list_of_text.append("  888IO8DO88b.     :   :     .d8888I8DO88  ")
        list_of_text.append("  8DEATH'  `Y8b.   `   '   .d8Y'  `DEATH8  ")
        list_of_text.append(" jTHEE!  .db.  Yb. '   ' .dY  .db.  8THEE! ")
        list_of_text.append("   `772  Y88Y    `b ( ) d'    Y88Y  888'   ")
        list_of_text.append("    8MYb  '`        ,',        ''  dMY8    ")
        list_of_text.append("   j8prECIOUSgf`'   ':'   `'?g8prECIOUSk   ")
        list_of_text.append("     'Y'   .7'     d' 'b     '2.   'Y'     ")
        list_of_text.append("      !   .7' db  d'; ;`b  db '7.   !      ")
        list_of_text.append("         d88  `'  2 ; ; 7  `'  88b         ")
        list_of_text.append("        d88Ib   .g8 ',' 8g.   dI88b        ")
        list_of_text.append("       :88DEATH88Y'     'Y88LOVE888:       ")
        list_of_text.append("       '! THEE888'       `888THEE !'       ")
        list_of_text.append("          '8Y  `Y         Y'  Y8'          ")
        list_of_text.append("           Y                   Y           ")
        list_of_text.append("           !                   !           ")

        my_font = pygame.font.SysFont('Lucida Console', 20)

        for i in range(len(list_of_text)):
            txt = list_of_text[i]
            txt_surf = my_font.render(txt, True, color)
            self.surf.blit(txt_surf, (0, i*20))

    def move(self):
        pass

