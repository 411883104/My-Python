import pygame,sys
from pygame.locals import *

class Message:
    '''管理键盘响应的类'''
    def __init__(self,game):
        self.snake=game.snake

    #获取消息
    def Get_Key(self):
        '''键盘响应'''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_d:
                    self.snake.moveRight = True
                    self.snake.moveLeft = False
                    self.snake.moveUp = False
                    self.snake.moveDown = False
                elif event.key == K_a:
                    self.snake.oveRight = False
                    self.snake.moveLeft = True
                    self.snake.moveUp = False
                    self.snake.moveDown = False
                if event.key == K_w:
                    self.snake.moveRight = False
                    self.snake.moveLeft = False
                    self.snake.moveUp = True
                    self.snake.moveDown = False
                elif event.key == K_s:
                    self.snake.moveRight = False
                    self.snake.moveLeft = False
                    self.snake.moveUp = False
                    self.snake.moveDown = True

            '''鼠标响应'''
            if event.type==MOUSEBUTTONDOWN:
                if self.snake.moveUp:
                    if event.pos[1]-self.snake.player[-1].top<0:
                        if event.pos[0]>self.snake.player[-1].centerx:
                            self.snake.moveRight=True
