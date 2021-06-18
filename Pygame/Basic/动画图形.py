import pygame,time,sys
from pygame.locals import*

#设置常量变量
pygame.init()
WINDOWWIDTH=400
WINDOWHEIGHT=400
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWWIDTH),0,32)
pygame.display.set_caption('Animation')

#设置方向常量变量
DOWNLEFT='downleft'
DOWNRIGHT='downright'
UPLEFT='upleft'
UPRIGHT='upright'
#设置移动速度（）移动多少个像素
MOVESPEED=4
#设置颜色变量
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#设置积木数据结构
b1={'rect':pygame.Rect(300,80,50,100),'color':RED,'dir':UPRIGHT}
b2={'rect':pygame.Rect(200,200,20,120),'color':GREEN,'dir':UPLEFT}
b3={'rect':pygame.Rect(100,150,60,60),'color':BLUE,'dir':DOWNLEFT}
boxes=[b1,b2,b3]
#可以使用boxes[i]访问列表中字典，boxes[i]['color']访问颜色的值
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)

    #移动积木
    for b in boxes:
        if b['dir']==DOWNLEFT:
            b['rect'].left-=MOVESPEED
            b['rect'].top+=MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir']==UPLEFT:
            b['rect'].left-=MOVESPEED
            b['rect'].top-=MOVESPEED
        if b['dir']==UPRIGHT:
            b['rect'].left+=MOVESPEED
            b['rect'].top-=MOVESPEED
        if b['rect'].top<0:
            if b['dir']==UPLEFT:
                b['dir']==DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']==DOWNRIGHT
        if b['rect'].bottom>WINDOWHEIGHT:
            if b['dir']==DOWNLEFT:
                b['dir']==UPLEFT
            if b['dir']==DOWNRIGHT:
                b['dir']==UPRIGHT
        if b['rect'].left<0:
            if b['dir']==DOWNLEFT:
                b['dir']==DOWNRIGHT
            if b['dir']==UPLEFT:
                b['dir']==UPRIGHT
        if b['rect'].right>WINDOWWIDTH:
            if b['dir']==DOWNRIGHT:
                b['dir']==DOWNLEFT
            if b['dir']==UPRIGHT:
                b['dir']==UPLEFT
        pygame.draw.rect(windowSurface,b['color'],b['rect'])
    pygame.display.update()
    time.sleep(0.02)#积木每一次移动都将程序暂停0.02秒(所有计算机上都延迟0.02秒)