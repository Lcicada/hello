# -*- coding: UTF-8 -*-

class GameStatus():

    def __init__(self,ai_settings):
        self.game_active =False
        self.ai_settings = ai_settings
        self.high_score = 0
        self.status_init()


    def status_init(self):
        self.ships_number_left = self.ai_settings.ship_number_limit
        self.score = 0
        
        
   
