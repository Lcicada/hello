# -*- coding: UTF-8 -*-
import pygame.font

class Scoreboard():
    def __init__(self,ai_settings,screen,game_status):
        self.screen = screen
        self.ai_settings = ai_settings
        self.game_status = game_status
        self.screen_rect = self.screen.get_rect()
        #显示得分信息时使用的字体设置
        self.text_color = (30, 30, 30) #文本颜色
        self.font = pygame.font.SysFont(None, 48) # 实例话一个字体对象，字体大小
        self.prep_score() #将显示的文本转换为图像
        self.prep_high_score()

    
    def prep_score(self):
        #首先将得分的数字转换为字符串
        score_str = str(self.game_status.score)

        #将得分转换为渲染的图像
        round_score = int(round(self.game_status.score,-1))
        #round 函数让小数精确到小数点后几位，小数点位数由第二个实参决定，若为负数，则圆整到最近的10,100等整数倍
        score_str = '{:,}'.format(round_score)
        #再将这个字符串传递给创建图像的render(), 为了在屏幕上清晰地显示得分，需要render()传递背景颜色，文本颜色
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.screen_bg_color)

        #将得分显示在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top = 20  

    def prep_high_score(self):
        #首先将最高得分的数字转换为字符串
        score_str = str(self.game_status.high_score)

        # #将得分转换为渲染的图像
        # round_score = int(round(self.game_status.score,-1))
        # #round 函数让小数精确到小数点后几位，小数点位数由第二个实参决定，若为负数，则圆整到最近的10,100等整数倍
        # score_str = '{:,}'.format(round_score)
        # #再将这个字符串传递给创建图像的render(), 为了在屏幕上清晰地显示得分，需要render()传递背景颜色，文本颜色
        self.high_score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.screen_bg_color)

        #将得分显示在屏幕上方中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image ,self.score_rect)
        self.screen.blit(self.high_score_image ,self.high_score_rect)