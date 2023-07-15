import pygame
import os
from source import const as c
from state import main_menu,load,play


class Game:
    def __init__(self,state_dict,begin_state):  ##构造函数
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()
        self.keys = pygame.key.get_pressed()
        self.state_dict = state_dict
        self.state = self.state_dict[begin_state] 

    
    def start(self):
        # 游戏主循环
       
        while True:
            ##事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()    ##游戏退出
                elif event.type == pygame.KEYDOWN:
                    self.keys = pygame.key.get_pressed()
                elif event.type == pygame.KEYUP:
                    self.keys = pygame.key.get_pressed()
            self.update()
            
            
            # 刷新画面
            pygame.display.update()
            self.clock.tick(60) # 通过时钟对象指定循环频率

    def update(self):
        if self.state.finished:
            game_info = self.state.game_info  #######
            next_state = self.state.next
            self.state.finished = False
            self.state = self.state_dict[next_state]
            self.state.start(game_info)
        self.state.update(self.screen, self.keys)


def load_image(path):
    pictures={}
    for pic in os.listdir(path):
      name,ext=os.path.splitext(pic)   ##分割成文件名和后缀
      img=pygame.image.load(os.path.join(path,pic))
      pictures[name]=img
    return pictures
def get_image(pic,x,y,width,height,scale,color):  ##获取图片的某部分
    image=pygame.Surface((width,height))   
    image.blit(pic,(0,0),(x,y,width,height))   ##(0,0)表示起始坐标，x,y,width,height，表示截取图片的位置
    image.set_colorkey(color)
    image=pygame.transform.scale(image,(int(width*scale),int(height*scale)))
    return image
