# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import Sprite


#通过Sprite类，将游戏中相关的元素编组，进而同时操作编组中的所有元素
class Alien(Sprite):
    #表示单个外星人的类
    def __init__(self,ai_settings, screen):
        super(Alien,self).__init__()
        self.screen = screen  #屏幕
        self.ai_settings = ai_settings

        #加载外星人图像。并设置起rect属性
        self.image = pygame.image.load('./alien.bmp')
        self.rect = self.image.get_rect() #外星人图片的rect属性

        #每个外星人初始都在屏幕左上角附近,将每个外星人的左边距啥都设置为外星人的宽度，上边距设置为外星人的高度
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人的准确位置
        self.x = float(self.rect.x)


    #指定位置绘制外星人
    def blitme(self):
        self.screen.blit(self.image, self.rect) 
    '''
    A.blit(source, dest, area=None, special_flags = 0) -> Rect。
    blit方法是将source的Surface渲染到A这个Surface上的方法。
    dest这个参数代之渲染的位置，dest既可以用一个代表source左上角坐标对的元组表示，也可以用一个Rect对象表示，Rect的topleft属性自动被用作dest
    '''

    def update(self):
        #向右还是向左移动外星人
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect() #屏幕的rect属性
        if self.rect.right >= screen_rect.right: #右边碰壁
            return True

        elif self.rect.left <=0: #左边碰壁
            return True
