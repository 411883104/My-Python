import pygame
class Map:
    '''绘制地图类'''
    def __init__(self,game):
        self.screen=game.screen
        self.setting=game.setting

        #设置边框
        self.top=pygame.Rect(0,0,self.setting.WIDTH,10)
        self.bottom=pygame.Rect(0,self.setting.HIGH-10,self.setting.WIDTH,10)
        self.left=pygame.Rect(0,0,10,self.setting.HIGH)
        self.right=pygame.Rect(self.setting.WIDTH-10,0,10,self.setting.HIGH)

    def draw(self):
        pygame.draw.rect(self.screen,self.setting.BLUE,self.top)
        pygame.draw.rect(self.screen, self.setting.BLUE, self.bottom)
        pygame.draw.rect(self.screen, self.setting.BLUE, self.left)
        pygame.draw.rect(self.screen, self.setting.BLUE, self.right)