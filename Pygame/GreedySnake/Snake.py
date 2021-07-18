import pygame
import Setting

class Snake:
    '''蛇的参数和构造'''

    def __init__(self,game):
        #创建玩家
        self.player=[]
        for i in range(1,int(game.setting.LONG/10)):
            self.player.append(pygame.Rect(i*10,10,10,10))
        self.food=game.food
        self.screen=game.screen
        self.setting=game.setting
        #移动状态
        self.moveRight=False
        self.moveLeft=False
        self.moveUp=False
        self.moveDown=False


        self.new=pygame.Rect(0,0,0,0)

    #更新蛇的位置
    def update(self):

        if self.moveRight:
            self.new=self.player[-1].copy()
            self.new.right+=self.setting.SPEED
            self.player.append(self.new.copy())
            self.new=self.player.pop(0)
        if self.moveLeft:
            self.new=self.player[-1].copy()
            self.new.left-=self.setting.SPEED
            self.player.append(self.new.copy())
            self.new=self.player.pop(0)
        if self.moveUp:
            self.new=self.player[-1].copy()
            self.new.top-=self.setting.SPEED
            self.player.append(self.new.copy())
            self.new=self.player.pop(0)
        if self.moveDown:
            self.new=self.player[-1].copy()
            self.new.bottom+=self.setting.SPEED
            self.player.append(self.new.copy())
            self.new=self.player.pop(0)



    def draw(self):
        #碰撞检测
        if self.player[-1].colliderect(self.food):
            #self.setting.SPEED+=0.1
            self.player.insert(0,self.new.copy())
            self.food.update()
        for play in self.player:
            pygame.draw.rect(self.screen,self.setting.GREEN,play)