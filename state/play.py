from source import tools
from source import const as c
from source import init
from source import info
from sprite import player,item,useful
import pygame

class play:
    def start(self, game_info):
        
        self.game_info = game_info
        self.info = info.info('play', self.game_info)
        self.finished=False
        self.win=False
        self.next='gameover'
        self.setup_maps()
        self.background=init.pictures['level_1']      #  #背景
        self.background_rect=self.background.get_rect()
        self.background=pygame.transform.scale(
                      self.background,(int(self.background_rect.width*c.back_multi),int(self.background_rect.height*c.back_multi)))
       
        self.game_ground=pygame.Surface((self.background_rect.width*c.back_multi,self.background_rect.height*c.back_multi))
       
        self.setup_player()
        self.viewport=init.window.get_rect()    ##      视口

        self.end_x= 9086

        self.setup_items()

        

    def setup_player(self):
        self.player=player.player('1P')
        self.player.rect.x=110
        self.player.rect.y=490

    def setup_items(self):
        self.ground_items_group=pygame.sprite.Group()
        for name in ['ground','pipe','step']:
            for wupin in self.maps[name]:
                self.ground_items_group.add(item.item(wupin['x'],wupin['y'],wupin['width'],wupin['height'],name))
        self.useful_group=pygame.sprite.Group()
        for wupin in self.maps['coin']:
            self.useful_group.add(useful.coin(wupin['x'],wupin['y'],'coin'))
        for wupin in self.maps['enemy']:
            self.useful_group.add(useful.enemy(wupin['x'],wupin['y'],'enemy'))
        for wupin in self.maps['brick']:
            self.useful_group.add(useful.brick(wupin['x'],wupin['y'],'brick'))
        

    
    def update_player(self):
        self.player.rect.x +=self.player.x_v
       
        if self.player.rect.x<0:
            self.player.rect.x=0
        elif self.player.rect.right> self.end_x:
            self.player.rect.right= self.end_x
        if self.player.rect.left< self.viewport.left:
            self.player.rect.left = self.viewport.left
        # x
        ##碰撞检测
        ##基础物体
        ground_item=pygame.sprite.spritecollideany(self.player,self.ground_items_group)
        if ground_item:
            if self.player.rect.x< ground_item.rect.x:      ##从左边撞击
                self.player.rect.right=ground_item.rect.left
                
            else:
                self.player.rect.left=ground_item.rect.right
        ## 功能物体
        useful_item=pygame.sprite.spritecollideany(self.player,self.useful_group)
        if useful_item:
            if useful_item.name=='coin':
                self.useful_group.remove(useful_item)
                coin_sound=pygame.mixer.Sound('resources/sound/coin.ogg')
                coin_sound.play(0,0,100)
                self.game_info['coin'] +=1
                self.game_info['score'] +=2
            if useful_item.name=='enemy':
                if self.player.rect.x<useful_item.rect.x:      ##从左边撞击
                   self.player.dead=True    
                else:
                   self.player.dead=True 

            if useful_item.name=='brick':
                if self.player.rect.x< useful_item.rect.x:      ##从左边撞击
                   self.player.rect.right=useful_item.rect.left    
                else:
                   self.player.rect.left=useful_item.rect.right
            
        # y
        self.player.rect.y +=self.player.y_v     
        useful_item=pygame.sprite.spritecollideany(self.player,self.useful_group)
        ground_item=pygame.sprite.spritecollideany(self.player,self.ground_items_group)  
        if ground_item:
            if self.player.rect.bottom < ground_item.rect.bottom:
                self.player.rect.bottom=ground_item.rect.top
                self.player.y_v=0
            else:
                self.player.rect.top=ground_item.rect.bottom
                self.player.y_v=0
        if useful_item:           
            if useful_item.name=='coin':
                self.useful_group.remove(useful_item)
                coin_sound=pygame.mixer.Sound('resources/sound/coin.ogg')
                coin_sound.play(0,0,200)
                self.game_info['coin'] +=1
                self.game_info['score'] +=2
            if useful_item.name=='enemy':
                if self.player.rect.bottom < useful_item.rect.bottom:      
                    self.useful_group.remove(useful_item)
                    self.game_info['score'] +=2
                    bump_sound=pygame.mixer.Sound('resources/sound/bump.ogg')
                    bump_sound.play()
            if useful_item.name=='brick':
                if self.player.rect.bottom < useful_item.rect.bottom:
                    self.player.rect.bottom=useful_item.rect.top
                    self.player.y_v=0
                else:
                    self.player.rect.top=useful_item.rect.bottom
                    self.player.y_v=0
        if self.player.rect.top>600:           ## 踩空了
            self.player.dead=True     
        
        if self.player.rect.right>=3263*2.68 and self.player.rect.bottom>=168*2.68 and self.player.rect.right<=3279*2.68:
            self.win=True
    def update_viewport(self):
        limit=self.viewport.x+self.viewport.width/2
        if self.player.x_v>0 and self.player.rect.x>limit and self.viewport.right< self.end_x:
            self.viewport.x +=self.player.x_v
    
    def update(self,surface,keys):
        self.player.update(keys)
        self.info.update_info(self.game_info)
        if self.player.dead:
            self.finished = True                
            self.update_game_info()
        elif self.win:
            self.finished = True                
            self.update_game_info()
        else:
            self.update_viewport()
            self.update_player()
        
        self.draw(surface)
    
    
    def draw(self,surface):
        self.game_ground.blit(self.background,self.viewport,self.viewport)  #(目标图层,指定位置,目标图层的特定部分)
        self.game_ground.blit(self.player.image,self.player.rect)
        self.useful_group.draw(self.game_ground)
        surface.blit(self.game_ground,(0,0),self.viewport)  
        self.info.draw(surface)                # 绘制信息
    
    def update_game_info(self):
        if self.player.dead:
            self.game_info['lives'] -= 1
        if self.game_info['lives'] == 0:
            self.next = 'gameover'
        elif self.win:
            self.next = 'win'
        else:
            self.next = 'load'
 
    def setup_maps(self):
        self.maps={
            'ground':[
        {'x':   0, 'y':538, 'width':2953, 'height':60},
        {'x':3048, 'y':538, 'width': 635, 'height':60},
        {'x':3819, 'y':538, 'width':2735, 'height':60},
        {'x':6647, 'y':538, 'width':3250, 'height':60}
    ],
    'pipe':[
        {'x':1201, 'y':451, 'width': 83, 'height': 84, },
        {'x':1629, 'y':409, 'width': 83, 'height':126, },
        {'x':1972, 'y':366, 'width': 83, 'height':170, },
        {'x':2444, 'y':366, 'width': 83, 'height':170, 'type':1},
        {'x':6987, 'y':451, 'width': 83, 'height': 84, },
        {'x':7673, 'y':451, 'width': 83, 'height': 84, },
        {'x':9724, 'y':451, 'width': 40, 'height': 84, 'type':2}
    ],
    'step':[
        {'x':5745, 'y':495, 'width': 40, 'height': 44},
        {'x':5788, 'y':452, 'width': 40, 'height': 44},
        {'x':5831, 'y':409, 'width': 40, 'height': 44},
        {'x':5874, 'y':366, 'width': 40, 'height':176},
        
        {'x':6001, 'y':366, 'width': 40, 'height':176},
        {'x':6044, 'y':408, 'width': 40, 'height': 44},
        {'x':6087, 'y':452, 'width': 40, 'height': 44},
        {'x':6130, 'y':495, 'width': 40, 'height': 44},
        
        {'x':6345, 'y':495, 'width': 40, 'height': 44},
        {'x':6388, 'y':452, 'width': 40, 'height': 44},
        {'x':6431, 'y':409, 'width': 40, 'height': 44},
        {'x':6474, 'y':366, 'width': 40, 'height': 44},
        {'x':6517, 'y':366, 'width': 40, 'height':176},
        
        {'x':6644, 'y':366, 'width': 40, 'height':176},
        {'x':6687, 'y':408, 'width': 40, 'height': 44},
        {'x':6728, 'y':452, 'width': 40, 'height': 44},
        {'x':6771, 'y':495, 'width': 40, 'height': 44},
        
        {'x':7760, 'y':495, 'width': 40, 'height': 44},
        {'x':7803, 'y':452, 'width': 40, 'height': 44},
        {'x':7845, 'y':409, 'width': 40, 'height': 44},
        {'x':7888, 'y':366, 'width': 40, 'height': 44},
        {'x':7931, 'y':323, 'width': 40, 'height': 44},
        {'x':7974, 'y':280, 'width': 40, 'height': 44},
        {'x':8017, 'y':237, 'width': 40, 'height': 44},
        {'x':8060, 'y':194, 'width': 40, 'height': 44},
        {'x':8103, 'y':194, 'width': 40, 'height':360},
        
        {'x':8488, 'y':495, 'width': 40, 'height': 44},
        {'x':9821, 'y': 64, 'width': 70, 'height':530}
    ],
    'coin':[
        {'x': 858, 'y':365},
        {'x': 944, 'y':365},
        {'x':3430, 'y':193},
        {'x':3473, 'y':193},
        {'x':3473, 'y':193},
        {'x':3516, 'y':193},
        {'x':4030, 'y':365},
        {'x':4287, 'y':365 },
        {'x':4330, 'y':365},
        {'x':5058, 'y':365 },
        {'x':5273, 'y':193},
        {'x':5488, 'y':193 },
        {'x':5574, 'y':193 },
        {'x':5617, 'y':193},
        {'x':5531, 'y':365},
        {'x':5574, 'y':365 },
        {'x':7202, 'y':365},
    ],
    'brick':[
        {'x': 858, 'y':365},
        {'x': 944, 'y':365},
        {'x':1030, 'y':365},
        {'x':3299, 'y':365},
        {'x':3385, 'y':365},
        
        {'x':3430, 'y':193},
        {'x':3473, 'y':193},
        {'x':3516, 'y':193},
        {'x':3559, 'y':193},
        {'x':3602, 'y':193 },
        {'x':3645, 'y':193 },
        {'x':3688, 'y':193 },
        {'x':3731, 'y':193 },
        {'x':3901, 'y':193 },
        {'x':3944, 'y':193},
        {'x':3987, 'y':193 },
        
        {'x':4030, 'y':365},
        {'x':4287, 'y':365 },
        {'x':4330, 'y':365},
        {'x':5058, 'y':365 },
        
        {'x':5187, 'y':193},
        {'x':5230, 'y':193 },
        {'x':5273, 'y':193},
        {'x':5488, 'y':193 },
        {'x':5574, 'y':193 },
        {'x':5617, 'y':193},
        {'x':5531, 'y':365},
        {'x':5574, 'y':365 },
        {'x':7202, 'y':365},
        {'x':7245, 'y':365},
        {'x':7331, 'y':365},

        {'x':9090, 'y': 64},
        {'x':9310, 'y': 64},
        {'x':9310, 'y':406},
        {'x':9310, 'y':449},
        {'x':9310, 'y':492}
    ],
    'final':[
        {'x':3263,'y':168},
        {'x':9286,'y':168}
    ],
        'enemy':[
        
            {'x':1120, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
        
            {'x':1920, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
       
            {'x':2320, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':2380, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
       
            {'x':3640, 'y':193, 'direction':0, 'type':0, 'color':0},
            {'x':3700, 'y':193, 'direction':0, 'type':0, 'color':0}
        ,
       
            {'x':4270, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':4330, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
        
            {'x':4700, 'y':538, 'direction':0, 'type':1, 'color':1}
        ,
        
            {'x':4900, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':4960, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
        
            {'x':5300, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':5360, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
       
            {'x':5600, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':5660, 'y':538, 'direction':0, 'type':0, 'color':0}
        ,
        
            {'x':7550, 'y':538, 'direction':0, 'type':0, 'color':0},
            {'x':7610, 'y':538, 'direction':0, 'type':0, 'color':0}
        
    ]
        }