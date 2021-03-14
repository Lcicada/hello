# -*- coding: UTF-8 -*-
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_function as gf
import pygame
from pygame.sprite import Group
from settings import Settings
from game_status import GameStatus
from button import Button
import sys
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    #初始化屏幕尺寸,背景颜色
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    screen.fill(ai_settings.screen_bg_color)

    # alien =Alien(ai_settings,screen)
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    game_status = GameStatus(ai_settings)
    play_button = Button(ai_settings,screen ,'Play')
    scoreboard = Scoreboard(ai_settings,screen,game_status)

    gf.create_fleet(ai_settings, screen,ship,  aliens) #创建多行多列 的aliens


    while True: 
        screen.fill(ai_settings.screen_bg_color) #每次循环，重新绘制屏幕，不然会有之前绘制留下的残影
        gf.check_events(ai_settings,screen, ship, aliens, bullets, game_status, play_button)
        if game_status.game_active: #判断3次机会有没有用完
            ship.update()
            gf.update_bullets(ai_settings, screen,ship, bullets,aliens,game_status,scoreboard)
            gf.update_aliens(ai_settings,game_status, screen,ship, aliens,bullets)

        gf.update_screen(ai_settings, screen, ship, aliens,bullets,play_button,scoreboard) # 更新屏幕上面的图形状况

            #upate_screen()代替如下代码
            # alien.blitme()
            # ship.blitme()
            # pygame.display.flip()
   


if  __name__ == "__main__":
    run_game()














'''
def run_game():
    #创建一个外星人
    alien = Alien(ai_settings, screen)
    #开始游戏
    while True:
        gf.check_events(ai_settings,screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

def run_game():
    #初始化屏幕尺寸,背景颜色
    ai_settings = Settings()
    screen =pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    screen.fill(ai_settings.screen_bg_color)


    #创建一艘飞船，一个子弹，和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #开始游戏
    while True:
        gf.check_event(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets)
            gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

    pygame.display.flip()

'''