from source import tools
from source import const as c
from source import init
from source import info
import pygame

class main_menu():         
    def __init__(self):
        self.game_info = {
            'score': 0,
            'coin': 0,
            'lives': 2
        }
        self.cursor()
        self.start(self.game_info)
    def start(self, game_info):    
        
        self.game_info = {
            'score': 0,
            'coin': 0,
            'lives': 2
        } ##主菜单初始化 game_info
        self.finished=False
        self.next='load'

        self.background=init.pictures['level_1']      #  #背景
        self.background_rect=self.background.get_rect()
        self.background=pygame.transform.scale(
                      self.background,(int(self.background_rect.width*c.back_multi),int(self.background_rect.height*c.back_multi)))
        self.viewport=init.window.get_rect()    ##      视口
        self.caption=tools.get_image(init.pictures['title_screen'],1,60,176,88,c.back_multi,(255,0,220))  #标题
        

        
        self.mario=tools.get_image(init.pictures['mario_bros'],178,32,12,16,c.mario_multi,(0,0,0))    #马里奥
       
        
        self.info=info.info('main_menu',self.game_info)
        pygame.mixer.music.play(-1,0)
    def cursor(self):
        self.cursor=pygame.sprite.Sprite()
        self.cursor.image=tools.get_image(init.pictures['item_objects'],25,160,8,8,c.mario_multi,(0,0,0))     #光标
        rect=self.cursor.image.get_rect()
        rect.x,rect.y=[220,360]
        self.cursor.rect=rect
        self.cursor.state='1'
    def update_cursor(self,keys):
        if keys[pygame.K_UP]:
            self.cursor.state='1'
            self.cursor.rect.y=360
        elif keys[pygame.K_DOWN]:
            self.cursor.state='2'
            self.cursor.rect.y=405
        elif keys[pygame.K_RETURN]:
            self.finished=True

            


    def update(self,surface,keys):

        self.update_cursor(keys)
        surface.blit(self.background,(0,0))   
        surface.blit(self.caption,(170,100))
        surface.blit(self.cursor.image,self.cursor.rect)
        surface.blit(self.mario,(110,490))
        self.info.draw(surface)
    def reset_game_info(self):
        self.game_info.update({
            'score': 0,
            'coin': 0,
            'lives': 3

        })