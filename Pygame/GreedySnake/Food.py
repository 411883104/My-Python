import pygame,random

class Food:
    '''食物更新类'''
    def __init__(self,game):
        self.setting=game.setting
        self.screen=game.screen
        self.Width=random.randint(0,self.setting.WIDTH-self.setting.SIZE)
        self.High=random.randint(0,self.setting.HIGH-self.setting.SIZE)
        self.rect=pygame.Rect(self.Width,self.High,self.setting.SIZE,self.setting.SIZE)

    #更新食物的位置
    def update(self):
        self.Width = random.randint(0, self.setting.WIDTH - self.setting.SIZE)
        self.High = random.randint(0, self.setting.HIGH - self.setting.SIZE)
        self.rect = pygame.Rect(self.Width, self.High, self.setting.SIZE, self.setting.SIZE)

    def draw(self):
        pygame.draw.rect(self.screen,self.setting.RED,self.rect)