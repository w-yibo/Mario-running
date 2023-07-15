import pygame
from source import tools,init,const

class player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name=name
        self.setup_states()
        self.setup_v()
        self.load_image()
        self.setup_timer()

        self.frame_index=0
        self.image=self.frames[self.frame_index]
        self.rect=self.image.get_rect()

    def setup_states(self):
        self.dead=False

    
    def setup_v(self):
        self.x_v=0
        self.y_v=0
    
    def load_image(self):
        picture=init.pictures['mario_bros']
        self.right_frames=[]
        self.left_frames=[]

        frame_rects=[
            (178,32,12,16),
            (80,32,15,16),
            (96,32,16,16),
            (112,32,16,16)
        ]    #####存储每一帧的rect
        for frame_rect in frame_rects:            # *frame_rect 解封装
            right_image=tools.get_image(picture,*frame_rect,const.mario_multi,(0,0,0))
            left_image=pygame.transform.flip( right_image,True,False)  #左右翻转
            self.right_frames.append(right_image)
            self.left_frames.append(left_image)
        
        ## 初始化
        
        self.frames=self.right_frames
    
    def setup_timer(self):     
        self.walking_timer=0

    def update(self,keys):
        self.current_time=pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_v=5
            self.frames=self.right_frames            
        elif keys[pygame.K_LEFT]:
            self.x_v=-5
            self.frames=self.left_frames              
        else:
            self.x_v=0           #停下来
            self.frame_index=0   
        if keys[pygame.K_SPACE]:
            if self.y_v==0:
               self.y_v=-15   
        if self.x_v:             
            if self.current_time - self.walking_timer> 100:         ## 实现动态动作
               self.walking_timer=self.current_time  ####
               self.frame_index +=1
               self.frame_index %=4
        self.y_v+=const.G
        self.image=self.frames[self.frame_index]
