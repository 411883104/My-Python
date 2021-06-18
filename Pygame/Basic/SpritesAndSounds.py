import pygame,sys,random
from pygame.locals import *

#初始化
pygame.init()
#pygame.time.Clock对象可以对于任何计算机都暂停适当的时间
mainClock=pygame.time.Clock()
#设置常量
WINDOWHEIGHT=400
WINDOWWIDTH=800
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)

#创建变量
foodCounter=0
NEWFOOD=40
FOODSIZE=15
MOVESPEED=4
#创建窗口
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption("Sprites and Sounds")

#添加精灵
player=pygame.Rect(300,100,40,40)
#读取图片，函数接收字符串(文件路径)，返回Surface对象
playerImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\test.jpg")
#使用pygame.transform模块中的pygame.transform.scale()函数缩放精灵，函数返回Surface对象
#第一个参数是在其上绘制的Surface对象，第二个参数是一个新图像宽度和高度的元组
playerStretchedImage=pygame.transform.scale(playerImage,(40,40))
foodImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\timg.jpg")
foodStretchedImage=pygame.transform.scale(foodImage,(FOODSIZE,FOODSIZE))

#添加声音
#pygame中两个声音模块lpygame.mixer(播放简短音效)和pygame.mixer.music(播放背景音乐)
#调用pygame.mixer.Sound()函数构造一个pygame.mixer.Sound()对象
pickUpSound=pygame.mixer.Sound("D:\\Dataset\\三国无双4-开头-音效.mp3")
#使用pygame.mixer.music.load()函数加载背景音乐
pygame.mixer.music.load("D:\\Dataset\\超级玛丽游戏音效.mp3")
#使用play()方法播放音效
#第一个参数表示在第一次播放后还要播放几次(传5即播放6次)，-1为特殊值，无限循环播放
#第二个参数是开始播放声音文件的位置(第几秒开始)
pygame.mixer.music.play(-1,0.0)
musicPlaying=True#用于后面控制音效的播放和暂停



foods=[]
for i in range(20):
    foods.append(pygame.Rect(random.randint(0,WINDOWWIDTH-FOODSIZE),random.randint(0,WINDOWHEIGHT-FOODSIZE),FOODSIZE,FOODSIZE))

#设置变量以记录移动
#用户按下方向键时变量设成True,松开后设回False
moveLeft=False
moveRight=False
moveUp=False
moveDown=False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # K_LEFT和K_a表示左方向键和按键A，包含在pygame.locals中
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = True
                moveRight = False
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == K_w:
                moveUp = True
                moveDown = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = True
                moveUp = False

            # 改变玩家位置
            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT)
                player.left = random.randint(0, WINDOWWIDTH)
            if event.key==K_m:
                if musicPlaying:
                    #使用pygame.mixer.music.stop()暂停音乐
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                #将开关设置设反
                musicPlaying=not musicPlaying

        # 处理KEYUP事件
        if event.type == KEYUP:
            # 如果释放esc键则退出游戏
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False

        # 通过鼠标添加事物
        # event.pos[0]表示鼠标X坐标，event.pos[1]表示鼠标Y坐标
        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    windowSurface.fill(WHITE)
    pygame.draw.rect(windowSurface, WHITE, player)
    windowSurface.blit(playerStretchedImage,player)

    # 在屏幕上移动玩家
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # 检查碰撞
    for food in foods[:]:  # 使用列表副本
        # 使用Rect对象碰撞检测方法colliderect()
        if player.colliderect(food):
            foods.remove(food)
        if musicPlaying:
            pickUpSound.play()
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])
        windowSurface.blit(foodStretchedImage,foods[i])


    # 更新食物
    foodCounter += 1
    if foodCounter > NEWFOOD:
        foodCounter = 0
        foods.append(
            pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE,
                        FOODSIZE))

    pygame.display.update()
    # tick()函数无论计算机速度有多快，他都可以每秒迭代40次
    mainClock.tick(40)