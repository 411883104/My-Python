import pygame,time,random,sys
from pygame.locals import*

pygame.init()
#pygame.time.Clock对象可以对于任何计算机都暂停适当的时间
mainClock=pygame.time.Clock()

WINDOWWIDTH=800
WINDOWHEIGHT=400
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption("Collision Detection")

BLACK=(0,0,0)
GREEN=(0,255,0)
WHITH=(255,255,255)


#创建变量
foodCounter=0
NEWFOOD=40
FOODSIZE=15
MOVESPEED=4

player=pygame.Rect(300,100,35,35)
foods=[]
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

#设置变量以记录移动
#用户按下方向键时变量设成True,松开后设回False
moveLeft=False
moveRight=False
moveUp=False
moveDown=False

#处理事件
#QUIT  当用户关闭窗口时触发的事件
#KEYDOWN   当用户按下键盘时触发的事件(其中有一个key属性来识别按下的哪个键，一个mod属性表明是否有其他键和该键同时按下)
#KEYUO     当用户释放一个按键时触发的事件，同时也有key和mod两个属性
#MOUSEMOTION   任何时候鼠标移动经过窗口时都会触发该事件
#    （有一个pos属性返回鼠标在窗口坐标的元组，rel属性也返回一个相对上一次事件的坐标元组）
#    鼠标从(200,200)向左移动变成(196,200)，则rel返回(-4,0)
#    buttons属性返回包含3个整数的元组，分别表示鼠标左键，中间键，右键。按下为1，没按为0
#MOUSEBUTTONDOWN  当在窗口按下鼠标时触发该事件
#    也有pos属性和有5个整数的buttons属性(1左键，2中间键，3右键，4向上滚轮，5向下滚轮)
#MOUSEBUTTONUP  当释放鼠标时触发的事件，具有和MOUSEBUTTONDOWN相同的属性

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            #K_LEFT和K_a表示左方向键和按键A，包含在pygame.locals中
            if event.key==K_LEFT or event.key==K_a :
                moveLeft=True
                moveRight=False
            if event.key==K_RIGHT or event.key==K_d :
                moveLeft=False
                moveRight=True
            if event.key==K_UP or event.key==K_w :
                moveUp=True
                moveDown=False
            if event.key==K_DOWN or event.key==K_s :
                moveDown=True
                moveUp=False

            #改变玩家位置
            if event.key==K_x:
                player.top=random.randint(0,WINDOWHEIGHT)
                player.left=random.randint(0,WINDOWWIDTH)

        #处理KEYUP事件
        if event.type==KEYUP:
            #如果释放esc键则退出游戏
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==K_LEFT or event.key==K_a :
                moveLeft=False
            if event.key==K_RIGHT or event.key==K_d :
                moveRight=False
            if event.key==K_UP or event.key==K_w :
                moveUp=False
            if event.key==K_DOWN or event.key==K_s :
                moveDown=False

        #通过鼠标添加事物
        #event.pos[0]表示鼠标X坐标，event.pos[1]表示鼠标Y坐标
        if event.type==MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0],event.pos[1],FOODSIZE,FOODSIZE))

    windowSurface.fill(WHITH)
    pygame.draw.rect(windowSurface,BLACK,player)

    #在屏幕上移动玩家
    if moveDown and player.bottom<WINDOWHEIGHT:
            player.top+=MOVESPEED
    if moveUp and player.top>0:
            player.top-=MOVESPEED
    if moveLeft and player.left>0:
            player.left-=MOVESPEED
    if moveRight and player.right<WINDOWWIDTH:
            player.right+=MOVESPEED

    #检查碰撞
    for food in foods[:]:#使用列表副本
        #使用Rect对象碰撞检测方法colliderect()
        if player.colliderect(food):
            foods.remove(food)
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface,GREEN,foods[i])

    #更新食物
    foodCounter+=1
    if foodCounter>NEWFOOD:
        foodCounter=0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE,FOODSIZE))

    pygame.display.update()
    #tick()函数无论计算机速度有多快，他都可以每秒迭代40次
    mainClock.tick(40)