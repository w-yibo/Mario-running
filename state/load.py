from source import info
from source import init
import pygame

class load:
    def start(self,game_info):
        self.game_info = game_info
        self.game_info['score']=0
        self.game_info['coin']=0
        self.finished=False
        self.next='play'
        self.timer=0
        self.info=info.info('load',self.game_info)

    def update(self,surface,keys):
        self.draw(surface)
        if self.timer==0:
            self.timer=pygame.time.get_ticks()   ##获取当前游戏进行时间
        elif pygame.time.get_ticks()-self.timer>3000:
            self.finished=True
            self.timer=0
    
    def draw(self,surface):
        surface.fill((0,0,0)) ##黑色
        self.info.draw(surface)

class gameover():
    def start(self,game_info):
        self.game_info = game_info
        self.finished=False
        self.next='main_menu'
        self.timer=0
        self.info=info.info('gameover',self.game_info)
        pygame.mixer.music.stop()
        game_over_bgm=pygame.mixer.Sound('resources/music/game_over.ogg')
        game_over_bgm.play()

    def update(self,surface,keys):
        self.draw(surface)
        if self.timer==0:
            self.timer=pygame.time.get_ticks()   ##获取当前游戏进行时间
        elif pygame.time.get_ticks()-self.timer>6000:
            self.finished=True
            self.timer=0

    
    def draw(self,surface):
        surface.fill((0,0,0)) ##黑色
        self.info.draw(surface)
class win():
    def start(self,game_info):
        self.game_info = game_info
        self.finished=False
        self.next='main_menu'
        self.timer=0
        self.info=info.info('win',self.game_info)
        pygame.mixer.music.stop()
        game_over_bgm=pygame.mixer.Sound('resources/music/world_clear.wav')
        game_over_bgm.play()
    def update(self,surface,keys):
        self.draw(surface)
        if self.timer==0:
            self.timer=pygame.time.get_ticks()   ##获取当前游戏进行时间
        elif pygame.time.get_ticks()-self.timer>6000:
            self.finished=True
            self.timer=0
    def draw(self,surface):
        surface.fill((0,0,0)) ##黑色
        self.info.draw(surface)