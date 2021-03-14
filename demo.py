import  pygame, sys
#  https://blog.csdn.net/zha6476003/article/details/82940350

def test():
    size = width, height = 640, 480
    color =(230,230,230)
    screen = pygame.display.set_mode(size)
    alien = pygame.image.load('./alien.bmp')

    alien_rect = alien.get_rect()
    screen_rect = screen.get_rect()
    
    alien_rect.centerx =(screen_rect.centerx)/2
    #alien_rect.centery = screen_rect.height - (alien_rect.height)/2
    alien_rect.bottom = screen_rect.bottom
    print  alien_rect.bottom , alien_rect.centery
    # screen_rect = screen.get_rect()
    # screen_rect.x = screen_rect.width
    # print screen_rect.x 
    

    while True:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                sys.exit()
        screen.fill(color)
        screen.blit(alien,alien_rect)
        pygame.display.flip()
    pygame.quit()


test()