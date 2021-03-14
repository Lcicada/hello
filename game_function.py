# -*- coding: UTF-8 -*-
from alien import Alien
from bullet import Bullet
import sys ,time
import pygame

#响应鼠标和键盘按键
def check_events(ai_settings,screen, ship, aliens, bullets, game_status, play_button):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            check_keydown_events(event,ai_settings,screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_up_events(event,ship)

        elif event.type == pygame.MOUSEBUTTONDOWN: #无论玩家点击屏幕什么地方，都会触发一个MOUSEBUTTONDOWN事件
            mouse_x,mouse_y = pygame.mouse.get_pos() #返回一个元组，其中包含鼠标点击的x ,y坐标
            check_play_button(ai_settings,screen, ship,aliens,bullets, game_status, play_button, mouse_x, mouse_y)

        elif event.type == pygame.QUIT:  #点击退出 ，退出游戏
            #if event.key == pygame.K_KP_ENTER: #点击enter键
                sys.exit()
#处理键盘keydown
def check_keydown_events(event,ai_settings,screen, ship, bullets):
    if event.key == pygame.K_RIGHT: 
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  
    elif event.key == pygame.K_SPACE: # 空格键控制子弹
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen,ship) #创建一颗子弹,即发射一枚子弹
            bullets.add(new_bullet) #将这颗子弹放到编组bullets

#处理键盘updown
def check_up_events(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_all_events(ship):
    for event in pygame.event.get():  
        #处理鼠标事件
        if event.type == pygame.QUIT:  #点击退出 ，退出游戏
            #if event.key == pygame.K_KP_ENTER: #点击enter键
            sys.exit()
        #处理键盘事件， 先检测Keydown事件，飞船移动
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                ship.ship_rect.centerx +=1 #飞船向右边移动
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.ship_rect.centerx -=1 #飞船向右边移动
                ship.moving_left = True            
        #处理键盘，keyup事件，长按按键，飞船一直移动
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
       
        # elif event.key ==pygame.kq:
        #     sys.exit()

def update_bullets(ai_settings, screen,ship, bullets,aliens,game_status,scoreboard):

    #更新子弹位置
    bullets.update() #对编组bullets里的每颗子弹调用bullet.update() ，更新子弹位置
    #删除已经消失的子弹
    for bullet in bullets.copy(): #不应从列表或者编组里删除条目，应该遍历编组的副本
        if bullet.bullet_rect.bottom <=0:
            bullets.remove(bullet)
    #若子弹打中外星人（相撞），删除相应的外星人，和子弹
    collisions = pygame.sprite.groupcollide(bullets,aliens, True,True)
    #每次消灭一个外星人，＋50分
    if collisions:
        for aliens in collisions.values():
            game_status.score += ai_settings.shoot_alien_point *len(aliens)
            scoreboard.prep_score()
            
        if game_status.score > game_status.high_score:
                game_status.high_score = game_status.score 
        else:
                game_status.high_score = game_status.high_score 
        scoreboard.prep_high_score()

    #生成新的一批外星人
    if len(aliens) ==0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def update_screen(ai_settings, screen, ship, aliens, bullets, play_button, scoreboard):
    #飞船
    ship.blitme()

    #外星人
    # alien.blitme()
    aliens.draw(screen)

    #在飞船和外星人后面重绘所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullets()

    #play按钮
    play_button.draw_button()

    #显示得分情况
    scoreboard.show_score()

    #让最近绘制的屏幕可见
    pygame.display.flip()


def update_aliens(ai_settings,game_status, screen,ship, aliens,bullets):
    #检查是否外星人位于屏幕边缘，并更新外星人群中所有外星人的位置
    check_fleet_edges(ai_settings, aliens)
    aliens.update() #对编组aliens调用update方法，这将自动对每个外星人调用update()

    #检查外星人与飞船是否相撞
    if pygame.sprite.spritecollideany(ship,aliens):
        print('Ship hit')
        ship_hit(ai_settings,game_status, screen,ship, aliens,bullets)
    
    check_alien_ship_gap(ai_settings,game_status,screen,ship,aliens,bullets)
    

def ship_hit(ai_settings,game_status, screen,ship, aliens,bullets):
    if game_status.ships_number_left >0:
        print game_status.ships_number_left
        game_status.ships_number_left -= 1
        print game_status.ships_number_left
        aliens.empty()
        bullets.empty()
        #创建一批新外星人群 和飞船
        create_fleet(ai_settings, screen, ship, aliens)
        ship.ship_init()
        time.sleep(5)

    else:
        game_status.game_active = False
        pygame.mouse.set_visible(True)

#当外星人下沿 = 飞船上沿 ，重新开始
def check_alien_ship_gap(ai_settings,game_status,screen,ship,aliens,bullets):
    #print  ship.ship_rect.y
    for alien in aliens.sprites():
        # print alien.rect.y
        # print alien.rect.bottom    
        if  alien.rect.bottom  == ship.ship_rect.y:
            print ('Game over')
            print (' Start again                ')
            ship_hit(ai_settings,game_status, screen,ship, aliens,bullets)
    #     print 111111111
    # print 22222


#x向下移动外星人群并改变移动方向
def check_fleet_edges(ai_settings, aliens):
    #外星人到达边缘时采取相应的措施
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    #将整群外星人下移，并改变他们的方向
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.fleet_drop_speed #将每个外星人下移fleet_drap_speed设置的值
    ai_settings.fleet_direction *= -1


#对上面的方法，解耦
def get_number_alien_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_alien_x = int(available_space_x/(2*alien_width))
    return number_alien_x

def get_number_rows(ai_settings,ship_height, alien_height):
    #可用的垂直高度 ： 屏幕高度 - 第一行外星人的上边距 -外星人高度-外星人间距（即外星人高度） -飞船高度 ;
    # 飞船上方要留出一定空白区域（外星人高度+外星人间距（即2倍的外星人高度）），给玩家留出射杀外星人的时间
    available_space_y =  ai_settings.screen_height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings,screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_alien_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.ship_rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_play_button(ai_settings,screen, ship,aliens,bullets, game_status, play_button, mouse_x, mouse_y):
    #每次点击play, 重置游戏次数（恢复到初始值）， 清空外星人、子弹列表，再创建新的外星人群，飞船居中
    button_cliked =  play_button.rect.collidepoint(mouse_x,mouse_y)#collidepoint()判断鼠标点击的位置是否在play按钮的rect内
    if button_cliked and not game_status.game_active: #当点击play按钮，且当前处于非活动状态时，即游戏重新开始
        ai_settings.initialize_dynamic_setting() #重置游戏速度方面的设置
        pygame.mouse.set_visible(False) #当游戏未开始，且点击了play 按钮后，就隐藏光标
        game_status.game_active = True

        game_status.status_init()
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings,screen, ship,aliens)
        ship.ship_init()