import pygame,sys,random,time
from pygame.locals import *

from Setting import Setting
from Snake import Snake
from Food import Food
from Message import Message
from Map import Map

class Game:
    def __init__(self):
        pygame.init()
        self.setting=Setting()
        self.screen = pygame.display.set_mode((self.setting.WIDTH,self.setting.HIGH),0,32)
        self.food=Food(self)
        self.snake=Snake(self)
        self.message=Message(self)
        self.map=Map(self)

    def update_draw(self):
        self.screen.fill(self.setting.BACKGROUND)
        #self.map.draw()
        self.snake.update()
        self.snake.draw()
        self.food.draw()
        pygame.display.update()

    def run(self):
        while True:
            self.message.Get_Key()
            self.update_draw()
            pygame.time.Clock().tick(self.setting.FPS)

if __name__=="__main__":
    game=Game()
    game.run()