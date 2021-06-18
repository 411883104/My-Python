import sys, pygame
from pygame.locals import *
import time
import random
import copy

#初始化
pygame.init()

#设置常量
WIDTH=800
HIGH=600

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#获取窗口window
window=pygame.display.set_mode((WIDTH,HIGH),0,32)
pygame.display.set_caption("Game")

#初始长度为50像素
long=50

#绘制玩家
players=[]
for i in range(0,10):
    body=pygame.Rect(10*i,0,10,10)
    players.append(body)
#食物
food=pygame.Rect(random.randint(0,WIDTH-10),random.randint(0,HIGH-10),10,10)

moveRight=False
moveLeft=False
moveUp=False
moveDown=False

tail=pygame.Rect(0,0,0,0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                moveRight=True
                moveLeft=False
                moveUp=False
                moveDown=False
            elif event.key==K_a:
                moveRight = False
                moveLeft = True
                moveUp = False
                moveDown = False
            if event.key==K_w:
                moveRight = False
                moveLeft = False
                moveUp = True
                moveDown = False
            elif event.key==K_s:
                moveRight = False
                moveLeft = False
                moveUp = False
                moveDown = True


    if moveRight:
        head=players[-1].copy()
        head.right+=10
        players.append(head.copy())
        tail=players.pop(0)
    if moveLeft:
        head = players[-1].copy()
        head.left -= 10
        players.append(head.copy())
        tail=players.pop(0)
    if moveUp:
        head = players[-1].copy()
        head.top-=10
        players.append(head.copy())
        tail=players.pop(0)

    if moveDown:
        head = players[-1].copy()
        head.bottom+=10
        players.append(head.copy())
        tail=players.pop(0)

    #设置窗口颜色
    window.fill((230,230,230))
    for player in players[:]:
        pygame.draw.rect(window, GREEN, player)
        if player.colliderect(food):
            players.insert(0,tail.copy())
            food = pygame.Rect(random.randint(0, WIDTH - 10), random.randint(0, HIGH - 10), 10, 10)
    pygame.draw.rect(window,RED,food)
    pygame.display.update()
    pygame.time.Clock().tick(20)
