import pygame,time,sys
from pygame.locals import*

#初始化
pygame.init()
#设置常量
WINDOWHIGHT=400
WINDOWWIDTH=800
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
WHITE=(255,255,255)
#创建窗口
windowSurface=pygame.display.set_mode((WINDOWWIDTH,WINDOWHIGHT),0,32)
pygame.display.set_caption("Sprites and Sounds")

#添加精灵
player=pygame.Rect(300,100,40,40)
#读取图片，函数接收字符串(文件路径)，返回Surface对象
playerImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\test.jpg")
#使用pygame.transform模块中的pygame.transform.scale()函数缩放精灵，函数返回Surface对象
#第一个参数是在其上绘制的Surface对象，第二个参数是一个新图像宽度和高度的元组
playerStretchedImage=pygame.transform.scale(playerImage,(40,40))
foodImage=pygame.image.load("D:\\BaiduNetdiskDownload\\PNG\\timg.jpg")

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

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_m:
                if musicPlaying:
                    #使用pygame.mixer.music.stop()暂停音乐
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1,0.0)
                #将开关设置设反
                musicPlaying=not musicPlaying
    windowSurface.fill(WHITE)
    #使用blit()函数绘制到窗口的Surface对象上
    windowSurface.blit(playerStretchedImage,player)
    pygame.display.update()