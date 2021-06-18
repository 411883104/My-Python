import pygame,sys,random
from pygame.locals import *

#创建常量
WINDOWWIDTH=600
WINDOWHIGHT=600
TEXTCOLOR=(0,0,0)
BACKGROUNDCOLOR=(255,255,255)
#帧数，帧是在游戏循环的单次迭代中所绘制的一个屏幕
#让游戏按照每秒对少帧的速度运行
FPS=60
BADDIEMINSIZE=10
BADDIEMAXSIZE=40
BADDIEMINSPEED=1
BADDIEMAXSPEED=8
ADDNEWBADDIERATE=6
PLAYERMOVERATE=5

#定义退出的函数
def terminate():
    pygame.quit()
    sys.exit()
#定义暂停和等待函数
def waitForPlayTopPressKey():
    while True:
        for event in pygame.event.get():
            #关闭窗口时调用退出函数
            if event.type==QUIT:
                terminate()
            #检测是否按下按键
            if event.type==KEYDOWN:
                #如果按下的是esc则退出
                if event.key==K_ESCAPE:
                    terminate()
                #如果输入的不是esc则退出该循环
                return
#定义记录的敌人碰撞的函数
def playHasHitBaddie(playerRect,baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
        return False
#定义将文本绘制到窗口的函数
def drawText(text,font,surface,x,y):
    #使用render()创建一个Surface对象，文本以特定的字体渲染其上
    textobj=font.render(text,1,TEXTCOLOR)
    #get.rect()返回函数Rect对象（拥有宽度和高度的一个副本）
    textrect=textobj.get_rect()
    #修改textrect的topleft属性
    textrect.topleft=(x,y)
    surface.blit(textobj,textrect)


pygame.init()
mainClock=pygame.time.Clock()
#set.mode()函数的第二个参数是可选的，传递pygame.FULLSCREEN使窗口占满屏幕
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHIGHT))
#windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHIGHT),pygame.FULLSCREEN)
pygame.display.set_caption("Dodger")
#使用pygame.mouse.set_visible()函数设置鼠标是否在窗口可见
pygame.mouse.set_visible(False)

#设置对象
font=pygame.font.SysFont(None,48)
gameOverSound=pygame.mixer.Sound("D:\\Dataset\\手雷音效.mp3")
pygame.mixer.music.load("D:\\Dataset\\超级玛丽游戏音效.mp3")
playerImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\test.jpg")
playerImage=pygame.transform.scale(playerImage,(50,50))
playerRect=playerImage.get_rect()
baddieImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\timg.jpg")

#显示开始页面
windowSurface.fill(BACKGROUNDCOLOR)
drawText('Dodger',font,windowSurface,(WINDOWWIDTH/3),(WINDOWHIGHT/3))
drawText('start',font,windowSurface,(WINDOWWIDTH/3)-30,(WINDOWHIGHT/3)+50)
pygame.display.update()
waitForPlayTopPressKey()

#开始游戏
topScore=0
while True:
    #创建baddies字典列表
    baddies=[]
    #敌人的属性，rect位置，speed落下的速度
    #surface缩放后的敌人绘制于其上的Surface对象（这个对象绘制于set_mode()函数返回的对象上）
    score=0#重置玩家的分数
    playerRect.topleft=(WINDOWWIDTH/2,WINDOWHIGHT-50)

    #设置玩家移动和作弊的变量
    moveLeft=moveRight=moveUp=moveDown=False
    reverseCheat=slowCheat=False
    baddieAddCounter=0

    #播放背景音乐
    pygame.mixer.music.play(-1,0.0)


    #游戏循环
    while True:
        score+=1
        for event in pygame.event.get():
            if event.type==QUIT:
                terminate()

            if event.type==KEYDOWN:
                if event.key==K_z:
                    reverseCheat=True
                if event.key==K_x:
                    slowCheat=True
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

            if event.type==KEYUP:
                if event.key==K_z:
                    reverseCheat=False
                    score=0
                if event.key==K_x:
                    slowCheat=False
                    score=0
                if event.key==K_ESCAPE:
                    terminate()

                if event.key==K_LEFT or event.key==K_a :
                    moveLeft=False
                if event.key==K_RIGHT or event.key==K_d :
                    moveRight=False
                if event.key==K_UP or event.key==K_w :
                    moveUp=False
                if event.key==K_DOWN or event.key==K_s :
                    moveDown=False

            #鼠标移动玩家
            if event.type==MOUSEMOTION:
                playerRect.centerx=event.pos[0]
                playerRect.centery=event.pos[1]

        if not reverseCheat and not slowCheat:
            baddieAddCounter+=1

        #添加新的敌人
        if baddieAddCounter==ADDNEWBADDIERATE:
            baddieAddCounter=0
            baddieSize=random.randint(BADDIEMINSIZE,BADDIEMAXSIZE)
            newBaddie={'rect':pygame.Rect(random.randint(0,WINDOWWIDTH-baddieSize),0-baddieSize,baddieSize,baddieSize),
                       'speed':random.randint(BADDIEMINSPEED,BADDIEMAXSPEED),
                       'surface':pygame.transform.scale(baddieImage,(baddieSize,baddieSize))
                       }
            baddies.append(newBaddie)

        #移动玩家和敌人
        if moveDown and playerRect.bottom < WINDOWHIGHT:
            #move_ip()函数表示将Rect对象的位置水平或垂直的移动多个像素
            #第一个参数是向右移动(赋负值向左)，第二个参数向上移动
            playerRect.move_ip(0,PLAYERMOVERATE)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0,-1*PLAYERMOVERATE)
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1*PLAYERMOVERATE,0)
        if moveRight and playerRect.right < WINDOWWIDTH:
            playerRect.move_ip(PLAYERMOVERATE,0)

        #移动敌人
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0,b['speed'])
            elif reverseCheat:
               b['rect'].move_ip(0,-5)
            elif slowCheat:
                b['rect'].move_ip(0,1)

        #删除敌人
        for b in baddies[:]:
            if b['rect'].top>WINDOWHIGHT:
                baddies.remove(b)
        windowSurface.fill(BACKGROUNDCOLOR)

        #绘制玩家得分
        drawText('Score: %s'%(score),font,windowSurface,10,0)
        drawText('Top Score: %s'%(topScore),font,windowSurface,10,40)

        #绘制玩家和敌人
        windowSurface.blit(playerImage,playerRect)
        for b in baddies:
            windowSurface.blit(b['surface'],b['rect'])

        pygame.display.update()
        if playHasHitBaddie(playerRect,baddies):
            if score>topScore:
                topScore=score
            break
        mainClock.tick(FPS)

    #游戏结束屏幕
    pygame.mixer.music.stop()
    gameOverSound.play()
    drawText('GAME OVER',font,windowSurface,(WINDOWWIDTH/3),(WINDOWHIGHT/3))
    drawText('a key again',font,windowSurface,(WINDOWWIDTH/3)-80,(WINDOWHIGHT/3)+50)
    pygame.display.update()
    waitForPlayTopPressKey()
    gameOverSound.stop()