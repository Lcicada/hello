# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        super(Bullet,self).__init__()
        self.screen = screen

        #在坐标（0,0）处设置一个子弹的矩形
        self.bullet_rect = pygame.Rect(0,0,ai_settings.bullet_width, ai_settings.bullet_height) #创建一个子弹对象
        self.bullet_rect.centerx = ship.ship_rect.centerx
        self.bullet_rect.top = ship.ship_rect.top
        self.rect = self.bullet_rect 

        self.y =float(self.bullet_rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def draw_bullets(self):
        pygame.draw.rect(self.screen, self.color , self.bullet_rect) #pygame.draw.rect： 绘制矩形
        
        '''
        pygame.draw.rect(Surface, color, Rect, width=0)
        用途：在Surface上绘制矩形，第二个参数是线条（或填充）的颜色，
        第三个参数Rect的形式是((x, y), (width, height))，表示的是所绘制矩形的区域，
        其中第一个元组(x, y)表示的是该矩形左上角的坐标，
        第二个元组 (width, height)表示的是矩形的宽度和高度。width表示线条的粗细，单位为像素；默认值为0，表示填充矩形内部。
        '''

    def update(self):
        #更新子弹的位置的小数值 
        self.y -= self.speed_factor  #子弹会动，取决于这个，不断减，y坐标不断更新
        #更新子弹的rect位置
        self.bullet_rect.y = self.y

    