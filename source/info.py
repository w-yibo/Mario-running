import pygame
from source import tools
from source import init
from source import const as c

class info:
    def __init__(self,state,game_info):
        self.state=state   ##传递状态
        self.game_info = game_info
        self.creat_info()
        self.creat_begin()
    def creat_words(self,words,size=40,wid_scale=1.25,hei_scale=1):       ##创建文字图片的方法
        my_font=pygame.font.SysFont('Centaur.ttf',size)
        words_image=my_font.render(words,True,(255,255,255))
        words_rect=words_image.get_rect()
        words_image=pygame.transform.scale(words_image,(int(words_rect.width*wid_scale),int(words_rect.height*hei_scale))) 
        return words_image 

    def creat_begin(self):                         #关卡特有信息
        self.begin=[]
        if self.state=='main_menu':
            self.begin.append((self.creat_words('1 PLAYER GAME'),(272,360)))
            self.begin.append((self.creat_words('2 PLAYER GAME'),(272,405)))
            self.begin.append((self.creat_words('Lets play the game!'),(290,465)))
        
        if self.state=='load':
            self.begin.append((self.creat_words('LEVEL'),(280,200)))
            self.begin.append((self.creat_words('1-1'),(430,200)))
            self.begin.append((self.creat_words('X    {}'.format(self.game_info['lives'])), (380, 280)))
            self.mario=tools.get_image(init.pictures['mario_bros'],178,32,12,16,c.mario_multi,(0,0,0))    #马里奥
        if self.state=='gameover':
            self.begin.append((self.creat_words('GAME OVER'),(280,300)))
        if self.state=='win':
            self.begin.append((self.creat_words('W I N !!!'),(280,300)))


    def creat_info(self):                          #游戏一直存在的文字信息 
        self.info=[]
        self.info.append((self.creat_words('MARIO'),(75,30)))
        self.info.append((self.creat_words('PARKOUR'),(450,30)))
        self.info.append((self.creat_words('X0'),(300,55)))
        self.info.append((self.creat_words('0'),(75,55)))
        self.info.append((self.creat_words('1 - 1'),(480,55)))
        self.gold=tools.get_image(init.pictures['item_objects'],1,160,5,8,c.mario_multi,(0,0,0))   #
    def update_info(self,game_info):
        self.info[2]=((self.creat_words('X{}'.format(game_info['coin'])),(300,55)))
        self.info[3]=((self.creat_words('{}'.format(game_info['score'])),(75,55)))
        

    #def update(self):
    def draw(self,surface):
        for word in self.begin:
            surface.blit(word[0],word[1])
        for word in self.info:
            surface.blit(word[0],word[1])
        if self.state=='load':
            surface.blit(self.mario,(300,270))
        surface.blit(self.gold,(280,58))

    
    


