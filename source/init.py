import pygame
from source import const as c
import os
from source import tools
def load_image(path):
    pictures={}
    for pic in os.listdir(path):
      name,ext=os.path.splitext(pic)   ##分割成文件名和后缀
      img=pygame.image.load(os.path.join(path,pic))
      pictures[name]=img
    return pictures
pygame.init() 
pygame.mixer.init()
window=pygame.display.set_mode((c.window_width,c.window_height))  
pygame.display.set_caption("马里奥跑酷")
pygame.mixer.music.load('resources/music/main_theme.ogg')
pictures=load_image('resources/graphics')  ##加载图片
