import pygame
from source import tools
from source import const as c
from source import init

class coin(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        self.image=tools.get_image(init.pictures['item_objects'],1,160,5,8,c.coin_multi,(0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.bottom=y-100
        self.name=name
class enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        self.image=tools.get_image(init.pictures['enemies'],0,16,15,15,c.enemy_multi,(0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.bottom=y
        self.name=name
 
class brick(pygame.sprite.Sprite):
    def __init__(self,x,y,name):
        pygame.sprite.Sprite.__init__(self)
        self.image=tools.get_image(init.pictures['tile_set'],15,0,15,15,c.brick_multi,(0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.name=name
  
    

