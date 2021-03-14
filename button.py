# -*- coding: UTF-8 -*-
import pygame.font

class Button():

    def __init__(self, ai_settings, screen,msg):
        self.screen = screen
        #设置按钮的一些参数
        self.button_size = (200,50)
        self.width = 200
        self.height = 50
        self.button_color = (0,225,0) #亮绿色
        self.text_color = (225,225,225) #文本颜色，白色
        self.font =pygame.font.SysFont(None ,48) #None:默认字体， 48字号

        #创建一个按钮对象,屏幕上居中显示
        self.rect =pygame.Rect(0,0,self.width, self.height)
        self.rect.center = screen.get_rect().center

        #按钮的标签只需创建依次
        self.prep_msg(msg)
    
    #将msg（按钮上的字符串）渲染为图像来处理文本，使其在按钮上居中
    def prep_msg(self, msg):
        self.msg_image  = self.font.render(msg, True, self.text_color,self.button_color) #font.render()将存储在msg的文本转为图像 
        #font.render()还接收布尔实参，该实参指定开启还是关闭反锯齿功能（反锯齿让文本的边缘更加平滑）
        #余下的两个参数，文本颜色，和背景颜色 ,此时文本的背景颜色和按钮颜色一致
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center 

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect) #按钮填充颜色
        self.screen.blit(self.msg_image,self.msg_image_rect)



