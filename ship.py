# -*- coding: UTF-8 -*-
import pygame
from pygame.sprite import Sprite

class Ship():

    def __init__(self,ai_settings, screen):
        self.screen = screen  #屏幕
        self.ai_settings = ai_settings
        #初始化飞船在屏幕底部中央
        self.ship = pygame.image.load('./ship.bmp')
        self.ship_rect = self.ship.get_rect()
        self.rect = self.ship_rect
        self.screen_rect = self.screen.get_rect()
        self.ship_rect.centerx = self.screen_rect.centerx
        #self.ship_rect.centery = self.screen_rect.height -(self.ship_rect.height)/2
        self.ship_rect.bottom = self.screen_rect.bottom
        #飞船初始位置中心
        self.center = float(self.ship_rect.centerx) #rect属性 只能存储整数， 故飞船的属性center中存储小数值

        self.moving_right = False #右边是否处于一直移动状态
        self.moving_left = False #左边是否处于一直移动状态


    def blitme(self):
        #在指定位置绘制飞船，初始位置
        self.screen.blit(self.ship, self.ship_rect)

    def ship_init(self):
        self.center = self.screen_rect.centerx

    def update(self):
        #moving_right属性，控制飞船是否移动，True移动，False停止移动 ,移动速度为ship_speed_factor=1.5
        #限制飞船移动的范围
        if self.moving_right and self.ship_rect.right<self.screen_rect.right:
            self.center  += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.ship_rect.left>0:
            self.center  -= self.ai_settings.ship_speed_factor
        
        self.ship_rect.centerx = self.center #更新ship位置
        
