# -*- coding: UTF-8 -*-
class Settings():

    def __init__(self):

        #设置屏幕
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_bg_color = (230,230,230)


        #外星人设置
        self.alien_speed_factor = 5 #移动量 ,外星人水平移动的速度
        self.fleet_drop_speed = 10 #外星人撞到屏幕边缘，外星人向下移动的速度
        self.fleet_direction =1 # 1:向右边移动， -1 :向左边移动

        #飞船设置
        self.ship_speed_factor = 0.5 #飞船水平移动的速度
        self.ship_number_limit = 3 #限制3只飞船，3次机会

        #子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3 #屏幕上最多可以出现3颗子弹

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #消灭外星人得分，增加速度
        self.score_scale = 1.5

        #计分
        self.shoot_alien_point = 50
        

        self.initialize_dynamic_setting()
    
    def initialize_dynamic_setting(self):
        #初始化随游戏进行而变化的设置
        self.alien_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3

        #fleet_direction 为1 表示右，为-1 表示向左
        self.fleet_direction = 1


    def increase_speed(self):
        self.alien_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.shoot_alien_point = int(self.shoot_alien_point*self.score_scale)

